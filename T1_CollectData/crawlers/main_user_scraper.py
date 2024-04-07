from modules.user_scraper import *

# Main:
file_path = PATH + "data/puser_id.json"
with open(file_path, 'r') as json_file:
    puser_id = json.load(json_file)
    
user_scraper = User_Scraper()
index = 1
for key, value in puser_id.items():
    if value == False:
        print(f"User {index}: <Id: {key}>!!!")
        user_scraper.scrape_user(key)
        puser_id[key] = True
        index = index + 1
        
        try:
            with open(file_path, 'w') as json_file:
                json.dump(puser_id, json_file)
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt: File opening process interrupted.")