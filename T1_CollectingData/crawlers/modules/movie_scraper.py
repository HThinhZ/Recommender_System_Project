# Import libraries
import requests
from bs4 import BeautifulSoup

# Init
class Movie_Scraper:
    def __init__(self):
        self.movies_id = []
        
    def scrape_movie_ratings(self, movie_id):
        page = requests.get(f"https://www.imdb.com/title/{movie_id}/reviews/?ref_=tt_ql_2")
        soup = BeautifulSoup(page.text)
        
        



