import youtube_dl
from tkinter import *

def youTube():

    def btn_hello_handler():
        textBox.pack(padx=5, pady=40)
        btn_hello.pack_forget()
        btn_download.pack()

    def btn_download_handler():
        YouTubeUrl = retrieve_input().strip()
        ydl_opts = {}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([YouTubeUrl])

    def retrieve_input():
        return textBox.get('1.0', 'end-1c')

    root = Tk()
    root.title("YT downloader")
    root.geometry("400x250")


# Кнопка приветствия
    btn_hello = Button(
        root,
        text="Скачать видео с YouTube",
        background="#555",
        foreground="#ccc",
        padx="20",
        pady="8",
        font="16",
        command = btn_hello_handler
        )

# Поле ввода
    textBox = Text(
        root, 
        height=2, 
        width=40)

# Кнопка скачивания
    btn_download = Button( 
        root,
        text="Скачать",
        background="#555",
        foreground="#ccc",
        padx="20",
        pady="8",
        font="16",
        command = btn_download_handler
        )

    btn_hello.pack()


    root.mainloop()


