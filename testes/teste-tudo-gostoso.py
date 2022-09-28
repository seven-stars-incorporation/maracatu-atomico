import requests
from bs4 import BeautifulSoup
header = {
    ':authority:' 'www.tudogostoso.com.br',
    ':method:' 'GET',
    ':path:' '/',
    ':scheme:' 'https',
    'accept:' 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding:' 'gzip, deflate, br',
    'accept-language:' 'pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control:' 'max-age=0',
    'cookie:' '_ga=GA1.3.664846419.1664376295; _gid=GA1.3.1083025205.1664376295; _fbp=fb.2.1664376294702.456628332; _pbjs_userid_consent_data=3524755945110770; nvg55810=11760be0efa129b6310da3346f10|0_272; __cf_bm=9xJXpkxIYEDZEmkCp4oBMwknVu7l3XUKTGRABytz5Mw-1664376296-0-AZa7xx7Nz569y1ebCJ6IVgGKbyjTTdcpXGAEXTpoX84skjd5Uov+67iCZFEwLJdNpGnPjt/sEEeK4DNbqTM8IHh7odycrjfrqIxdjB/RL7Uqby2w37E5jlorLqZykK7cVXuaNqn6wQ9VQorBa8UytTMb39EIWn4Uc8B6yutuv7hw; __gads=ID=58b238259efe045d:T=1664376298:S=ALNI_MYE-5rF1WQw4gr3OQSHPkE_9yimNA; __gpi=UID=0000097633ced954:T=1664376298:RT=1664376298:S=ALNI_MbmtWpo3ZlMo9o9s36NGIgCoaMyVQ; _pin_unauth=dWlkPU4yVTJOVFJsTXpFdE16QTROQzAwTlRnNExXSmpZakF0WWpFeE9UYzVNelk1TURGaA; tt_c_vmt=1664376485; tt_c_c=search; tt_c_s=search; tt_c_m=search; _ttuu.s=1664376485309; tt.u=0100007FA65E3463DD063F3002E01310; tt.nprf=; _ttdmp=|LS:|CA:CA6172; _gat_UA-54622095-1=1',
    'sec-ch-ua:' '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
    'sec-ch-ua-mobile:' '?0',
    'sec-ch-ua-platform:' '"Windows"',
    'sec-fetch-dest:' 'document',
    'sec-fetch-mode:' 'navigate',
    'sec-fetch-site:' 'none',
    'sec-fetch-user:' '?1',
    'upgrade-insecure-requests:' '1',
    'user-agent:' 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
}

url = 'https://www.tudogostoso.com.br/'

resp = requests.get(url, headers= header)


if resp.status_code == 200:
    print("Requisição OK")

else:
    print(resp.status_code)