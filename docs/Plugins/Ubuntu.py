import os
import sys
from colorama import Fore

def ubuntu():
    intro = f"""{Fore.BLUE}AuRun v0.5{Fore.WHITE}"""
    os.system("clear")
    print(intro)
    print(f"{Fore.CYAN}1-Обновить\n0-Назад")
    AuRun_number = input(f"{Fore.WHITE}Выбери номер:")
    if AuRun_number == "1":
        os.system("apt-get update")
        os.system("apt-get upgrade -y")
        # elif AuRun_number == "2":
        #     terminal()
    elif AuRun_number == "0":
        sys.exit
    else:
        return ubuntu()



        