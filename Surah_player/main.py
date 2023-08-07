import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os

player = tkr.Tk()
player.title("Al-Quran audiobook")
player.geometry("450x350")

directory = askdirectory()
os.chdir(directory)
surah_list = os.listdir()
playlist = tkr.Listbox(player, font="Helvetica 12 bold", bg="yellow", selectmode=tkr.SINGLE)

for surah in surah_list:
    position = 0
    playlist.insert(position, surah)
    position += 1

pygame.init()
pygame.mixer.init()

def play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()

def stop():
    pygame.mixer.music.stop()

def pause():
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()

play_button = tkr.Button(player, width=5, height=3, font="Helvetica 12 bold", text="PLAY", command=play, bg="green", fg="white")
pause_button = tkr.Button(player, width=5, height=3, font="Helvetica 12 bold", text="PAUSE", command=pause, bg="purple", fg="white")
unpause_button = tkr.Button(player, width=5, height=3, font="Helvetica 12 bold", text="UNPAUSE", command=unpause, bg="blue", fg="white")
stop_button = tkr.Button(player, width=5, height=3, font="Helvetica 12 bold", text="STOP", command=stop, bg="red", fg="white")


var = tkr.StringVar()
surah_title = tkr.Label(player, font="Helvetica 12 bold", textvariable=var)

surah_title.pack()
play_button.pack(fill="x")
pause_button.pack(fill="x")
unpause_button.pack(fill="x")
stop_button.pack(fill="x")
playlist.pack(fill="both", expand="yes")

player.mainloop()


