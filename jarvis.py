from time import sleep,time
from pywhatkit import check_window,help,prnt_sleeptm
from pywhatkit.mainfunctions import sendMail
import tkinter
from tkinter import *
from tkinter import filedialog
import tkinter.ttk
import numpy as np
import wikipedia
import webbrowser as web
import pythoncom
import win32api
import datetime
from datetime import date
import cv2
import json
import requests
import subprocess
import pyautogui as py
import pyttsx3
import pyperclip
import speech_recognition as sr
import pywhatkit
from os import walk
import os
import random
import ctypes


api='f8b5d3d8307c47c29dfe5c7489a46843'
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.setProperty('rate',150)
    engine.say(audio)
    engine.runAndWait()

def update():
    hr=int(datetime.datetime.now().hour)
    if hr>=3 and hr<=12:
        speak("Good Morning Sir")
    elif hr>12 and hr<=16:
        speak("Good Afternoon Sir")
    elif hr>16 and hr<=22:
        speak("Good Evening Sir")
    else:
        speak("Good Night Sir")
    # speak("I am stacy, your virtual assistant. How may i help you sir")

def voiceinput():
    global j
    mic=sr.Recognizer()
    with sr.Microphone(device_index=1) as sound:
        print("Listening...")
        mic.pause_threshold=1
        mic.energy_threshold=450
        voice=mic.listen(sound)

    try:
        print("Processing...")
        query=mic.recognize_google(voice,language='en-in')
        print(f"Requirement {query}")
        j=0
    except:
        j+=1
        speak("Oops, sorry can you repeat")
        return 'None'
    return query

def hell():
    a.destroy()
    global pic
    pic=1

def hell2():
    a.destroy()
    global lock
    lock=1

def func():
    global s
    s=t.get(1.0,END)
    win.destroy()

def func2():
    t.delete(1.0,END)

def openfile():
    x=filedialog.askopenfilename(initialdir=r"C:/",title='Open file',filetypes=(("Text Files","*.txt"), ))
    x=open(x,'r')
    text=x.read()
    t.insert(END,text)
    x.close()

def nap():
    mic=sr.Recognizer()
    with sr.Microphone(device_index=1) as sound:
        mic.pause_threshold=1
        mic.energy_threshold=450
        voice=mic.listen(sound)

    try:
        query=mic.recognize_google(voice,language='en-in')
        query=query.lower()
        if 'stacy' in query or "hey" in text or 'stacey' in text:
            speak("yes sir")
            return
    except:
        nap()

