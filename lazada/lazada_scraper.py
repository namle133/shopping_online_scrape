from bs4 import BeautifulSoup
from bs4.element import ResultSet

def get_product_names(soup: BeautifulSoup) -> ResultSet:
    selector = '._17mcb .Bm3ON .buTCk .RfADt a'
    name_items = soup.select(selector=selector)
    return name_items

def get_price_items(soup: BeautifulSoup) -> ResultSet:
    selector = '._17mcb .Bm3ON .buTCk .aBrP0 .ooOxS'
    price_items = soup.select(selector=selector)
    return price_items

def get_historical_sold(soup: BeautifulSoup) -> ResultSet:
    selector = '._17mcb .Bm3ON .buTCk ._6uN7R'
    sold_items = soup.select(selector=selector)
    return sold_items

def get_product_origin(soup: BeautifulSoup) -> ResultSet:
    selector = '._17mcb .Bm3ON .buTCk ._6uN7R .oa6ri'
    product_origin = soup.select(selector=selector)
    return product_origin

def get_sold_item_at_index(index: int, sold_items: ResultSet) -> str:
    sold_item = sold_items[index].select('._1cEkb')
    if len(sold_item) < 1:
        return str(0)
    return sold_item[0].text

def get_product_info(soup: BeautifulSoup) -> str:
    name_items = get_product_names(soup=soup)
    price_items = get_price_items(soup=soup)
    sold_items = get_historical_sold(soup=soup)
    product_origin = get_product_origin(soup=soup)

    for index in range(len(name_items)):
        sold_item = get_sold_item_at_index(index, sold_items)
        product_info = "{0}, '|', {1} , '|', {2} , '|', {3} \n".format(name_items[index]['title'], price_items[index].text, sold_item, product_origin[index].text)
        yield product_info
    