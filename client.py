
import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
import ftplib
import os
import ntpath #This is used to extract filename from path
import time
from ftplib import FTP
from tkinter import filedialog
from pathlib import Path


from playsound import playsound
import pygame
from pygame import mixer

PORT  = 8050
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096

name = None
listbox =  None
filePathLabel = None

global song_counter
song_counter = 0

global USERNAME
global PASSWORD



def play():
    global song_selected
    song_selected=listbox.get(ANCHOR)
    
    pygame
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.play()
    if(song_selected != ""):
        infoLabel.configure(text="Now Playing: " +song_selected)
    else:
       infoLabel.configure(text="")

def stop():
    global song_selected
    pygame
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.pause()
    infoLabel.configure(text="")


def pause():
    global song_selected
    pygame
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.pause()

def resume():
    global song_selected
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.play()
    
    mixer.music.unpause()

def download():
    global USERNAME
    global PASSWORD
    textarea.insert (END,"\n"+"\nPlease wait file is downloading.....") 
    textarea.see ("end")
    song_selected-listbox.get(ANCHOR)
    infoLabel.configure (text="Downloading "+song_selected)
    HOSTNAME = "127.0.0.1"
    USERNAME "lftpd" =
    PASSWORD = "lftpd"
    home = str(Path.home())
    download_path=home+"/Downloads"
    ftp_server = ftplib.FTP (HOSTNAME,USERNAME,PASSWORD)
    ftp_server.encoding = "utf-8"
    ftp_server.cwd('shared_files')
    locals = os.path.join (download_path, song_selected)
    file = open(locals, 'wb')
    ftp_server.retrbinary('RETR '+ song_selected, file.write)
    ftp_server.dir()
    file.close() ftp_server.quit()
    infoLabel.configure (text="Download Complete")
    time.sleep (1)
    if (song_selected != ""):
    infoLabel.configure (text="Now Playing" +song_selected)
    else:
    infoLabel.configure (text="")
    USERNAME PASSWORD

    
        

    
        
#Client GUI
def musicWindow(): 
    global song_counter
    global filePathLabel
    global listbox
    global infoLabel
    
    window=Tk()
    window.title('Music Window')
    window.geometry("300x350")
    window.configure(bg='LightSkyBlue')
    
    selectlabel = Label(window, text= "Select Song",bg='LightSkyBlue', font = ("Calibri",8))
    selectlabel.place(x=2, y=1)
    
    listbox = Listbox(window,height = 10,width = 39,activestyle = 'dotbox',bg='LightSkyBlue',borderwidth=2, font = ("Calibri",10))
    listbox.place(x=10,y=18)
    for file in os.listdir('shared_files'):
        filename = os.fsdecode(file)
        listbox.insert(song_counter, filename)
        song_counter = song_counter + 1
        
    scrollbar1 = Scrollbar(listbox)
    scrollbar1.place(relheight = 1,relx = 1)
    scrollbar1.config(command = listbox.yview)
    
    PlayButton=Button(window,text="Play", width=10,bd=1,bg='SkyBlue',font = ("Calibri",10), command = play)
    PlayButton.place(x=30,y=200)
    
    Stop=Button(window,text="Stop",bd=1,width=10,bg='SkyBlue', font = ("Calibri",10), command = stop)
    Stop.place(x=200,y=200)

       
    
    Upload=Button(window,text="Upload",width=10,bd=1,bg='SkyBlue', font = ("Calibri",10))
    Upload.place(x=30,y=300)
    
    Download =Button(window,text="Download",width=10,bd=1,bg='SkyBlue', font = ("Calibri",10))
    Download.place(x=200,y=300)
    
    infoLabel = Label(window, text= "",fg= "blue",bg='SkyBlue', font = ("Calibri",8))
    infoLabel.place(x=4, y=330)
    
    window.mainloop()
    
def setup():
    global SERVER
    global PORT
    global IP_ADDRESS
    global song_counter

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

    musicWindow()

#Initiate Server Connection    
setup()


   



# # import socket
# # import sys
# # from threading import Thread
# # import select
# # from tkinter import *
# # from tkinter import ttk

# # import ftplib
# # 
# # import ntpath
# # 
# # from ftplib import FTP
# import socket
# from threading import Thread
# from tkinter import *
# from tkinter import ttk
# import ftplib
# import os
# import time
# import ntpath #This is used to extract filename from path

# from tkinter import filedialog
# from pathlib import Path


