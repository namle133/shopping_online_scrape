def input_initial_value() -> (str, str, str):
    location = input("Location: ")
    keyword = input("Keyword: ")
    page = input("Page: ")
    return location, keyword, page

def add_to_cart() -> bool:
    is_choose = input("Do you want to add product to cart? Please type (Y or N): ")
    while True:
        if is_choose == 'Y':
            return True
        elif is_choose == 'N':
            return False
        else:
            is_choose = input("Error type. Please type again: ")
        