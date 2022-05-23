import os
import sys

def entertainment():
    os.system("clear")
    print("Развлечение")
    print("""1-CS-GO\n2-Назад""")
    browser_number = input("Выбери номер:")
    if browser_number == "1":
        os.system("steam csgo")
    elif browser_number == "4":
        os.system("clear")
        exit
    else:
        print("Введен неверный номер!")




