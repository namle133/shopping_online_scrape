from bs4 import BeautifulSoup
from bs4.element import ResultSet

def get_product_names(soup: BeautifulSoup) -> ResultSet:
    selector = '''
        div#search 
        div.sg-col-20-of-24.s-matching-dir.sg-col-16-of-20.sg-col.sg-col-8-of-12.sg-col-12-of-16 
        .rush-component .s-latency-cf-section 
        div span.a-size-medium.a-color-base.a-text-normal'''
    name_items = soup.select(selector=selector)
    return name_items

def get_price_items(soup: BeautifulSoup) -> ResultSet:
    selector = '''
        div#search 
        div.sg-col-20-of-24.s-matching-dir.sg-col-16-of-20.sg-col.sg-col-8-of-12.sg-col-12-of-16 
        .rush-component .s-latency-cf-section 
        div div.a-row.a-size-base.a-color-base'''
    price_items = soup.select(selector=selector)
    return price_items

def get_price_items_at_index(soup: BeautifulSoup, index: int) -> str:
    selector = '''
        div#search 
        div.sg-col-20-of-24.s-matching-dir.sg-col-16-of-20.sg-col.sg-col-8-of-12.sg-col-12-of-16 
        .rush-component .s-latency-cf-section 
        div div.a-section.a-spacing-small.a-spacing-top-small'''
    price_items = soup.select(selector=selector)[index].select('div.a-row.a-size-base.a-color-base span.a-price span.a-offscreen')
    if len(price_items) == 0:
        return "unavailable"
    if len(price_items) > 1:
        price_item = ""
        for item in price_items:
            price_item += item.text + "-"
        return price_item[:-1]
    return price_items[0].text

def get_product_info(soup: BeautifulSoup) -> str:
    name_items = get_product_names(soup=soup)

    for idx in range(len(name_items)):
        price_items = get_price_items_at_index(soup=soup, index=idx)
        product_info = "{0}, '|', {1}  \n".format(name_items[idx].text, price_items)
        yield product_info
    