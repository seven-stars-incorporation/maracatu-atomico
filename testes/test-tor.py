import requests 
req = requests.session() 
req.proxies = {'http': 'socks5://127.0.0.1:9050', 
    'https': 'socks5://127.0.0.1:9050'
    } 
    
def request_tor(url): 
    page = req.get(url) 
    text = page.text 
    return text 
    print(request_tor)