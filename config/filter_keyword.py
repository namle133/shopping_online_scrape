def filter_string(str_name: str, c: str) -> str:
    print_space = False
    print_str=""
    for i in range(len(str_name)):
        if 'a' <= str_name[i] <= 'z' or 'A'  <= str_name[i] <= 'Z':
            if str_name[i - 1]  == " " and print_space and i>0:
                print_str += c

            print_str += str_name[i]
            print_space = True
    return print_str