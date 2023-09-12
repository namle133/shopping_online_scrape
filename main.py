from config.config import ShoppingOnlineLocation
from bs4 import BeautifulSoup
from driver.driver import create_web_driver
import tiki.tiki_scraper as tiki_scraper
import lazada.lazada_scraper as lazada_scraper
import shopee.shopee_scraper as shopee_scraper
from config.input import input_initial_value
from config.input import add_to_cart

def shopping_online_run(location: str, keyword: str, page: str):
    # location, keyword, page = input_initial_value()

    shopping_online_info = ShoppingOnlineLocation(
        location=location, 
        keyword=keyword, 
        page=page,
    )

    base_url = shopping_online_info.get_base_url()
    print(base_url)
    browser = create_web_driver(base_url, location)
    html = browser.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
    soup = BeautifulSoup(html, "html.parser")

    match location:
        case "tiki":
            product_info = tiki_scraper.get_product_info(soup=soup)
            shopping_online_info.add_product_to_csv(product_info)
        case "lazada":
            product_info = lazada_scraper.get_product_info(soup=soup)
            shopping_online_info.add_product_to_csv(product_info)
        case "shopee":
            is_choose = add_to_cart()
            if is_choose:
                index_item = int(input("Please fill item's index you want to add it in cart: "))
                shopee_scraper.add_product_to_cart(browser, soup, index_item)
            else:
                product_info = shopee_scraper.get_product_info(soup=soup)
                shopping_online_info.add_product_to_csv(product_info)

        
            
   