import pyautogui as pg
import os
import sys

from tkinter import *


def terminal():

    def Exit():
        sys.exit()

    def Pass():
        sudo_password = input("Введи пароль: ")
        command = 'sudo -S ls'.split()
        p = Popen(command, stdin=PIPE, stderr=PIPE, shell=True, universal_newlines=True)
        p.communicate(sudo_password + '\n')
       
        

    root = Tk()
    root.title("Терминал")
    root.geometry("400x500")

    btn_Pass = Button(
        root,
        text="Обновить",         
        background="#00041f", 
        foreground="#ffffff",
        padx="20",             
        pady="8",
        font="16",            
        command=Pass)
    btn_Pass.pack()

    btn_Exit = Button(
        root,
        text="Закрыть",         
        background="#00041f", 
        foreground="#ffffff",
        padx="20",             
        pady="8",
        font="16",            
        command=Exit)
    btn_Exit.pack()






