from config.filter_keyword import filter_string
# using datetime module
import datetime

def get_timestamp() -> str:
    # ct stores current time
    ct = datetime.datetime.now()
    print("current time:-", ct)
    
    # ts store timestamp of current time
    ts = ct.timestamp()
    return str(int(ts))

class ShoppingOnlineLocation:
    def __init__(self, location: str, keyword: str, page: str) -> None:
        self.location = location
        self.keyword = keyword
        self.page = page
        
    def get_base_url(self) -> str:
        match self.location:
            case "tiki":
                filter_keyword = filter_string(self.keyword, "%20")
                base_url = "https://tiki.vn/search?q={0}&page={1}".format(filter_keyword, self.page)
                return base_url
            case "shopee":
                filter_keyword = filter_string(self.keyword, "%20")
                base_url = "https://shopee.vn/search?keyword={0}&page={1}".format(filter_keyword, self.page)
                return base_url
            case "lazada":
                filter_keyword = filter_string(self.keyword, "-")
                base_url = "https://www.lazada.vn/tag/{0}/?page={1}".format(filter_keyword, self.page)
                return base_url
            case "amazon":
                filter_keyword = filter_string(self.keyword, "+")
                base_url = "https://www.amazon.com/s?k={0}&page={1}".format(filter_keyword, self.page)
                return base_url
            case default:
                return "we cannot support this"
            
    def add_product_to_csv(self, products):
        ts = get_timestamp()
        with open(
            './{0}/product_info_in_{1}_{2}.csv'.format("csv", self.location, ts), 
            "a", encoding="utf-8") as f:
            
            for item in products:
                f.write(item)       