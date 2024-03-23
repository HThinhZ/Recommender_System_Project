import requests
import json

def crawl_movie_inf(movie_id):
    insert_data = {}
    url = "https://imdb-api.huyvongmongmanh75.workers.dev/title/" + movie_id;
    response = requests.get(url)
    data = response.json()

    insert_data["movie_id"] = movie_id
    insert_data["title"] = data["title"]
    insert_data["introduction"] = data["plot"]
    insert_data["runtime"] = data["runtime"]
    insert_data["rating"] = data["rating"]
    insert_data["award"] = data["award"]
    insert_data["genre"] = data["genre"]
    insert_data["releaseDate"] = data["releaseDetailed"]["date"][:10]
    insert_data["releaseLocation"] = data["releaseDetailed"]["releaseLocation"]["country"]
    insert_data["actors"] = data["actors"]
    insert_data["directors"] = data["directors"]
    return insert_data



data = crawl_movie_inf("tt31174028")
json_string = json.dumps(data, indent=4)  
print(json_string)