# from playsound import playsound
# import pygame
# from pygame import mixer



# PORT  = 8050
# IP_ADDRESS = '127.0.0.1'
# SERVER = None

# labelchat = None

# # name = None
# # listbox =  None
# # textarea= None
# # labelchat = None
# # text_message = None
# # filePathLabel = None
# infoLabel = None

# BUFFER_SIZE = 4096

# # def connectWithClient():
# #     global SERVER
# #     global listbox
# #     global song_counter

# #     text=listbox.get(ANCHOR)
# #     list_item = text.split(":")
# #     msg="connect "+list_item[1]
# #     SERVER.send(msg.encode('ascii'))



# # def disconnectWithClient():
# #     global SERVER

# #     text=listbox.get(ANCHOR)
# #     list_item = text.split(":")
# #     msg="disconnect "+list_item[1]
# #     SERVER.send(msg.encode('ascii'))


# # def quitSession():
# #     global SERVER
# #     SERVER.close()

# # def getFileSize(file_name):
# #     with open(file_name, "rb") as file:
# #         chunk = file.read()
# #         return len(chunk)

# # def receiveMessage():
# #     global SERVER
# #     global BUFFER_SIZE
    


#     # for file in os.listdir("shared_files"):
#     #     filename=os.fsdecode(file)
#     #     listbox.insert(song_counter,filename)
#     #     listbox.insert(song_counter,filename)
#     #     song_counter=song_counter+1

#     # while True:
#     #     chunk = SERVER.recv(BUFFER_SIZE)
#     #     try:
#     #         if("tiul" in chunk.decode() and "1.0," not in chunk.decode()):
#     #             letter_list = chunk.decode().split(",")
#     #             listbox.insert(letter_list[0],letter_list[0]+":"+letter_list[1]+": "+letter_list[3]+" "+letter_list[5])
#     #             print(letter_list[0],letter_list[0]+":"+letter_list[1]+": "+letter_list[3]+" "+letter_list[5])
#     #         else:
#     #             textarea.insert(END,"\n"+chunk.decode('ascii'))
#     #             textarea.see("end")
#     #             print(chunk.decode('ascii'))
#     #     except:
#     #         pass


# def play():
#     global song_selected
#     song_selected=listbox.get(ANCHOR)

#     pygame.init()
#     mixer.init()
#     mixer.music.load("shared_files/"+song_selected)
#     mixer.music.play()
#     if(song_selected !=""):
#         infoLabel.configure(text="Now Playing:" +song_selected)
#     else:
#         infoLabel.configure(text="")



# # def browseFiles():
# #     global textarea
# #     global filePathLabel

# #     try:
# #         filename = filedialog.askopenfilename()
# #         filePathLabel.configure(text=filename)
# #         HOSTNAME = "127.0.0.1"
# #         USERNAME = "lftpd"
# #         PASSWORD = "lftpd"

# #         ftp_server = FTP(HOSTNAME, USERNAME, PASSWORD)
# #         ftp_server.encoding = "utf-8"
# #         ftp_server.cwd('shared_files')
# #         fname=ntpath.basename(filename)
# #         with open(filename, 'rb') as file:
# #             ftp_server.storbinary(f"STOR {fname}", file)

# #         ftp_server.dir()
# #         ftp_server.quit()
# #     except FileNotFoundError:
# #         print("Cancle Button Pressed")


# def sendMessage():
#     global SERVER
#     global textarea
#     global text_message

#     msgtosend= text_message.get()                                              

#     SERVER.send(msgtosend.encode('ascii'))
#     textarea.insert(END,"\n"+"You>"+msgtosend)
#     textarea.see("end")
#     text_message.delete(0, 'end')



# def showClientsList():
#     global listbox
#     listbox.delete(0,"end")
#     SERVER.send("show list".encode('ascii'))


# def connectToServer():
#     global SERVER
#     # global name

#     # cname = name.get()
#     # SERVER.send(cname.encode())

# def stop():
#     global song_selected
#     pygame
#     mixer.init()
#     mixer.music.load("shared_files/"+song_selected)
#     mixer.music.pause()
#     infoLabel.configure(text="")

# def resume():
#     global song_selected
#     mixer.init()
#     mixer.music.load("shared_files/"+song_selected)
#     mixer.music.play()

# def pause():
#     global song_selected
#     pygame
#     mixer.init()
#     mixer.music.load("shared_files/"+song_selected)
#     mixer.music.play()


# def musicWindow():

