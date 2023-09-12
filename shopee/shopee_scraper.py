from bs4 import BeautifulSoup
from bs4.element import ResultSet
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from time import sleep

shopee_parth = "https://shopee.vn"
shopee_cart = "https://shopee.vn/cart"

def get_product_names(soup: BeautifulSoup) -> ResultSet:
    selector = '.KMyn8J .dpiR4u .FDn--\+'
    name_items = soup.select(selector=selector)
    return name_items

def get_price_items(soup: BeautifulSoup) -> ResultSet:
    selector = '.KMyn8J .hpDKMN .vioxXd.rVLWG6'
    price_items = soup.select(selector=selector)
    return price_items

def get_product_origin(soup: BeautifulSoup) -> ResultSet:
    selector = '.KMyn8J .zGGwiV'
    product_origin = soup.select(selector=selector)
    return product_origin

def get_historical_sold(soup: BeautifulSoup) -> ResultSet:
    selector = '.KMyn8J .ZnrnMl'
    sold_items = soup.select(selector=selector)
    return sold_items

def get_sold_item_at_index(index: int, sold_items: ResultSet) -> str:
    sold_item = sold_items[index].text
    if len(sold_item) < 1:
        return "Đã bán " + str(0)
    return sold_item

def get_link_items(soup: BeautifulSoup) -> ResultSet:
    selector = '.col-xs-2-4.shopee-search-item-result__item a'
    link_items = soup.select(selector)
    return link_items

def get_link_item_at_index(soup: BeautifulSoup, index: int) -> str:
    link_items = get_link_items(soup)
    total_items = len(link_items)
    
    for i in range(total_items):
        if i == index:
            return link_items[index]['href']
    return ""

def get_product_info(soup: BeautifulSoup) -> str:
    name_items = get_product_names(soup=soup)
    price_items = get_price_items(soup=soup)
    sold_items = get_historical_sold(soup=soup)
    product_origin = get_product_origin(soup=soup)
    link_items = get_link_items(soup=soup)

    for index in range(len(name_items)):
        sold_item = get_sold_item_at_index(index, sold_items)
        product_info = "{0}, '|', {1} , '|', {2} , '|', {3} , '|', {4} \n".format(name_items[index].text, price_items[index].text, sold_item, product_origin[index].text, link_items[index]['href'])
        yield product_info
        
def add_product_to_cart(driver : WebDriver,soup: BeautifulSoup ,index: int):
    url = get_link_item_at_index(soup, index)
    link_item = shopee_parth + url
    driver.get(link_item)
    sleep(5)
    
    elem = driver.find_element(By.XPATH, '//button[normalize-space()="thêm vào giỏ hàng"]')
    elem.click()
    
    sleep(2)
    driver.get(shopee_cart)
    sleep(8)
    print("add to cart successfully")
    driver.quit()
    
    
    
    
    
    
