import time
import csv
import sys
timer = time.time()
users = {'admin': "0000"}
items = [{'name': 'Milk', 'quantity': 120, 'unit': 'l', 'unit price': 2.50},
         {'name': 'Egg', 'quantity': 1200, 'unit': 'piece', 'unit price': 0.50},
         {'name': 'Wood', 'quantity': 200, 'unit': 'mb', 'unit price': 5.00}]
sold_items = []


def check_user(name):
    if name in users.keys():
        password = input("User password: ")
        if users[name] == password:
            return True
        else:
            print("Warning!! Wrong password!! Try again.")
            return False
    else:
        print("Warning!! Wrong user name!!")
        return False


def add_user():
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
            sold_items.append({'name': items[number]['name'], 'quantity': quantity, 'unit': items[number]['unit'],
                               'unit price': items[number]['unit price']})
        else:
            print("No item in stock. Try again.")


def get_costs():
    costs = sum([items[number]['quantity'] * items[number]['unit price'] for number in range(0, len(items))])
    return costs


def get_income():
    if len(sold_items) == 0:
        return 0
    else:
        income = sum([sold_items[number]['quantity'] * sold_items[number]['unit price']
                      for number in range(0, len(sold_items))])
        return income


def show_revenue():
    print("{:69}".format('.' * 69))
    print("Revenue breakdown (PLN)")
    print("Income: {}".format(get_income()))
    print("Costs: {}".format(get_costs()))
    print("{:69}".format('_' * 69))
    print("Revenue: {}".format(round(get_income()-get_costs()), 2))
    print('')


def export_items_to_csv():
    with open('Green_house.csv', 'w', newline='') as csvfile:
        fieldname = ['name', 'quantity', 'unit', 'unit price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldname)
        writer.writeheader()
        for num_item in range(0, len(items)):
            writer.writerow({'name': items[num_item]['name'], 'quantity': items[num_item]['quantity'],
                             'unit': items[num_item]['unit'], 'unit price': items[num_item]['unit price']})
    print("Successfully exported data to 'Green_house.csv'.")


def load_items_from_csv(source):
    items.clear()
    with open(source, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            items.append(row)
        for num_item in range(0, len(items)):
            items[num_item]['quantity'] = int(items[num_item]['quantity'])
            items[num_item]['unit price'] = float(items[num_item]['unit price'])
    print("Successfully import data to 'Green_house.csv'.")


# Rozruch aplikacji
if __name__ == "__main__":
    if len(sys.argv) > 1:
        path = sys.argv[1]
        load_items_from_csv(path)
    print("Welcome to the 'Green World' warehouse.")
    # Logowanie do systemu
    while True:
        login = input("User name: ")
        #if check_user(login) is True:
         #   pass
        #else:
          #  exit(1)
        # Rozpoczęcie pracy w aplikacji
        print("\nHello {}.\n".format(login))
        while True:
            # Menu aplikacji
            print("\nMENU: \nWarehouse status [status]\nAdd item [add]\nSell item [sell]\nShow revenue [revenue]\n"
                  "Save your inventory [save]\nLoad up-to-data data [load]\nEnd of work [exit]")
            user = input("What would you like to do? ")
            if user == 'status':
                stock_status()
            elif user == 'add':
                add_item()
                stock_status()
            elif user == 'sell':
                sell_item()
                stock_status()
            elif user == 'revenue':
                show_revenue()
            elif user == 'save':
                export_items_to_csv()
            elif user == 'load':
                path = input("Please enter path(standard file 'Green_house.csv'): ")
                if path == '':
                    path = 'Green_house.csv'
                load_items_from_csv(path)
            elif user == 'exit':
                exit()
            else:
                print("Wrong command.")
        # Zakończenie pracy programu
        print(time.time() - timer)
        exit("Have a nice day. Please come back.")
