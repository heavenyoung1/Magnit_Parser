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
        # src = file.read()
        soup = BeautifulSoup(response.text, 'lxml')
        # city = soup.find('a', class_='header__contacts-link_city').text.strip()
        # print(city)

        cards = soup.find_all('a', class_='card-sale_catalogue')
        # print(cards)
        # print(len(cards))
        for card in cards:
            try:
                title = card.find('div', class_='card-sale__title').text.strip()
                sale = card.find('div', class_='card-sale__discount').text.strip()

                #old_price_integer = card.find('span', class_='label__price-integer').text.strip()
                old_price_integer = card.find('div', class_='label__price_old').find('span', class_='label__price-integer').text.strip()
                old_price_decimal = card.find('div', class_='label__price_old').find('span', class_='label__price-decimal').text.strip()
                #old_price_decimal = card.find('span', class_='label__price-decimal').text.strip()
                old_price = f'{old_price_integer}.{old_price_decimal}'

                new_price_integer = card.find('span', class_='label__price-integer').text.strip()
                new_price_decimal = card.find('span', class_='label__price-decimal').text.strip()

                print(title, sale, old_price)

            except AttributeError:
                continue



def main():
    collect_data()

if __name__ == '__main__':
    main()