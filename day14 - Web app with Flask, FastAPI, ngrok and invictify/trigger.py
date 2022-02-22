import requests

ngrok_url = 'https://05c6-50-42-225-52.ngrok.io'
endpoint = f'{ngrok_url}/box-office-mojo-scraper'

r = requests.post(endpoint, json={})
print(r.json()['data'])