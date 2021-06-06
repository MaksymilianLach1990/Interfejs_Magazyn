import time
timer = time.time()
users = {'admin': "0000"}
items = [{'name': 'Milk', 'quantity': 120, 'unit': 'l', 'unit price': 2.50},
         {'name': 'Egg', 'quantity': 1200, 'unit': 'piece', 'unit price': 0.50},
         {'name': 'Wood', 'quantity': 200, 'unit': 'mb', 'unit price': 5.00}]


def check_user(login):
    if login in users.keys():
        password = input("User password: ")
        if users[login] == password:
            return True
        else:
            print("Warning!! Wrong password!! Try again.")
            return False
    else:
        print("Warning!! Wrong user name!!")
        return False


def add_user(login):
    pass


def add_item():
    name = input("Item name: ")
    quantity = int(input("Item quantity: "))
    unit = input("Item unit of measure[piece, l, kg]: ")
    unit_price = float(input("Item price in PLN: "))
    items.append({'name': name, 'quantity': quantity, 'unit': unit, 'unit price': unit_price})


def stock_status():
    print("{:69}".format('-' * 69))
    print("|{:20}|{:>14}|{:>10}|{:>20}|".format("Name", "Quantity", "Unit", "Unit Price [PLN]"))
    print("|{:67}|".format('-' * 67))
    for i in range(0, len(items)):
        print("|{:20}|{:14.2f}|{:>10}|{:20.2f}|".format(items[i].get('name'), items[i].get('quantity'),
                                                        items[i].get('unit'), items[i].get('unit price')))
    print("{:69}".format('-' * 69))


def sell_item():
    name = input("Item name: ")
    quantity = int(input("Quantity to sell: "))
    for number in range(0, len(items)):
        if name == items[number].get('name'):
            items[number]['quantity'] = items[number]['quantity'] - quantity
        else:
            pass


def buy_item():
    pass


# Rozruch aplikacji
if __name__ == "__main__":
    print("Welcome to the 'Green World' warehouse.")
    # Logowanie do systemu
    while True:
        login = input("User name: ")
        #if check_user(login) is True:
         #   pass
        #else:
          #  exit(1)
        # Rozpoczęcie pracy w aplikacji
        print("\nHello {}, what would you like to do?\n".format(login))
        while True:
            # Menu aplikacji
            print("MENU: \nWarehouse status [status]\nAdd item [add]\nSell item [sell]")
            user = input()
            if user == 'status':
                stock_status()
            elif user == 'add':
                add_item()
                stock_status()
            elif user == 'sell':
                sell_item()
                stock_status()
            elif user == 'exit':
                exit()
            else:
                print("Wrong command.")
        # Zakończenie pracy programu
        print(time.time() - timer)
        exit("Miłego dnia. Zapraszamy ponownie. Poprawne Wyłączenie.")
