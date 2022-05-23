import os
import sys
import webbrowser as wb
from colorama import Fore

def quick_setup():
    intro = f"""{Fore.BLUE}AuRun v0.5{Fore.WHITE}"""
    os.system("clear")
    print(intro)
    wb.open("https://animego.org", new=2)
    wb.open("https://www.youtube.com", new=0)
    os.system("apt-get update")
    os.system("apt-get upgrade -y")
    sys.exit
