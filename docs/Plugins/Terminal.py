import os
import sys

def terminal():
    os.system("clear")
    print("Терминал")
    print("""1-Обновить\n2-Назад""")
    browser_number = input("Выбери номер:")
    if browser_number == "1":
        os.system("sudo apt-get update")
        os.system("sudo apt-get upgrade -y")
    elif browser_number == "2":
        os.system("clear")
        sys.exit
    else:
        print("Введен неверный номер!")
