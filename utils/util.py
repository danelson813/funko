import requests
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent


def get_url(i: int) -> str:
    return f"https://funko.com/fandoms/?start={i*20}&sz=20"


def get_soup_req(url):
    ua = UserAgent()
    useragent = ua.random
    useragent = "'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
    session = requests.Session()
    session.headers.update({'User-agent': useragent})

    response = session.get(url)

    soup = bs(response.text, 'html.parser')
    return soup 


def main(url):
    soup = get_soup_req(url)
    items = soup.select('li.col-6.col-lg-3.mt-3.mt-md-6.col-xl-5ths.product-tile-col')
    results = []
    # parse the list
    for item in items:
        title = item.select_one('h2.pdp-link.mb-2 > a').text
        product_license = item.select_one('div.product-license').text.strip()
        price = item.select_one('span.sales').text.strip()
        image_link = item.select_one('img.tile-image')['src']
        product_link = item.select_one('a.image-link')['href']
        result = {
            'title': title,
            'product_license': product_license,
            'price': price,
            'image_link': image_link,
            'product_link': product_link
            }
        results.append(result)
    return results
