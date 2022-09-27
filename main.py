import discord, requests
from bs4 import BeautifulSoup
# import os

client = discord.Client()

@client.event
async def on_ready():
    print('Tudo certo. Bot: {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$help'):
        await message.channel.send(
            'Olá, sou o bot de nóticias :smiling_face_with_3_hearts: ```\n$help => Mostra os comandos\n$ping => Mostra o ping da minha casa até aqui\n\n$g1 => 5 Noticias do G1\n$estadao => 3 Noticias do Estadão\n\n>>>>>COMANDOS EM DESESNVOLVIMENTO<<<<\n$r7 => Noticias da Record\n$gn => Google News```'
            )

    if message.content.startswith('$ping'):
        await message.channel.send(
            f'Pong! :ping_pong: {round(client.latency * 1000)}ms'
        )

# A brincadeira começa daqui :)

    # G1
    if message.content.startswith('$g1'):
    
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

            for i in range(0, 5):
                await message.channel.send(f'Link: {lista_links[i]}')
        else:
            await message.channel.send(
                f'Minha requisição foi negada :disappointed:\nStatus: {resposta.status_code}'
                )


    # Estadão
    if message.content.startswith('$es'):

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

            for link in noticia.find_all('a'):
                lista_links.append(link.get('href'))

            for i in range(0, 3):
                await message.channel.send(f'Link: {lista_links[i]}')

        else:
            await message.channel.send(
                f'Minha requisição foi negada :disappointed:\nStatus: {resposta.status_code}'
                )

#Em Desenvolvimento:

    # R7
    if message.content.startswith('$r7'):
        await message.channel.send(f'Esse site tá perguntando se eu sou um robô :disappointed:\nAguenta um pouquinho que eu vou enganar ele hehehe :smiling_imp:\nCaso queria acessar, está aqui o link: https://www.r7.com/')

    # Google Noticias
    if message.content.startswith('$gn'):
        await message.channel.send(f'Esse site tá perguntando se eu sou um robô :disappointed:\nAguenta um pouquinho que eu vou enganar ele hehehe :smiling_imp:\nCaso queria acessar, está aqui o link: https://news.google.com/')




client.run('OTI4NzQ4MjY2NzE0MTc3NjA3.YddSOg.dAVVfKUQa-WmrBFlh8jHdXt6D9E')
