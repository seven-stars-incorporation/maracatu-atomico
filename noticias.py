import requests, emoji
from bs4 import BeautifulSoup
# import os

class Noticias():
    # G1
    def g1():
        url = 'http://g1.com.br/'
        header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                        'AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/51.0.2704.103 Safari/537.36'}

        resposta = requests.get(url, headers= header)

        if resposta.status_code == 200:
            conteudo = resposta.content
            site = BeautifulSoup(conteudo, 'html.parser')
            noticia = site.find('div', attrs={'class' : 'row medium-uncollapse bastian-container small-collapse medium-collapse large-uncollapse'})

            lista_links = []

            for link in noticia.find_all('a'):
                lista_links.append(link.get('href'))

            # Esses indices se repitiram em todos os testes, por isso estou tirando eles
            del lista_links[1]
            del lista_links[1]
            del lista_links[2]
            del lista_links[3]
            del lista_links[3]

            try:
                for i in range(0, 5):
                    print(f'Link: {lista_links[i]}')

            except:
                print(emoji.emojize('Não consigo te apresentar os links :disappointed:\nDesculpa')) 

        else:
            print(emoji.emojize(f'Minha requisição foi negada :disappointed:\nStatus: {resposta.status_code}'))


    # Estadão
    def estadao():
        url = 'https://www.estadao.com.br/'
        header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                'AppleWebKit/537.36 (KHTML, like Gecko) '
                                'Chrome/51.0.2704.103 Safari/537.36'}

        resposta = requests.get(url, headers= header)

        if resposta.status_code == 200:

            conteudo = resposta.content
            site = BeautifulSoup(conteudo, 'html.parser')

            noticia = site.find('div', attrs={'class' : 'intro'})

            lista_links = []
            try:
                for link in noticia.find_all('a'):
                    lista_links.append(link.get('href'))

                for i in range(0, 3):
                    print(f'Link: {lista_links[i]}')
            except:
                print(emoji.emojize('Não consigo te apresentar os links :disappointed:\nDesculpa'))
                
        else:
            print(emoji.emojize(f'Minha requisição foi negada :disappointed:\nStatus: {resposta.status_code}'))

    #Em Desenvolvimento:

    # R7
    def r7():
        print(emoji.emojize(f'Esse site tá perguntando se eu sou um robô :disappointed:\nAguenta um pouquinho que eu vou enganar ele hehehe :smiling_imp:\nCaso queria acessar, está aqui o link: https://www.r7.com/'))

    # Google Noticias
    def gn():
        print(emoji.emojize(f'Esse site tá perguntando se eu sou um robô :disappointed:\nAguenta um pouquinho que eu vou enganar ele hehehe :smiling_imp:\nCaso queria acessar, está aqui o link: https://news.google.com/'))

