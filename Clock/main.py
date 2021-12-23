from tkinter import *
from time import strftime
#Create a Main Window
root=Tk()
#Write the title of the main window
root.title("Clock")
#Label for the time to be displayed
label=Label(root,font=("ds-digital",50),background="black",foreground="cyan")
label.pack(anchor="center")
def Time():
    string=strftime("%H:%M:%S %p")
    #to enter the string into the label config is used
    label.config(text=string)
    #after 1 seconds execute time function again and update the label
    label.after(1000,Time)
#Call the Time funciton
Time()
#To keep on excuting untill close is used
mainloop()
