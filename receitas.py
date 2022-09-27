import requests
from bs4 import BeautifulSoup

class Receitas():
    
    def geral():
        header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/51.0.2704.103 Safari/537.36'
    }

        print("Antes de tudo, de qual site você busca a receita?")
        print("Receita Da Hora [1]\nPanelinha [2]\nTudo Gostoso [3]")

        escolha = int(input("> "))

        match escolha:
            case 1:
                print("Receita da Hora :)")    
                pqs = input("Ingrediente Principal em uma palavra: ")
                url = 'https://www.receitadahora.com/?s='+pqs

                resposta = requests.get(url, headers= header)

                if resposta.status_code == 200:
                    print("Requisição OK")

            
            
            
            case 2:
                print("Panelinha :)")

            case 3: 
                print("Tudo gostoso")

            case _:
                print("Escolha uma opção válida")