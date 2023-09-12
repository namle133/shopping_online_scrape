from bs4 import BeautifulSoup
from bs4.element import ResultSet

def get_product_names(soup: BeautifulSoup) -> ResultSet:
    selector = 'div.styles__StyledLoadingContainer-sc-1rrl9ib-0.jIJcEV div.CatalogProducts__Wrapper-sc-1hmhz3p-0.fSXJZx div a .name h3'
    name_items = soup.select(selector=selector)
    return name_items

def get_price_items(soup: BeautifulSoup) -> ResultSet:
    selector = 'div.styles__StyledLoadingContainer-sc-1rrl9ib-0.jIJcEV div.CatalogProducts__Wrapper-sc-1hmhz3p-0.fSXJZx div .price-discount__price'
    price_items = soup.select(selector=selector)
    return price_items

def get_historical_sold(soup: BeautifulSoup) -> ResultSet:
    selector = 'div.styles__StyledLoadingContainer-sc-1rrl9ib-0.jIJcEV div.CatalogProducts__Wrapper-sc-1hmhz3p-0.fSXJZx div a .style__StyledRatingList-sc-7xd6qw-6.eMNcac'
    sold_infos =  soup.select(selector=selector)
    return sold_infos

def get_product_info(soup: BeautifulSoup) -> str:
    name_items = get_product_names(soup=soup)
    price_items = get_price_items(soup=soup)
    sold_items =  get_historical_sold(soup=soup)

    for index in range(len(name_items)):
        product_info = "{0}, '|', {1} , '|', {2} \n".format(name_items[index].text, price_items[index].text, sold_items[index].text)
        yield product_info
    