if __name__=="__main__":
    update()
    with open("config.json","r") as f:
        param=json.load(f)["mail"]
    global j
    j=0
    while True:
        text=voiceinput().lower()
        if 'search' in text and 'wikipedia' in text:
            speak('Topic please')
            text=voiceinput()
            find=wikipedia.summary(text,sentences=2)
            speak('find')

        elif 'open youtube' in text:
            web.open("www.youtube.com")

        elif 'opne google' in text:
            web.open('www.google.com')

        elif 'my site'in text:
            web.open("https://bhumicraftzilla1.pythonanywhere.com/")

        elif 'mood' in text and 'your' in text or 'smile' in text:
            speak("i am happy sir")
            root = Tk()
            root.wm_geometry('190x200')
            l=Label(root,text="\U0001f603",font="AdobeFanHeitiStdB 100 bold").place(x=0,y=0)
            root.mainloop()

        elif 'hai' in text or 'hye' in text or 'hi' in text or 'hello' in text:
            speak("Hi sir!")

        elif 'who are you' in text or "Tell me about yourself" in text:
            speak("I am stacy")

        elif 'how are you' in text:
            speak("Excellant , How do you do")

        elif '''today's news''' in text or 'newspaper' in text or 'news' in text:
            i='f8b5d3d8307c47c29dfe5c7489a46843'
            url="http://newsapi.org/v2/top-headlines?country=in&apiKey="+i
            r=requests.get(url)
            f=r.text
            p=json.loads(f)
            t=p["articles"]
            pic=0
            lock=0
            for i in t:
                speak(i["title"])
                a = Tk()
                a.wm_geometry('400x150')
                a.after(5000,a.destroy)
                a.config(bg="black")
                l=Label(a,text="If you want \nDetails news of \nthis headline",font="AdobeFanHeitiStdB 11 bold",fg="white",bg="black").place(x=25,y=5)
                l2=Label(a,text="Click Here",font="AdobeFanHeitiStdB 8",fg="white",bg="black").place(x=65,y=75)
                ak=Button(a,text="Detail",width=8,font='arial 12 bold',command=hell).place(x=45,y=100)
                tkinter.ttk.Separator(a, orient=VERTICAL).pack(fill=Y,expand=Y)
                l=Label(a,text="If you want \nto stop reading",font="AdobeFanHeitiStdB 11 bold",fg="white",bg="black").place(x=230,y=5)
                l2=Label(a,text="Click Here",font="AdobeFanHeitiStdB 8",fg="white",bg="black").place(x=268,y=75)
                ak=Button(a,text="Stop",width=8,font='arial 12 bold',command=hell2).place(x=245,y=100)
                a.mainloop()
                if pic==1:
                    speak(i['description'])
                    pic=0
                if lock==1:
                    lock=0
                    break
                speak('Next Headline')
            speak("thanks for listening")

        elif ('find' in text) and 'youtube' in text:
            speak("topic please")
            text=voiceinput()
            web.open("www.youtube.com/results?search_query="+text)

        elif ('search' in text and "google" in text) :
            inp=voiceinput()
            pywhatkit.search(inp)

        elif ('play' in text) and (('song' in text) or ("video" in text )or ("movie" in text)) and ('online' in text):
            speak("name of movie please")
            text=voiceinput()
            web.open("www.youtube.com/results?search_query="+text)

        elif 'play' in text and 'song' in text:
            g=r'C:\Users\ASUS\Downloads'
            for (path,dir,file) in walk(g):
                if (file!=""):
                    l=list(filter(lambda x:x.endswith('.mp3'),file))
                    if l!=[]:
                        os.startfile(path+"\\"+str(random.choice(list(l))))
                        break
                    else:
                        continue

        elif ('play' in text) and ('video' in text or 'movie' in text):
            g=r'C:\Users\ASUS\Downloads'
            for (path,dir,file) in walk(g):
                if (file!=""):
                    l=list(filter(lambda x:x.endswith('.mp4'),file))
                    if l!=[]:
                        os.startfile(path+"\\"+str(random.choice(list(l))))
                        break
                    else:
                        continue

        elif 'send' in text and 'message' in text:
            speak('over which platform sir!')
            text=voiceinput().lower()
            if 'email' in text or 'gmail' in text:
                speak('Would you like to write or speak your message sir?')
                text=voiceinput()
                if 'write' in text or 'type' in text or 'right' in text:
                    win=Tk()
                    win.geometry("600x400")
                    mainmenu=Menu(win,tearoff=0)

                    file=Menu(mainmenu,tearoff=0)
                    file.add_command(label='open',command=openfile)

                    win.config(menu=mainmenu)
                    mainmenu.add_cascade(label='File',menu=file)

                    t = Text(win, height=16, width=55)
                    t.pack(pady=2)
                    b1= Button(win,text="Submit",bg="black",fg="white",border=0,font="AdobeFanHeitiStdB 14 bold",borderwidth=2,relief=SUNKEN,command=func)
                    b1.place(x=180,y=340,width=100,height=35)
                    b2= Button(win,text="Clear",bg="black",fg="white",font="AdobeFanHeitiStdB 15 bold",borderwidth=2,relief=SUNKEN,command=func2)
                    b2.place(x=340,y=340,width=75,height=35)
                    win.mainloop()
                else:
                    speak("please speak your message")
                    s=voiceinput()
                speak('where to send it sir')
                for _ in range(3):
                    text=voiceinput().lower()
                    try:
                        if 'tanmay' in text:
                            sendMail(my_mail=param['user'],my_pass=param['pass'],mail_to=param['tanmay'],content=s)
                            speak('your Mail is sent Sir')
                            break
                        elif 'deepanshi' in text:
                            sendMail(my_mail=param['user'],my_pass=param['pass'],mail_to=param['deepanshi'],content=s)
                            speak('your Mail is sent Sir')
                            break
                        else:
                            print("error")
                            raise web.Error

                    except Exception as e:
                        if _!=2:
                            speak("Please say it again sir")
                        else:
                            speak('sorry try again')
            elif 'whatsapp' in text:
                speak('Would you like to write or speak your message sir?')
                text=voiceinput()
                if 'write' in text or 'type' in text:
                    win=Tk()
                    win.geometry("600x400")
                    mainmenu=Menu(win,tearoff=0)

                    file=Menu(mainmenu,tearoff=0)
                    file.add_command(label='open',command=openfile)

                    win.config(menu=mainmenu)
                    mainmenu.add_cascade(label='File',menu=file)

                    t = Text(win, height=16, width=55)
                    t.pack(pady=2)
                    b1= Button(win,text="Submit",bg="black",fg="white",border=0,font="AdobeFanHeitiStdB 14 bold",borderwidth=2,relief=SUNKEN,command=func)
                    b1.place(x=180,y=340,width=100,height=35)
                    b2= Button(win,text="Clear",bg="black",fg="white",font="AdobeFanHeitiStdB 15 bold",borderwidth=2,relief=SUNKEN,command=func2)
                    b2.place(x=340,y=340,width=75,height=35)
                    win.mainloop()
                else:
                    speak("please speak your message")
                    s=voiceinput()
                speak('where to send it sir')
                for _ in range(3):
                    text=voiceinput().lower()
                    try:
                        if 'tanmay' in text:
                            try:
                                speak('your message will be delivered within a minute sir')
                                pywhatkit.sendwhatmsg(param['tanmayw'],s,int(str(datetime.datetime.now()).split()[1].split(':')[0])
                                ,int(str(datetime.datetime.now()).split()[1].split(':')[1])+int(1),wait_time=5)
                            except:
                                speak('your message will be delivered within a minute sir')
                                pywhatkit.sendwhatmsg(param['tanmayw'],s,int(str(datetime.datetime.now()).split()[1].split(':')[0])
                                ,int(str(datetime.datetime.now()).split()[1].split(':')[1])+int(2),wait_time=5)
                            break
                        elif 'deepanshi' in text:
                            try:
                                speak('your message will be delivered within a minute sir')
                                pywhatkit.sendwhatmsg(param['deep'],s,int(str(datetime.datetime.now()).split()[1].split(':')[0])
                                ,int(str(datetime.datetime.now()).split()[1].split(':')[1])+int(1),wait_time=5)
                            except Exception as e:
                                speak('your message will be delivered within a minute sir')
                                pywhatkit.sendwhatmsg(param['deep'],s,int(datetime.datetime.now().hour)
                                ,int(datetime.datetime.now().minute)+int(2),wait_time=5)
                            break
                        elif 'mummy' in text:
                            try:
                                speak('your message will be delivered within a minute sir')
                                pywhatkit.sendwhatmsg(param['mummy'],s,int(str(datetime.datetime.now()).split()[1].split(':')[0])
                                ,int(str(datetime.datetime.now()).split()[1].split(':')[1])+int(1),wait_time=5)
                            except Exception as e:
                                speak('your message will be delivered within a minute sir')
                                pywhatkit.sendwhatmsg(param['mummy'],s,int(datetime.datetime.now().hour)
                                ,int(datetime.datetime.now().minute)+int(2),wait_time=5)
                            break
                        elif 'bhai' in text:
                            try:
                                speak('your message will be delivered within a minute sir')
                                pywhatkit.sendwhatmsg(param['bhai'],s,int(str(datetime.datetime.now()).split()[1].split(':')[0])
                                ,int(str(datetime.datetime.now()).split()[1].split(':')[1])+int(1),wait_time=5)
                            except Exception as e:
                                speak('your message will be delivered within a minute sir')
                                pywhatkit.sendwhatmsg(param['bhai'],s,int(datetime.datetime.now().hour)
                                ,int(datetime.datetime.now().minute)+int(2),wait_time=5)
                            break
                        elif 'dad' in text:
                            try:
                                speak('your message will be delivered within a minute sir')
                                pywhatkit.sendwhatmsg(param['dad'],s,int(str(datetime.datetime.now()).split()[1].split(':')[0])
                                ,int(str(datetime.datetime.now()).split()[1].split(':')[1])+int(1),wait_time=5)
                            except Exception as e:
                                speak('your message will be delivered within a minute sir')
                                pywhatkit.sendwhatmsg(param['dad'],s,int(datetime.datetime.now().hour)
                                ,int(datetime.datetime.now().minute)+int(2),wait_time=5)
                            break
                        elif 'jack' in text:
                            try:
                                speak('your message will be delivered within a minute sir')
                                pywhatkit.sendwhatmsg(param['jack'],s,int(str(datetime.datetime.now()).split()[1].split(':')[0])
                                ,int(str(datetime.datetime.now()).split()[1].split(':')[1])+int(1),wait_time=5)
                            except Exception as e:
                                speak('your message will be delivered within a minute sir')
                                pywhatkit.sendwhatmsg(param['jack'],s,int(datetime.datetime.now().hour)
                                ,int(datetime.datetime.now().minute)+int(2),wait_time=5)
                            break
                        elif "college" in text and "group" in text:
                            try:
                                speak('your message will be delivered within a minute sir')
                                pywhatkit.sendwhatmsg_to_group(param['college'],s,int(str(datetime.datetime.now()).split()[1].split(':')[0])
                                ,int(str(datetime.datetime.now()).split()[1].split(':')[1])+int(1),wait_time=5)
                            except Exception as e:
                                speak('your message will be delivered within a minute sir')
                                pywhatkit.sendwhatmsg_to_group(param['college'],s,int(str(datetime.datetime.now()).split()[1].split(':')[0])
                                ,int(str(datetime.datetime.now()).split()[1].split(':')[1])+int(1),wait_time=5)
                            break
                        elif "school" in text and "group" in text:
                            try:
                                speak('your message will be delivered within a minute sir')
                                pywhatkit.sendwhatmsg_to_group(param['school'],s,int(str(datetime.datetime.now()).split()[1].split(':')[0])
                                ,int(str(datetime.datetime.now()).split()[1].split(':')[1])+int(1),wait_time=5)
                            except Exception as e:
                                speak('your message will be delivered within a minute sir')
                                pywhatkit.sendwhatmsg_to_group(param['school'],s,int(str(datetime.datetime.now()).split()[1].split(':')[0])
                                ,int(str(datetime.datetime.now()).split()[1].split(':')[1])+int(1),wait_time=5)
                            break
                        elif "mam" in text:
                            try:
                                speak('your message will be delivered within a minute sir')
                                pywhatkit.sendwhatmsg(param['mam'],s,int(str(datetime.datetime.now()).split()[1].split(':')[0])
                                ,int(str(datetime.datetime.now()).split()[1].split(':')[1])+int(1),wait_time=5)
                            except Exception as e:
                                speak('your message will be delivered within a minute sir')
                                pywhatkit.sendwhatmsg(param['mam'],s,int(str(datetime.datetime.now()).split()[1].split(':')[0])
                                ,int(str(datetime.datetime.now()).split()[1].split(':')[1])+int(1),wait_time=5)
                            break
                        else:
                            raise KeyError
                    except Exception as e:
                        if _!=2:
                            speak("Please say it again sir")
                        else:
                            speak('sorry try again')

        elif 'send' in text and 'mail' in text or 'email' in text or 'gmail' in text:
                speak('Would you like to write or speak your message sir?')
                text=voiceinput()
                if 'write' in text or 'type' in text or 'right' in text:
                    win=Tk()
                    win.geometry("600x400")
                    mainmenu=Menu(win,tearoff=0)

                    file=Menu(mainmenu,tearoff=0)
                    file.add_command(label='open',command=openfile)

                    win.config(menu=mainmenu)
                    mainmenu.add_cascade(label='File',menu=file)

                    t = Text(win, height=16, width=55)
                    t.pack(pady=2)
                    b1= Button(win,text="Submit",bg="black",fg="white",border=0,font="AdobeFanHeitiStdB 14 bold",borderwidth=2,relief=SUNKEN,command=func)
                    b1.place(x=180,y=340,width=100,height=35)
                    b2= Button(win,text="Clear",bg="black",fg="white",font="AdobeFanHeitiStdB 15 bold",borderwidth=2,relief=SUNKEN,command=func2)
                    b2.place(x=340,y=340,width=75,height=35)
                    win.mainloop()
                else:
                    speak("please speak your message")
                    s=voiceinput()
                speak('where to send it sir')
                for _ in range(3):
                    text=voiceinput().lower()
                    try:
                        if 'tanmay' in text:
                            sendMail(my_mail=param['user'],my_pass=param['pass'],mail_to=param['tanmay'],content=s)
                            speak('your Mail is sent Sir')
                            break
                        elif 'deepanshi' in text:
                            sendMail(my_mail=param['user'],my_pass=param['pass'],mail_to=param['deepanshi'],content=s)
                            speak('your Mail is sent Sir')
                            break
                        else:
                            print("error")
                            raise web.Error

                    except Exception as e:
                        if _!=2:
                            speak("Please say it again sir")
                        else:
                            speak('sorry try again')
        
        elif "open" in text and "control panel" in text:
            py.click(0,1074,clicks=1)
            py.typewrite('control panel')
            py.typewrite(['enter'])

        elif "open" in text and ("wi-fi" in text or "settings" in text):
            py.click(0,1074,clicks=1)
            py.typewrite('wifi')
            py.typewrite(['enter'])

        elif "open" in text and "uninstall" in text and "window":
            py.click(0,1074,clicks=1)
            py.typewrite('control panel')
            py.typewrite(['enter'])
            sleep(0.4)
            py.click(x=605, y=490,clicks=1)

        elif "screenshot" in text:
            x=py.screenshot()
            x.save(r'C:/users/ASUS/Desktop/'+str(date.today())+str(datetime.datetime.now().hour)+'.jpg')
            x=cv2.imread(r'C:/users/ASUS/Desktop/'+str(date.today())+str(datetime.datetime.now().hour)+'.jpg')
            cv2.imshow("screenshot",x)
            cv2.waitKey(0)

        elif "wi-fi" in text and "password" in text:
            data = subprocess.check_output(['netsh', 'wlan', 'show',
                                'profiles']).decode('utf-8').split('\n')
            profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
            for i in profiles:
                password= subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i,
                                    'key=clear']).decode('utf-8').split('\n')
                password = [b.split(":")[1][1:-1] for b in password if "Key Content" in b]
                try:
                    print ("{:<30}| {:<}".format(i, password[0]))
                except IndexError:
                    print ("{:<30}| {:<}".format(i, ""))
        
        elif "notes" in text and "handwritten" in text:
            speak('Would you like to write or speak your message sir?')
            text=voiceinput()
            if 'write' in text or 'type' in text:
                win=Tk()
                win.geometry("600x400")
                mainmenu=Menu(win,tearoff=0)

                file=Menu(mainmenu,tearoff=0)
                file.add_command(label='open',command=openfile)

                win.config(menu=mainmenu)
                mainmenu.add_cascade(label='File',menu=file)

                t = Text(win, height=16, width=55)
                t.pack(pady=2)
                b1= Button(win,text="Submit",bg="black",fg="white",border=0,font="AdobeFanHeitiStdB 14 bold",borderwidth=2,relief=SUNKEN,command=func)
                b1.place(x=180,y=340,width=100,height=35)
                b2= Button(win,text="Clear",bg="black",fg="white",font="AdobeFanHeitiStdB 15 bold",borderwidth=2,relief=SUNKEN,command=func2)
                b2.place(x=340,y=340,width=75,height=35)
                win.mainloop()
            else:
                speak("please speak your message")
                s=voiceinput()
            pywhatkit.text_to_handwriting(s,rgb=[0,0,0])

        elif "notepad" in text:
            py.click(0,1074,clicks=1)
            py.typewrite('notepad')
            py.typewrite(['enter'])
            speak('say quit,over,exit or stop to stop writing')
            while True:
                text=voiceinput()
                if 'quit' in text or 'exit' in text or 'over' in text or 'stop' in text:
                    break
                pyperclip.copy(text+' ')
                py.hotkey('ctrl','v')

        elif "word" in text and 'open' in text:
            py.click(0,1074,clicks=1)
            py.typewrite('word')
            py.typewrite(['enter'])
            speak('say quit,over,exit or stop to stop writing')
            while True:
                text=voiceinput()
                if 'quit' in text or 'exit' in text or 'over' in text or 'stop' in text:
                    break
                pyperclip.copy(text+' ')
                py.hotkey('ctrl','v')

        elif ('thank you' in text or 'thanks' in text):
            speak('my pleasure')



        elif j>=3 and 'none' in text:
            nap()

        if ('turn' in text and 'off' in text or 'of' in text):
            speak('bye sir')
            exit()



