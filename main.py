import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import datetime

def collect_data(city_code='2398'):
    current_time = datetime.datetime.now().strftime('%d_m_%Y_%H_%M')

    ua = UserAgent()

    headers = {
        'User-Agent': ua.random,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }

    cookies = {
        'mg_geo_id': f'{city_code}'
    }
    response = requests.get(url='https://magnit.ru/promo/', headers=headers, cookies=cookies)

    # with open('data.html', 'w', encoding='UTF-8') as file:
    #     file.write(response.text)

    with open('data.html', encoding='UTF-8') as file:
        src = file.read()

    soup = BeautifulSoup('src', 'lxml')
    city = soup.find("a", class_="header__contacts-link header__contacts-link_city")
    print(city)


def main():
    collect_data()

if __name__ == '__main__':
    main()