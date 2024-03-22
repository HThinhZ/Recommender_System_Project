from modules.movie_scraper import *

# Main:
file_path = PATH + "data/pmovie_id.json"
with open(file_path, 'r') as json_file:
    pmovie_id = json.load(json_file)

movie_scraper = Movie_Scraper()
for key, value in pmovie_id.items():
    if value == False:
        movie_scraper.scrape_movie(key)
        pmovie_id[key] = True