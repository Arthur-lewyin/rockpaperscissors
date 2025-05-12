from tkinter import *
import random 
import tkinter.font as font

root = Tk()
root.geometry("500x300")

player_score = 0 
computer_score = 0

options = [('rock',0),('paper',1),('scissors',2)]

def cw():
    global player_score, computer_score, winner_label

    computer_score = computer_score + 1
    winner_label.config(text="Computer wins, HA HA!")
    cs2.config(text ="Computer Score : " +str(computer_score))
    ys2.config(text = "Your score : " + str(player_score))
    
def yw():
    global player_score, computer_score, winner_label

    player_score = player_score + 1
    winner_label.config(text="You won...")
    cs2.config(text ="Computer Score : " +str(computer_score))
    ys2.config(text = "Your score : " + str(player_score))
    
def tie():
    global player_score, computer_score, winner_label

    winner_label.config(text="Only losers tie")
    cs2.config(text ="Computer Score : " +str(computer_score))
    ys2.config(text = "Your score : " + str(player_score))
  

title = Label(text= "Rock Paper Scissors",font =font.Font(size = 20), fg="grey")
title.pack()

winner_label= Label(text = "Let's start the Game...", font= font.Font(size= 10), fg = "green")
winner_label.pack()

frame = Frame(root)
frame.pack()

yo = Label(frame, text = "Your Options : ", font = font.Font(size = 10), fg = "grey")
yo.grid(row = 0, column= 0, pady = 8)

r = Button(frame, text = "Rock", font = font.Font (size = 10),fg ="black",bg = "red")
r.grid(row =1 , column = 1, padx= 8, pady=5)

p = Button(frame, text = "Paper", font = font.Font (size = 10),fg ="black",bg = "grey")
p.grid(row =1 , column = 2, padx= 8, pady=5)

s = Button(frame, text = "Scissors", font = font.Font (size = 10),fg ="black",bg = "blue")
s.grid(row =1 , column = 3, padx= 8, pady=5)

sc = Label(frame, text="Score", font = font.Font(size = 10), fg= "grey")
sc.grid(row = 2, column= 0, pady = 8)

ys = Label(frame, text = "You Selected : -- ", font = font.Font(size = 10), fg = "black")
ys.grid(row = 3, column= 1, pady = 8)

ys2 = Label(frame, text = "Your score : -- ", font = font.Font(size = 10), fg = "black")
ys2.grid(row = 3, column= 2, pady = 8)

cs = Label(frame, text = "Computer Selected : -- ", font = font.Font(size = 10), fg = "black")
cs.grid(row =4, column= 1, pady = 8)

cs2 = Label(frame, text = "Computer Score : -- ", font = font.Font(size = 10), fg = "black")
cs2.grid(row =4, column= 2, pady = 8)

root.mainloop()