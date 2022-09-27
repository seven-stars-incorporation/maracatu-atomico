import requests
from bs4 import BeautifulSoup

url = 'https://haveibeenpwned.com/unifiedsearch/email'
header = {
    'Host' : 'haveibeenpwned.com',
    'user-agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0',
    'Accept' : '*/*',
    'Accept-Language' : 'pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3',
    'Referer' : 'https://haveibeenpwned.com/',
    'X-Requested-With' : 'XMLHttpRequest',
    'Cookie' : '__cf_bm=nY37cuHjhzGvfDnhhUULtrmrM2xXrFBJLOHX0dlBFQ8-1641752851-0-AQ+stl5RUDWTA/9SCo8VFxkSiPabgVf1t/yK9jPhsVQysl9thintqFTODzT8hSyB2aL6e3Nnul4OhBi2jir4mUnLS7IgKOejiARzTGHTM29QObi+xNECXDUN5rXc1P+LpW2aEY3TvmKO1GfxLLdoSBYZx5Uh0aHhirS6VSeeVy3q; ai_user=wBHzR|2022-01-09T18:27:30.828Z; _ga=GA1.2.32892139.1641752851; _gid=GA1.2.1554994716.1641752851; _gat=1; ai_session=kKH9W|1641752851124|1641752851124'
        }

resposta = requests.get(url, headers= header)

print(resposta.status_code)
print(resposta.content)




# site = BeautifulSoup(conteudo, 'html.parser')

# noticia = site.find('div', attrs={'class' : 'intro'})

# lista_links = []

# for link in noticia.find_all('a'):
#     lista_links.append(link.get('href'))

# for i in range(0, 3):
#     print(f'Link: {lista_links[i]}')

# titulo = noticia.find('a', attrs={'class' : 'feed-post-link'})

# print(titulo.text)
