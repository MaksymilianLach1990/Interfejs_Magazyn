import time
timer = time.time()

# Rozruch aplikacji
users = {'admin': "0000"}
if __name__ == "__main__":
    print("Witamy w magazynie 'Green World'.")
    while True:
        # Logowanie do systemu
        login = input("Podaj nazwę użytkownika: ")
        if login in users.keys():
            pass
        else:
            print("Warning!! Zła nazwa urzytkownika!!")
            exit(1)
        password = input("Podaj hasło urzytkownika: ")
        if users[login] == password:
            pass
        else:
            print("Warning!! Błedne hasło!! Spróbuj ponownie.")
            exit(1)
        users[login] = password
        # Rozpoczęcie pracy w aplikacji
        print("Witaj {}, jaką akcję chciałbyś wykonać?".format(login))
        user = input()
        # Menu aplikacji
        # Zakończenie pracy programu
        print(time.time() - timer)
        exit("Miłego dnia. Zapraszamy ponownie. Poprawne Wyłączenie.")