#     print("\n\t\t\t\tIP MESSENGER")

    
#     window=Tk()

#     window.title('Messenger')
#     window.geometry("500x350")

#     # global name
#     global playButton
#     global listbox
#     # global textarea
#     global selectlabel
#     # global text_message
#     # global filePathLabel
#     global Stop
    
#     window=Tk()
#     window.title('music Window')
#     window.geometry("300*300")
#     window.configure(bg='LightSkyBlue')

#     selectlabel = Label(window, text= "select song",bg='LightSkyBlue', font = ("Calibri",0))
#     selectlabel.place(x=2, y=1)

#     listbox = Listbox(window,height = 10,width = 39,activestyle = 'dotbox',bg='LightSkyBlue',borderwidth=2, font = ("Calibri",10))
#     listbox.place(x=10, y=10)

#     ResumeButton = Button(window,text="resume",width = 10,bd=1,bg="skyBlue", font = ("Calibri",10))
#     ResumeButton.place(x=10, y=10)


#     scrollbar1 = Scrollbar(listbox)
#     scrollbar1.place(relheight = 1,relx = 1)
#     scrollbar1.config(command = listbox.yview)

#     playButton = Button(window, text= "play",bg='LightSkyBlue',width=10,bd=1, font = ("Calibri",10),command=play)
#     playButton.place(x=30, y=200)

#     Stop=Button(window,text="Stop",bd=1,width=10,bg="skyBlue", font=("Calibri",10))
#     Stop.place(x=200,y=200)

#     pauseButton=Button(window,text="pause",width=10,bd=1,bg="skyblue",font=("Calibri",10),command=pause)
#     pauseButton.place(x=200,y=250)

#     Upload=Button(window,text="Upload",width=10,bd=1,bg="Skyblue",font=("Calibri,10"))
#     Upload.place(x=30,y=250)

#     Download=Button(window,text="Download",width=10,bd=1,bg='SkyBlue',font=("Calibri",10))
#     Download.place(x=200,y=250)

#     infoLabel = Label(window, text= "",fg= "blue", font = ("Calibri",8))
#     infoLabel.place(x=4, y=200)

#     window.mainloop()


    

#     # namelabel = Label(window, text= "Enter Your Name", font = ("Calibri",10))
#     # namelabel.place(x=10, y=8)

#     # name = Entry(window,width =30,font = ("Calibri",10))
#     # name.place(x=120,y=8)
#     # name.focus()

#     # connectserver = Button(window,text="Connect to Chat Server",bd=1, font = ("Calibri",10), command = connectToServer)
#     # connectserver.place(x=350,y=6)

#     # separator = ttk.Separator(window, orient='horizontal')
#     # separator.place(x=0, y=35, relwidth=1, height=0.1)

#     # labelusers = Label(window, text= "Active Users", font = ("Calibri",10))
#     # labelusers.place(x=10, y=50)

    

    
#     # connectButton=Button(window,text="Connect",bd=1, font = ("Calibri",10), command = connectWithClient)
#     # connectButton.place(x=282,y=160)

#     # disconnectButton=Button(window,text="Disconnect",bd=1, font = ("Calibri",10), command = disconnectWithClient)
#     # disconnectButton.place(x=350,y=160)

#     # refresh=Button(window,text="Refresh",bd=1, font = ("Calibri",10), command = showClientsList)
#     # refresh.place(x=435,y=160)

    

#     # textarea = Text(window, width = 67,height = 6,font = ("Calibri",10))
#     # textarea.place(x=10,y=200)

#     # scrollbar2 = Scrollbar(textarea)
#     # scrollbar2.place(relheight = 1,relx = 1)
#     # scrollbar2.config(command = listbox.yview)

    
#     # attach=Button(window,text="Attach & Send",bd=1, font = ("Calibri",10), command = browseFiles)
#     # attach.place(x=10,y=305)

#     # text_message = Entry(window, width =43, font = ("Calibri",12))
#     # text_message.pack()
#     # text_message.place(x=98,y=306)

   
   
#     # send=Button(window,text="Send",bd=1, font = ("Calibri",10), command = sendMessage)
#     # send.place(x=450,y=305)




# def setup():
#     global SERVER
#     global PORT
#     global IP_ADDRESS

#     SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     SERVER.connect((IP_ADDRESS, PORT))

#     musicWindow()

# setup()

# #     receive_thread = Thread(target=receiveMessage)              
# #     receive_thread.start()

#     #  openChatWindow()




