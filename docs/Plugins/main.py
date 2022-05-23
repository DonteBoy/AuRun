import os
import sys
from Browser import browser
from Terminal import terminal
from Entertainment import entertainment
# from Chat import chat
from Sms import sms

def AuRun():
    intro = """AuRun"""
    i = 1
    def AuRun_start():
        while i == i:
            os.system("clear")
            print(intro)
            print("""1-Браузер \n2-Терминал\n3-Развлечение\n4-Чат\n5-Отправить sms\n6-Выйти""")
            AuRun_number = input("Выбери номер:")
            if AuRun_number == "1":
                browser()
            elif AuRun_number == "2":
                terminal()
            elif AuRun_number == "3":
                entertainment()
            elif AuRun_number == "4":
                # chat()
                print("gg")
            elif AuRun_number == "5":
                sms()
            elif AuRun_number == "6":
                os.system("clear")
                sys.exit
            else:
                print("Введен неверный номер!")
       
    AuRun_start()

AuRun()

