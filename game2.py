from tkinter import *

import tkinter.messagebox
tk = Tk()
tk.title("Tic Tac Toe")

click = True

def checker(buttons):
	global click
	if buttons["text"] == " " and click == True:
		buttons["text"] = "X"
		click = False
	elif buttons["text"] == " " and click == False:
		buttons["text"] = "O"
		click = True
		
	elif(buttons1["text"] == "X" and buttons2["text"] == "X" and buttons3["text"] == "X" or
		buttons4["text"] == "X" and buttons5["text"] == "X" and buttons6["text"] == "X" or
		buttons7["text"] == "X" and buttons8["text"] == "X" and buttons9["text"] == "X" or
		buttons3["text"] == "X" and buttons5["text"] == "X" and buttons7["text"] == "X" or
		buttons1["text"] == "X" and buttons5["text"] == "X" and buttons9["text"] == "X" or
		buttons1["text"] == "X" and buttons4["text"] == "X" and buttons7["text"] == "X" or
		buttons2["text"] == "X" and buttons5["text"] == "X" and buttons8["text"] == "X" or
		buttons3["text"] == "X" and buttons6["text"] == "X" and buttons9["text"] == "X"):
	   tkMessageBox.showinfo("WINNER X", "You Have Just Won a Game")
		
	elif(buttons1["text"] == "O" and buttons2["text"] == "O" and buttons3["text"] == "O" or
		buttons4["text"] == "O" and buttons5["text"] == "O" and buttons6["text"] == "O" or
		buttons7["text"] == "O" and buttons8["text"] == "O" and buttons9["text"] == "O" or
		buttons3["text"] == "O" and buttons5["text"] == "O" and buttons7["text"] == "O" or
		buttons1["text"] == "O" and buttons5["text"] == "O" and buttons9["text"] == "O" or
		buttons1["text"] == "O" and buttons4["text"] == "O" and buttons7["text"] == "O" or
		buttons2["text"] == "O" and buttons5["text"] == "O" and buttons8["text"] == "O" or
		buttons3["text"] == "O" and buttons6["text"] == "O" and buttons9["text"] == "O"):
	   tkMessageBox.showinfo("WINNER O", "You Have Just Won a Game")
		
buttons=StringVar()
button1 = Button(tk,text=" ",font=('Times 26 bold'), heigh = 4, width = 8, command=lambda:checker(button1))
button1.grid(row=1, column=0,sticky = S+N+E+W)
button2 = Button(tk,text=" ",font=('Times 26 bold'), heigh = 4, width = 8, command=lambda:checker(button2))
button2.grid(row=1, column=1,sticky = S+N+E+W)
button3 = Button(tk,text=" ",font=('Times 26 bold'), heigh = 4, width = 8, command=lambda:checker(button3))
button3.grid(row=1, column=2,sticky = S+N+E+W)
button4 = Button(tk,text=" ",font=('Times 26 bold'), heigh = 4, width = 8, command=lambda:checker(button4))
button4.grid(row=2, column=0,sticky = S+N+E+W)
button5 = Button(tk,text=" ",font=('Times 26 bold'), heigh = 4, width = 8, command=lambda:checker(button5))
button5.grid(row=2, column=1,sticky = S+N+E+W)
button6 = Button(tk,text=" ",font=('Times 26 bold'), heigh = 4, width = 8, command=lambda:checker(button6))
button6.grid(row=2, column=2,sticky = S+N+E+W)
button7 = Button(tk,text=" ",font=('Times 26 bold'), heigh = 4, width = 8, command=lambda:checker(button7))
button7.grid(row=3, column=0,sticky = S+N+E+W)
button8 = Button(tk,text=" ",font=('Times 26 bold'), heigh = 4, width = 8, command=lambda:checker(button8))
button8.grid(row=3, column=1,sticky = S+N+E+W)
button9 = Button(tk,text=" ",font=('Times 26 bold'), heigh = 4, width = 8, command=lambda:checker(button9))
button9.grid(row=3, column=2,sticky = S+N+E+W)
tk.mainloop()"# game_of_hand" 
