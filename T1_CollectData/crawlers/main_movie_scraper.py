from modules.movie_scraper import *

# Main:
file_path = PATH + "data/pmovie_id.json"
with open(file_path, 'r') as json_file:
    pmovie_id = json.load(json_file)

movie_scraper = Movie_Scraper()
index = 1
for key, value in pmovie_id.items():
    if value == False:
        print(f"Movie {index}: <Title: {key}>!!!")
        movie_scraper.scrape_movie(key)
        pmovie_id[key] = True
        index = index + 1
        
        try:
            with open(file_path, 'w') as json_file:
                json.dump(pmovie_id, json_file)
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt: File opening process interrupted.")