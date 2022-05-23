import os
from colorama import Fore

def AuRun():
    intro = f"""{Fore.BLUE}AuRun v0.5{Fore.WHITE}"""
    os.system("clear")
    print(intro)
    print(f"{Fore.CYAN}[1]-Ubuntu\n[2]-Браузер{Fore.RED}\n[3]-Новости\n[4]-Отправить сообщение\n[/]-Разное\n[!]-Помощник\n[@]-Графический интерфейс\n{Fore.CYAN}[*]-Быстрая настройка\n[0]-Выйти")
    AuRun_number = input(f"{Fore.WHITE}Выбери действие:")
    if AuRun_number == "1":
        from Plugins.Ubuntu import ubuntu
        ubuntu()
        return AuRun()
    elif AuRun_number == "2":
        from Plugins.Browser import browser
        browser()
        return AuRun()
    # elif AuRun_number == "3":
    #     terminal()
    # elif AuRun_number == "4":
    #     terminal()    
    # elif AuRun_number == "5":
    #     terminal()
    elif AuRun_number == "*":
        from Plugins.Quick_setup import quick_setup
        quick_setup()
        return AuRun()    
    elif AuRun_number == "0":
        exit(0)
    else:
        return AuRun()

AuRun()
