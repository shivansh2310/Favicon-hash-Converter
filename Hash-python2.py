import mmh3
import requests
 
response = requests.get('#favicon.ico URL')
favicon = response.content.encode('base64')
hash = mmh3.hash(favicon)
print hash
