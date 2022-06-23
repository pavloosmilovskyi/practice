import sys
from collection import Collection
import validation
from Product import Product

def option_menu():
    print("1 - to see information\n"
          "2 - to add\n"
          "3 - to delete\n"
          "4 - to find\n"
          "5 - to replace using ID\n"
          "6 - to sort\n"
          "7 - to end work\n")

def main_menu():
    path = 'text.txt'
    data = Collection(path)
    data.read()
    option_menu()
    option = int(input())
    if option == 7:
        sys.exit()
    if option == 1:
        print(data)
    elif option == 2:
        data.add()
        print(data)
    elif option == 3:
        print("Input id:")
        id = validation.validate_numb()
        data.remove(id)
        print(data)
    elif option == 4:
        print("Input:")
        search_object = input()
        data.search(search_object)
    elif option == 5:
        data.replace()
    elif option == 6:
        print("Input parameter: \n"
              "(id, title, date_of_creation, updated_at, price)")
        field = validation.validate_jewer_item([str(item) for item in Product.__dict__], f"get_{input()}")
        data.sort(field)


    main_menu()