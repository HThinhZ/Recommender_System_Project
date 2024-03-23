# Import libraries
import requests
from bs4 import BeautifulSoup
import re
import json
from time import sleep
import random

# Initial varibles:
PATH = "C:/Users/ADMIN/Processing/DSApplication_Project/Processing/T1_CollectingData/"

# Initial Class
class Movie_Scraper:
    def __init__(self):
        pass
    
    def scrape_movie_ratings(self, container):
        # Inital lists:
        user_id = []
        user_rating = []
        
        # Regex pattern 
        pattern = r'\/user\/(ur\d+)'
        
        for content in container:
            user_tag = content.find('span', class_ = "display-name-link")
            rating_tag = content.find_all('span', class_= "rating-other-user-rating")
                
            try: 
                user_id_re = re.findall(pattern, str(user_tag.find('a')['href']))
                user_id.append(user_id_re[0])
            except:
                user_id.append("")
            
            try:
                rating = rating_tag[0].find('span')
                user_rating.append(rating.text)
            except:
                user_rating.append("")
        
        return (user_id, user_rating)
        
    def scrape_movie(self, movie_id):
        # Inital variables:
        data = {}
        users_id = []
        movies_id = []
        users_rating = []
       
        page = requests.get(f"https://www.imdb.com/title/{movie_id}/reviews/?ref_=tt_ql_2")
        soup = BeautifulSoup(page.text, 'html.parser')
        
        container = soup.find_all('div', class_ = "lister-item-content")
        
        movie_ratings = self.scrape_movie_ratings(container)
        users_id.extend(movie_ratings[0])
        users_rating.extend(movie_ratings[1])
        movies_id.extend([movie_id]*len(movie_ratings[0]))
        
        file_path = PATH + "data/puser_id.json"
        
        with open(file_path, 'r') as json_file:
            puser_id = json.load(json_file)
        
        for user_id in users_id:
            if user_id not in puser_id:
                puser_id[user_id] = False
            
        
        key_tag = soup.find('div', class_ = "load-more-data")
        next_key = key_tag['data-key']
        
        npage = 0
        while npage < 10:
            npage = npage + 1
            sleep(random.uniform(1,3))
            print(f"Scraping page {npage} !!!")
            headers = {
                'authority': 'www.imdb.com',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                # 'cookie': 'session-id=132-9465593-9579807; ubid-main=135-6830841-7942246; x-main=w0ZaH5Eo3FmqVdfuysdVNtYtfKr3ZcI2HRoZI0XQ0JcXNqFZ4dR4GgtS5NhNzMVX; at-main=Atza|IwEBIOSayYl4Fq5MXlnWj-XCeod479dbf5kNoLnC3G73bhkNsW3WySbj_TBGXn7SJzeRVLAaJPWDpY1lffbqCzw-a4Y-NhZhNMqv5OkiLpxSvYhr-oE6q0affb-aYD31fzp__S9ApxOTsD1fnxcRdGg0c_oQ3_YogUfqGkmX-pV5YO5FlYgcdhX0RwFhAAitQkHNX3SoQzH-Yj41k8K2c_W0_vWyXgPmgi0HS_eyUWKkayADgA; sess-at-main="6tsRA4li+0+CoTNmqSzcYfAM3/wZF4TOP8JKh3ENzNg="; uu=eyJpZCI6InV1ZDA3NDU0MmVmNmIxNGVhODk5YTUiLCJwcmVmZXJlbmNlcyI6eyJmaW5kX2luY2x1ZGVfYWR1bHQiOmZhbHNlfSwidWMiOiJ1cjE3MjkzODc4NSJ9; session-id-time=2082787201l; ad-oo=0; ci=e30; session-token=Z7dHB0TQ5DLJOaJkuJ8MXy+BSqhpENAgIJw6L/LcTou8LYfGDwMvclmnwkSz8f3T01eavzh5A19ftc8HM3ZlqaXKKfscowg2n1+XFOHpEu5aIha4+Cgnzzy6CU0tgGHlaU0eowtdnehLyVGzjryCHb4xPiTiGmDHYv/SzJ0rqfEvVr58CFxuZ/5UZ7hYDzyaLu+snwo9x2wFlp//KroDgnocbmXl5boYuA4O2ikjsfGAVJTScTfm/ovwlKZYCC3ZOtMpiCn8G/+MTe0y4nhaceBr/kDyh21TzkjqZvLcCP4FVUrqY0oqK5+b2HCl2PSY6976m6g78k/D3bIfaywXCm5qlcnYj8N5mITkfein+XA3SABVqGD+jYxMhDX4Rm1s; csm-hit=tb:H48GE6BC66YDMACCT10B+s-VNKN7C39WABVD60XCYNF|1711017733239&t:1711017733239&adb:adblk_no',
                'referer': f'https://www.imdb.com/title/{movie_id}/reviews/?ref_=tt_ql_2',
                'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Microsoft Edge";v="122"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0',
                'x-requested-with': 'XMLHttpRequest',
            }
        
            params = {
                'ref_': 'undefined',
                'paginationKey': next_key,
            }
                    
            page = requests.get(f"https://www.imdb.com/title/{movie_id}/reviews/_ajax", headers=headers, params=params)
            soup = BeautifulSoup(page.text, 'html.parser')
            
            container = soup.find_all('div', class_ = "lister-item-content")
            
            movie_ratings = self.scrape_movie_ratings(container)

            users_id.extend(movie_ratings[0])
            movies_id.extend([movie_id]*len(movie_ratings[0]))
            users_rating.extend(movie_ratings[1])
            
            key_tag = soup.find('div', class_ = "load-more-data")
            next_key = key_tag['data-key'] 
            
            data['user_id'] = users_id
            data['movie_id'] = movies_id
            data['user_rating'] = users_rating
            
            
            file_path_data = PATH + "data/data_mur.json"
            
            for user_id in users_id:
                if user_id not in puser_id:
                    puser_id[user_id] = False
            
            with open(file_path_data, 'w') as json_file:
                json.dump(data, json_file)
                
            with open(file_path, 'w') as json_file:
                json.dump(puser_id, json_file)
            



