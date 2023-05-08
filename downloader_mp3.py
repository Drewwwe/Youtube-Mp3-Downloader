from pytube import YouTube
import os
import tkinter as tk
from tkinter import filedialog
def download_mp3(link):
    yt = YouTube(link)
    title = yt.title.replace(" ", "_")
    filename = f"{title}.mp4"
    folder_path = filedialog.askdirectory()
    stream = yt.streams.filter(only_audio=True).first()
    print("Downloading...")
    stream.download(filename=filename)
    os.rename(filename, f"{title}.mp3")
    os.startfile(os.path.join(folder_path, f"{title}.mp3"))
    print("Done!")
if __name__ == '__main__':
    link = input("Enter YouTube link:")
    download_mp3(link)
