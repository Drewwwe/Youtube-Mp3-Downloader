from pytube import YouTube
import os
import tkinter as tk
from tkinter import filedialog
def download_mp3(link):
    yt = YouTube(link)
    title = yt.title.replace(" ", "_")
    filename = f"{title}.mp4"
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory()
    stream = yt.streams.filter(only_audio=True).first()
    print("Downloading...")
    stream.download(filename=filename)
    os.rename(filename, f"{title}.mp3")
    os.chdir(folder_path)
    os.startfile(f"{title}.mp3")
    print("Done!")
link = input("Enter YouTube link:")
download_mp3(link)
