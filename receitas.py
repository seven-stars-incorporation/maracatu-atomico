import requests
from bs4 import BeautifulSoup


url = 'http://g1.com.br/'
header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                        'AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/51.0.2704.103 Safari/537.36'}

resposta = requests.get(url, headers= header)

if resposta.status_code == 200:
    print("Segura ae")