from tkinter import *
from pytube import YouTube
import webbrowser
from tkinter.messagebox import *
yt = None
strm_value = None
root = Tk()
def high():
     yt.streams.get_highest_resolution().download()
def low():
    yt.streams.get_lowest_resolution().download()
def now():
    videos = list(enumerate(yt.streams.all()))
    videos[int(strm_value.get())].download()
def download():
    global yt
    yt = YouTube(link_value.get())
    quality = Tk()
    quality.iconbitmap("Title_Icon.ico")
    quality.title("Youtube Video Details")
    quality.geometry("280x280")
    Label(quality,text=f"Video Title: {yt.title}").pack()
    Button(quality,text="Click here to view video thumbnail",command=view_thumbnail).pack(padx=12,pady=8)
    global strm_value
    strm_value = StringVar()
    Button(quality,text="Click here to download in low quality",command=low).pack(padx=12,pady=8)
    # strm_value.set("Enter streaming quality here")
    Button(quality,text ="Click here to download in high quality",command=high).pack(padx=12,pady=8)
    quality.mainloop
def view_thumbnail():
    webbrowser.open(yt.thumbnail_url)

root.title("Youtube Video Downloader")
root.geometry("760x460")
root.iconbitmap("Title_Icon.ico")
label=Label(root,text="Welcome To Youtube Video Downloader Ultimate",font=("Courier", 20)).pack(padx=13,pady=9)
link_value = StringVar()
Label(root,text="Enter your youtube video link here").pack(padx=10,pady=7)
Entry(root,textvariable=link_value).pack()
Button(root,text="Download",command=download).pack(padx=9,pady=6)
root.mainloop()
