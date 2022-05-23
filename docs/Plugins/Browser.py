import os
import sys
import webbrowser
from colorama import Fore

def browser():
    intro = f"""{Fore.BLUE}AuRun v0.5{Fore.WHITE}"""
    os.system("clear")
    print(intro)
    print(f"{Fore.CYAN}1-Начать \n2-Учеба\n3-Развлечение\n0-Назад")
    browser_number = input(f"{Fore.WHITE}Выбери номер:")
    if browser_number == "1":
        webbrowser.open("https://animego.org", new=2)
        webbrowser.open("https://www.youtube.com", new=0)
        webbrowser.open("https://lolz.guru/", new=0)
        webbrowser.open("https://www.behance.net/", new=0) 
    elif browser_number == "2":
        webbrowser.open("https://learn.javascript.ru/", new=2)
        webbrowser.open("https://live.skillbox.ru/calendar/", new=0)
    elif browser_number == "3":
        webbrowser.open("https://www.youtube.com/", new=2)
        webbrowser.open("https://animego.org", new=0)
    elif browser_number == "0":
        sys.exit
    else:
        return browser()
