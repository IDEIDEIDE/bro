#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 18:17:21 2021

@author: clockshield
"""

from tkinter import *
import random
root=Tk()
root.title("lol")
root.geometry("400x400")

label_yourfriend = Label(root)
label_friendcheck = Label(root)
friends = ["Roy", "Abe", "Stacy", "Gregory", "Tommie"]
friendcount = 1

def randomfriend():
    nubmer = random.randint(0, 4)
    print(friends[nubmer])
    label_yourfriend["text"] = "Your friend is: " + friends[nubmer]
    friendcount = friendcount + 1
    label_friendcheck["text"] = "Friend Count: " + str(friendcount)
    

btn = Button(root, text = "press to get your friend loner", command = randomfriend)
btn.place(relx = 0.5, rely = 0.4, anchor=CENTER)
label_yourfriend.(relx = 0.5, rely = 0.5, anchor=CENTER)
label_friendcheck.place(relx = 0.5, rely = 0.6, anchor=CENTER)
root.mainloop()