# path = "C:\\Users\\ASUS\\Downloads\\Video\\Python Problem 4- Solution - Python Tutorials For Absolute Beginners In Hindi #110.mp4"
# path = os.path.realpath(path)
# os.startfile(path)



# pywhatkit.sendwhatmsg('+918287539949','''khana khara hoon zara.. jaldi aa jao 
#                         tum bhi''',int(str(datetime.datetime.now()).split()[1].split(':')[0])
#                         ,int(str(datetime.datetime.now()).split()[1].split(':')[1])+int(1),wait_time=5)
# s=input()
# pywhatkit.text_to_handwriting(s,rgb=[0,0,0])
# pywhatkit.watch_tutorial_in_Hindi()
# pywhatkit.image_to_ascii_art('code.jpg','hello.txt')


# from os import walk
# import os
# import time

# for (dirpath, dirnames, filenames) in walk('C:/'):
#     if 'bandicam 2021-01-01 02-02-16-939.mp4' in filenames:
#         os.startfile(dirpath+'bandicam 2021-01-01 02-02-16-939.mp4')

# os.chdir("C:/")
# for file in glob.glob("bandicam 2021-01-01 02-02-16-939.mp4"):
#     os.startfile(file)

# import win32api
# import win32con

# win32api.WinExec(
#     '{0}\\control.exe Inetcpl.cpl'.format(win32api.GetSystemDirectory()),
#     win32con.SW_NORMAL
# )
# win32api.WinExec('control.exe Inetcpl.cpl', win32con.SW_NORMAL)

# import os
# os.system('devmgmt.msc')
# import subprocess

# def openSettings():
#     subprocess.Popen([r"C:\Windows\System32\DpiScaling.exe"])

# openSettings()
