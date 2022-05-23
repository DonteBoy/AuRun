import sys
from tkinter import *
from Browser import browser
from Terminal import terminal
# from YouTube import youTube

def Exit():
    sys.exit()

def Browser():
    browser()
    
def Terminal():
    terminal()

# def YouTube():
#     youTube()

root = Tk()
root.title("AuRun")
root.geometry("400x500")

btn_Browser = Button(
    text="Браузер",         
    background="#ee800b",     
    foreground="#ffffff",    
    padx="20",             
    pady="8",
    font="16",            
    command = Browser)
btn_Browser.pack()

# btn_YouTube = Button(
#     text="YouTube",         
#     background="#ee800b",     
#     foreground="#ffffff",    
#     padx="20",             
#     pady="8",
#     font="16",            
#     command = YouTube)
# btn_YouTube.pack()

btn_Terminal = Button(
    text="Терминал",         
    background="#581845",     
    foreground="#ffffff",    
    padx="20",             
    pady="8",
    font="16",            
    command = Terminal)
btn_Terminal.pack()

btn_Exit = Button(
    text="Закрыть",         
    background="#00041f", 
    foreground="#ffffff",
    padx="20",             
    pady="8",
    font="16",            
    command=Exit)
btn_Exit.pack()

root.mainloop()





    # activebackground: цвет кнопки, когда она находится в нажатом состоянии

    # activeforeground: цвет текста кнопки, когда она в нажатом состоянии

    # bd: толщина границы (по умолчанию 2)

    # bg/background: фоновый цвет кнопки

    # fg/foreground: цвет текста кнопки

    # font: шрифт текста, например, font="Arial 14" - шрифт Arial высотой 14px, или font=("Verdana", 13, "bold") - шрифт Verdana высотой 13px с выделением жирным

    # height: высота кнопки

    # highlightcolor: цвет кнопки, когда она в фокусе

    # image: изображение на кнопке

    # justify: устанавливает выравнивание текста. Значение LEFT выравнивает текст по левому краю, CENTER - по центру, RIGHT - по правому краю

    # padx: отступ от границ кнопки до ее текста справа и слева

    # pady: отступ от границ кнопки до ее текста сверху и снизу

    # relief: определяет тип границы, может принимать значения SUNKEN, RAISED, GROOVE, RIDGE

    # state: устанавливает состояние кнопки, может принимать значения DISABLED, ACTIVE, NORMAL (по умолчанию)

    # text: устанавливает текст кнопки

    # textvariable: устанавливает привязку к элементу StringVar

    # underline: указывает на номер символа в тексте кнопки, который подчеркивается. По умолчанию значение -1, то есть никакой символ не подчеркивается

    # width: ширина кнопки

    # wraplength: при положительном значении строки текста будут переносится для вмещения в пространство кнопки
