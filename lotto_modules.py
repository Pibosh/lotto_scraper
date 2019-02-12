import requests
import re
from bs4 import BeautifulSoup


def open_page(data):
    url = 'https://www.lotto.pl/lotto/wyniki-i-wygrane/wyszukaj'
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0'}
    payload = {'data_losowania[date]': data, 'form_build_id': 'form-880053ca8105560cf9cd0e52d616608d',
               'form_id': 'lotto_wyszukaj_form', 'op': ''}
    req = requests.post(url, data=payload, headers=headers)
    if req.status_code == 200:
        req.encoding = 'UTF-8'
        return req.content
    else:
        return False


def lotto_numbers(data):
    soup = BeautifulSoup(open_page(data), features="html.parser")
    whole_results = soup.find('div', attrs={"class": re.compile(r'resultsItem lotto sortrosnaco')})
    if whole_results is None:
        return None
    else:
        numbers = whole_results.find_all('span')
        lucky_numbers = []
        for number in numbers:
            number = number.string.strip()
            lucky_numbers.append(number)

        return lucky_numbers
