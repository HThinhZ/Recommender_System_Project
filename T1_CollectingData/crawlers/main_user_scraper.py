from modules.user_scraper import *

# Main:
file_path = PATH + "data/puser_id.json"
with open(file_path, 'r') as json_file:
    puser_id = json.load(json_file)

user_scraper = User_Scraper()
for key, value in puser_id.items():
    if value == False:
        user_scraper.scrape_user(key)
        # pmovie_id[key] = True