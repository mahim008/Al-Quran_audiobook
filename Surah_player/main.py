import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os

player = tkr.Tk()
player.title("Al-Quran audiobook")
player.geometry("450 X 350")

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