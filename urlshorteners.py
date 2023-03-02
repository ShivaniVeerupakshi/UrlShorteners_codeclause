'''import pyshorteners
url=input("Enter long URL here: ")
short=pyshorteners.Shortener()
x=short.tinyurl.short(url)
print("The shortened url is:",x)'''

import pyperclip
import pyshorteners

from tkinter import *                # tkinter for GUI design

#define GUI for shortener
import urlshortener as urlshortener

root = Tk()

#set the geometry
# root.geometry("400*200")

# give a title
root.title("URL Shortener")

#set a background color
root.configure(bg="#49A")

#take 2 string variable for keep long and short URL
url = StringVar()
url_address = StringVar()

#define 2 function for shortening url and copy the url
def urlshortener():
    urladdress = url.get()
    url_short = pyshorteners.Shortener().tinyurl.short(urladdress)
    url_address.set(url_short)

def copyurl():
    url_short = url_address.get()
    pyperclip.copy(url_short)

Label(root , text="My URL Shortener" , font="poppins").pack(pady=10)
Entry(root, textvariable=url).pack(pady=5)
Button(root, text="Generate Short URL", command=urlshortener).pack(pady=7)
Entry(root, textvariable=url_address).pack(pady=5)
Button(root, text="Copy URL",command=copyurl).pack(pady=5)

root.mainloop()


