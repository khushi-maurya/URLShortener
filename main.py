
# import all necessary libraries

from tkinter import *

import pyshorteners

# the main function starts here

# Function to Shorten the URL link
def short():
    long_url = entry1.get()

    type_tiny = pyshorteners.Shortener()
    short_url = type_tiny.tinyurl.short(long_url)

    entry2.insert(END,short_url)

# Working on the designing of the URL Shortener Project's Accessibility

# Create the main window
win=Tk()
win.geometry("400x320")
win.title("URL SHORTENER")

# Create GUI components
frame=Frame(win,width=460,height=20,bg="navy blue")
frame.grid(row=0,column=0)

Label(win,text="Enter Your URL Link",font="Modern 18 bold",fg="navy blue",bg="pink",width=22,height=1).place(x=70,y=50)

entry1=Entry(win,font="10",bd=3,width=40)
entry1.place(x=18,y=110)

Button(win,text="Click to Short",font="courier 14 bold",bg="blue",fg="white",bd=10,height=1,width=15,command=short).place(x=100,y=160)

Label(win,text="Shorted URL Is:",font="Modern 13 bold",fg="white",bg="navy blue",width=16).place(x=50,y=235)
entry2=Entry(win,font="Modern 16 bold",bg="pink",width=28,bd=4)
entry2.place(x=50,y=260)

# Run the main event loop
win.mainloop()