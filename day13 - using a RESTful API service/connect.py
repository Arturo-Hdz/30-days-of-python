from re import search
from sys import api_version
from unittest import result
from wsgiref import headers
import requests
import pprint
import pandas as pd

api_key = "dd884c862fa83a21eb42856b3db11597"
api_key_v4 = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkZDg4NGM4NjJmYTgzYTIxZWI0Mjg1NmIzZGIxMTU5NyIsInN1YiI6IjYyMGRkNjQ3Yjg0Zjk0MDA0MTkyMjk4OSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.WfxIHGkNaJsTdS9-a04x0VW-HdTMSu8y20DDRUlv6dw"

#http request methods
"""
GET -> grab data
POST -> add/update data

PATCH
PUT
DELETE
"""

# whats our endpoint (url)

# what is the HTTP method that we need?

"""
Endpoint
/movie/{movie_id}
https://api.themoviedb.org/3/movie/550?
api_key=dd884c862fa83a21eb42856b3db11597
"""
movie_id = 500
api_version = 3
api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/movie/{movie_id}"
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"
print(endpoint)

headers = {
       'Authorization': f'Bearer {api_key_v4}',
       'Content-Type': 'application/json;charset=utf-8'
}
# r = requests.get(endpoint) # json={"api_key": api_key})
r = requests.get(endpoint, headers=headers) 
print(r.status_code)
# print(r.text)

api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/search/movie"
search_query = "The Matrix"
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}&query={search_query}"
# print(endpoint)
r = requests.get(endpoint)
# pprint.pprint(r.json())

if r.status_code in range(200, 299):
    data = r.json()
    results = data['results']
    if len(results) > 0:
       print(results[0].keys())
       movie_ids = set()
       for result in results:
              _id = result['id']
              print(result['title'], _id)
              movie_ids.add(_id)
       print(list(movie_ids))

output = 'movies.csv'
movie_data = []
for movie_id in movie_ids:
    api_version = 3
    api_base_url = f"https://api.themoviedb.org/{api_version}"
    endpoint_path = f"/movie/{movie_id}"
    endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"
    r = requests.get(endpoint)
    if r.status_code in range(200, 299):
       data= r.json()
       movie_data.append(data)
    print(r.json())

df = pd.DataFrame(movie_data)
print(df.head())
df.to_csv(output, index=False)