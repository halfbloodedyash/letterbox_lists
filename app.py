from flask import Flask, request, render_template, send_file, url_for
import requests
from bs4 import BeautifulSoup
import csv
import os

app = Flask(__name__)

# Setup function to replace @app.before_first_request
def setup_static():
    os.makedirs(os.path.join(app.root_path, 'static', 'css'), exist_ok=True)
    
    # Create styles.css in the static folder
    css_path = os.path.join(app.root_path, 'static', 'css', 'styles.css')
    with open(css_path, 'w', encoding='utf-8') as f:
        # Copy the CSS content into the file
        f.write("""
        /* Your CSS content goes here - Copy all the CSS from the CSS artifact */
        """)

def scrape_letterboxd_list(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        return []
    
    soup = BeautifulSoup(response.text, 'html.parser')
    movie_elements = soup.select(".poster-container")
    
    movies = []
    for movie in movie_elements:
        title_tag = movie.find("img")
        if title_tag and 'alt' in title_tag.attrs:
            movies.append(title_tag['alt'])
    
    return movies

def create_letterboxd_csv(movie_list, file_path):
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Title"])  # Writing the header required by Letterboxd
        for movie in movie_list:
            writer.writerow([movie])

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        
        if not url.startswith('https://letterboxd.com/'):
            return render_template('index.html', error="Please enter a valid Letterboxd URL.")
            
        movies = scrape_letterboxd_list(url)
        
        if movies:
            csv_file_path = "letterboxd_movies.csv"
            create_letterboxd_csv(movies, csv_file_path)
            return render_template('index.html', download_link=csv_file_path, movie_count=len(movies))
        else:
            return render_template('index.html', error="No movies found. Please check the URL.")
    
    return render_template('index.html')

@app.route('/download')
def download():
    file_path = "letterboxd_movies.csv"
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    return "File not found", 404

if __name__ == '__main__':
    # Run the setup function before starting the app
    setup_static()
    app.run(debug=True)