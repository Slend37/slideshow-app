from tkinter import *
import tkinter as tk
from pygame import mixer
import keyboard
import glob
import PIL
import os

mixer.init()

musics=[]
cmus=0
for music in glob.glob('*.mp3'):
    musics.append(music)
    print(musics)
    cmus+=1
    print(cmus)
count = 0
files = []
years = []
for a in range(2009,2023):
    for file in glob.glob(str(a)+'\*.png'):
        files.append(file)
        years.append(a)
        print(files)
        count+=1
        print(count)

win = tk.Tk()
win.config(bg="black")
win.title('Slideshow App')
win.geometry('1366x768')
win.minsize(1366,700)
win.maxsize(1366,768)
win.resizable(0, 1)
photka=-1
def fulls():
    def unfulls():
        win.attributes('-fullscreen',False)
        keyboard.remove_hotkey("esc")
        keyboard.add_hotkey("esc",lambda:[fulls()])
    win.attributes('-fullscreen',True)
    keyboard.remove_hotkey("esc")
    keyboard.add_hotkey("esc",lambda:[unfulls()])

keyboard.add_hotkey("esc",lambda:[fulls()])
var1 = Entry()
var1.pack(anchor=CENTER,padx=8,pady=8)


musiccode = -1
def starting():
    if mixer.music.get_busy()==True:
        pass
    else:
        global musiccode
        musiccode+=1
        mixer.music.load(str(musics[musiccode]))
        mixer.music.play()
        mixer.music.set_volume(0.2)
    def fulls():
        def unfulls():
            win.attributes('-fullscreen', False)
            keyboard.remove_hotkey("esc")
            keyboard.add_hotkey("esc", lambda: [fulls()])

        win.attributes('-fullscreen', True)
        keyboard.remove_hotkey("esc")
        keyboard.add_hotkey("esc", lambda: [unfulls()])
    try:
        var1.pack_forget()
    except:
        pass
    global photka
    photka += 1
    def maincode():
        """Вывод картинки"""
        global photka
        global input_img
        global img
        global panel
        print(files[photka])
        if PhotoImage(file=files[photka]).width() > 1366:
            if PhotoImage(file=files[photka]).height() > 720:
                input_img = Image.open(files[photka])
                input_img = input_img.resize((1366, int(PhotoImage(file=files[photka]).height() * (PhotoImage(file=files[photka]).width() / 1366))),Image.ANTIALIAS)
                input_img.save(files[photka][0:files[photka].find(".png")] + "_red.png", "png")
                img = PhotoImage(file=files[photka][0:files[photka].find(".png")] + "_red.png")
                os.remove(str(files[photka]))
                if PhotoImage(file=files[photka][0:files[photka].find(".png")] + "_red.png").height()>720:
                    input_img = Image.open(files[photka][0:files[photka].find(".png")] + "_red.png")
                    input_img = input_img.resize((int(1366/(PhotoImage(file=files[photka][0:files[photka].find(".png")] + "_red.png").height()/720)),720),Image.ANTIALIAS)
                    input_img.save(files[photka][0:files[photka].find(".png")]+"_red_red.png", "png")
                    img = PhotoImage(file=files[photka][0:files[photka].find(".png")]+"_red_red.png")
                    os.remove(files[photka][0:files[photka].find(".png")] + "_red.png")
                else:
                    pass
            else:
                input_img = Image.open(files[photka])
                input_img = input_img.resize((1366, int(PhotoImage(file=files[photka]).height() * (PhotoImage(file=files[photka]).width() / 1366))),Image.ANTIALIAS)
                input_img.save(files[photka][0:files[photka].find(".png")] + "_red.png")
                img = PhotoImage(file=files[photka][0:files[photka].find(".png")] + "_red.png")
                os.remove(str(files[photka]))
        elif PhotoImage(file=files[photka]).height() > 720:
            input_img = Image.open(files[photka])
            input_img = input_img.resize((int(PhotoImage(file=files[photka]).width() * (PhotoImage(file=files[photka]).height() / 720)), 720),Image.ANTIALIAS)
            input_img.save(files[photka][0:files[photka].find(".png")] + "_red.png")
            img = PhotoImage(file=files[photka][0:files[photka].find(".png")] + "_red.png")
            os.remove(str(files[photka]))
        else:
            img = PhotoImage(file=str(files[photka]))
        panel = Label(win, bg="black", image=img)
        panel.image = img
        panel.pack(expand=1)
        global year
        try:
            year.pack_forget()
        except:
            pass
        year = Label(win,bg="black",fg="white",text=years[photka],font="Consolas 30")
        year.place(x=10,y=10)

    def back():
        keyboard.remove_hotkey("enter")
        keyboard.remove_hotkey("space")
        keyboard.remove_hotkey("backspace")
        keyboard.add_hotkey("backspace", lambda: [back()])
        keyboard.add_hotkey("enter", lambda: [skip()])
        keyboard.add_hotkey("space", lambda: [starting()])
        win.after_cancel(move)
        try:
            win.after_cancel(move)
        except:
            pass
        global panel
        panel.pack_forget()
        global photka
        photka -= 1
        maincode()
        start.pack_forget()

    def pause():
        win.after_cancel(move)
        keyboard.remove_hotkey("enter")
        keyboard.remove_hotkey("space")
        keyboard.remove_hotkey("backspace")
        keyboard.add_hotkey("backspace", lambda: [back()])
        keyboard.add_hotkey("enter", lambda: [skip()])
        keyboard.add_hotkey("space", lambda: [starting()])

    def skip():
        keyboard.remove_hotkey("enter")
        keyboard.remove_hotkey("space")
        keyboard.remove_hotkey("backspace")
        keyboard.add_hotkey("backspace", lambda: [back()])
        keyboard.add_hotkey("enter", lambda: [skip()])
        keyboard.add_hotkey("space", lambda: [starting()])
        try:
            win.after_cancel(move)
        except:
            pass
        global panel
        panel.pack_forget()
        global photka
        photka+=1
        maincode()
        start.pack_forget()

    global panel
    if photka>=count:
        try:
            panel.pack_forget()
            year.pack_forget()
        except:
            pass
        Label(win,text="Конец!",bg="black",fg="white",font="Consolas 50").pack(expand="yes")
        year = Label(win, bg="black", text= '     ', font="Consolas 50")
        year.place(x=10, y=10)
    else:
        try:
            keyboard.remove_hotkey("enter")
        except:
            pass
        try:
            keyboard.remove_hotkey("backspace")
        except:
            pass
        keyboard.add_hotkey("backspace", lambda: [back()])
        keyboard.add_hotkey("enter", lambda: [skip()])
        keyboard.remove_hotkey("space")
        keyboard.add_hotkey("space", lambda: [pause()])
        panel.pack_forget()
        maincode()
        start.pack_forget()

        move = win.after(int(var1.get())*1000,lambda:[starting()])
panel=Label(win, text='0')
pausebut=Label(win, text='0')
year=Label(win,text='0')
keyboard.add_hotkey("space", lambda:[starting()])
start = Button(win,text="Start",font="Comfortoo 40",bg="yellow",
               command=lambda: [starting()])
start.pack(side="bottom")

win.mainloop()