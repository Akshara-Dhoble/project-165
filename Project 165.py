# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 13:16:47 2023

@author: Akshara Sagar Dhoble
"""

from tkinter import *
from PIL import ImageTk , Image
from tkinter import filedialog

root = Tk()

root.title("IMAGE VIEWER")
root.geometry("500x500")
root.configure(background = "black")

label = Label(root , bg = "white" , highlightthickness=5)
label.place(relx=0.5 , rely= 0.5 , anchor=CENTER)

img_path = ""

def openfile():
    global img_path
    img_path = filedialog.askopenfilename(title = "Open Text File" , filetypes = [("image files" , "*.jpg , *.gif , *.jpeg , *.txt")])
    print(img_path)
    im = Image.open(img_path)
    img = ImageTk.PhotoImage(im)
    label_image["image"] = img
    img.close()
    
def rotateImage():
    global img_path
    im = Image.open(img_path)
    img = ImageTk.PhotoImage(im.rotate(180))
    label_image["image"] = imgprint(img_path)
    img.close()
    
    
    
btn = Button(root , text= "View Photo" , command=openfile)
btn.place(relx=0.5 , rely=0.18 , anchor=CENTER)

btn_1 = Button(root , text= "Rotate Photo" , command=rotateImage)
btn_1.place(relx=0.5 , rely=0.78 , anchor=CENTER)

root.mainloop()