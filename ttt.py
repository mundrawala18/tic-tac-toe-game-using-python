from tkinter import *
import random
import tkinter.messagebox
tk=Tk()
tk.title("Tic Tac Toe")
r,t=0,0
old_btn=0
possible=[]
#btn=[btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9]
click = 0
def plot(buttons):
	global click
	global t,r
	global old_btn,possible
	if buttons["text"] == "" and click == 0:
		buttons["text"]="X"
		btn.remove(buttons)
		click=1
		check()
		old_btn = buttons
		t=comp_turn(buttons)
		plot(t)
		r=0
	elif buttons["text"]!= "" and click == 1:
		r=1
		t=comp_turn(old_btn)
		plot(t)
	elif buttons["text"]== "" and click == 1:
		buttons["text"]="O"
		btn.remove(buttons)
		click=0
		r=0
		check()
def check():
	if (btn1["text"]== "X" and btn2["text"]== "X" and btn3["text"]== "X" or 
		btn4["text"]== "X" and btn5["text"]== "X" and btn6["text"]== "X" or
		btn7["text"]== "X" and btn8["text"]== "X" and btn9["text"]== "X" or 
		btn1["text"]== "X" and btn5["text"]== "X" and btn9["text"]== "X" or
		btn3["text"]== "X" and btn5["text"]== "X" and btn7["text"]== "X" or
		btn7["text"]== "X" and btn4["text"]== "X" and btn1["text"]== "X" or 
		btn3["text"]== "X" and btn6["text"]== "X" and btn9["text"]== "X" or
		btn2["text"]== "X" and btn5["text"]== "X" and btn8["text"]== "X"):
		tkinter.messagebox.showinfo("Message :)","Player 'X' Win")	
		exit()
	elif (btn1["text"]== "O" and btn2["text"]== "O" and btn3["text"]== "O" or 
		btn4["text"]== "O" and btn5["text"]== "O" and btn6["text"]== "O" or
		btn7["text"]== "O" and btn8["text"]== "O" and btn9["text"]== "O" or 
		btn1["text"]== "O" and btn5["text"]== "O" and btn9["text"]== "O" or
		btn3["text"]== "O" and btn5["text"]== "O" and btn7["text"]== "O" or
		btn7["text"]== "O" and btn4["text"]== "O" and btn1["text"]== "O" or 
		btn3["text"]== "O" and btn6["text"]== "O" and btn9["text"]== "O" or
		btn2["text"]== "O" and btn5["text"]== "O" and btn8["text"]== "O"):
		tkinter.messagebox.showinfo("Message :)","Player 'O' Win")
		exit()
	
	elif ((btn1["text"]=="X" or btn1["text"]=="O") and (btn2["text"]=="X" or btn2["text"]=="O") and (btn3["text"]=="X" or btn3["text"]=="O") and
		(btn4["text"]=="X" or btn4["text"]=="O") and (btn5["text"]=="X" or btn5["text"]=="O") and (btn6["text"]=="X" or btn6["text"]=="O") and 
		(btn7["text"]=="X" or btn7["text"]=="O") and (btn8["text"]=="X" or btn8["text"]=="O") and (btn9["text"]=="X" or btn9["text"]=="O")):
		tkinter.messagebox.showinfo("Message :)","DRAWN")
		exit()
#buttons=StringVar()
btn1=Button(tk,text="",font=('Arial 26 bold'),height=4,width=8,command=lambda:plot(btn1))
btn1.grid(row=1,column=0)
btn2=Button(tk,text="",font=('Arial 26 bold'),height=4,width=8,command=lambda:plot(btn2))
btn2.grid(row=1,column=1)
btn3=Button(tk,text="",font=('Arial 26 bold'),height=4,width=8,command=lambda:plot(btn3))
btn3.grid(row=1,column=2)
btn4=Button(tk,text="",font=('Arial 26 bold'),height=4,width=8,command=lambda:plot(btn4))
btn4.grid(row=2,column=0)
btn5=Button(tk,text="",font=('Arial 26 bold'),height=4,width=8,command=lambda:plot(btn5))
btn5.grid(row=2,column=1)
btn6=Button(tk,text="",font=('Arial 26 bold'),height=4,width=8,command=lambda:plot(btn6))
btn6.grid(row=2,column=2)
btn7=Button(tk,text="",font=('Arial 26 bold'),height=4,width=8,command=lambda:plot(btn7))
btn7.grid(row=3,column=0)
btn8=Button(tk,text="",font=('Arial 26 bold'),height=4,width=8,command=lambda:plot(btn8))
btn8.grid(row=3,column=1)
btn9=Button(tk,text="",font=('Arial 26 bold'),height=4,width=8,command=lambda:plot(btn9))
btn9.grid(row=3,column=2)

btn=[btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9]

def comp_turn(buttons):
	global r
	global possible
	if r==0:
		if buttons == btn1:
			possible = [btn2,btn4,btn5]
			if (btn1["text"]=="X" and btn3["text"]=="X"):
				return btn2
			if (btn1["text"]=="X" and btn7["text"]=="X"):
				return btn4
			if (btn1["text"]=="X" and btn9["text"]=="X"):
				return btn5
			if (btn2["text"]=="X"):
				return btn3
			if (btn4["text"]=="X"):
				return btn7
			if (btn5["text"]=="X"):
				return btn9
				
		elif buttons == btn2:
			possible= [btn1,btn5,btn3]
			if (btn2["text"]=="X" and btn3["text"]=="X"):
				return btn1
			if (btn2["text"]=="X" and btn8["text"]=="X"):
				return btn5
			if (btn2["text"]=="X" and btn1["text"]=="X"):
				return btn3
			if (btn1["text"]=="X"):
				return btn3
			if (btn5["text"]=="X"):
				return btn8
			if (btn3["text"]=="X"):
				return btn1
		elif buttons == btn3:
			possible= [btn2,btn5,btn6] 
			if (btn3["text"]=="X" and btn1["text"]=="X"):
				return btn2
			if (btn3["text"]=="X" and btn9["text"]=="X"):
				return btn6
			if (btn3["text"]=="X" and btn7["text"]=="X"):
				return btn5
			if (btn2["text"]=="X"):
				return btn1
			if (btn5["text"]=="X"):
				return btn7
			if (btn6["text"]=="X"):
				return btn9
		elif buttons == btn4:
			possible= [btn1,btn5,btn7]
			if (btn4["text"]=="X" and btn7["text"]=="X"):
				return btn1
			if (btn4["text"]=="X" and btn6["text"]=="X"):
				return btn5
			if (btn4["text"]=="X" and btn1["text"]=="X"):
				return btn7
			if (btn1["text"]=="X"):
				return btn7
			if (btn5["text"]=="X"):
				return btn6
			if (btn7["text"]=="X"):
				return btn1
		elif buttons == btn5:
			possible= [btn1,btn2,btn3,btn4,btn6,btn7,btn8,btn9]
			if (btn5["text"]=="X" and btn1["text"]=="X"):
				return btn9
			if (btn5["text"]=="X" and btn2["text"]=="X"):
				return btn8
			if (btn5["text"]=="X" and btn3["text"]=="X"):
				return btn7
			if (btn5["text"]=="X" and btn4["text"]=="X"):
				return btn6
			if (btn5["text"]=="X" and btn6["text"]=="X"):
				return btn4
			if (btn5["text"]=="X" and btn7["text"]=="X"):
				return btn3
			if (btn5["text"]=="X" and btn8["text"]=="X"):
				return btn2
			if (btn5["text"]=="X" and btn9["text"]=="X"):
				return btn1
		elif buttons == btn6:
			possible= [btn3,btn5,btn9] 
			if (btn6["text"]=="X" and btn9["text"]=="X"):
				return btn3
			if (btn6["text"]=="X" and btn4["text"]=="X"):
				return btn5
			if (btn6["text"]=="X" and btn3["text"]=="X"):
				return btn9
			if (btn3["text"]=="X"):
				return btn9
			if (btn5["text"]=="X"):
				return btn4
			if (btn9["text"]=="X"):
				return btn3
		elif buttons == btn7:
			possible= [btn4,btn5,btn8]
			if (btn7["text"]=="X" and btn3["text"]=="X"):
				return btn5
			if (btn7["text"]=="X" and btn1["text"]=="X"):
				return btn4
			if (btn7["text"]=="X" and btn9["text"]=="X"):
				return btn8
			if (btn5["text"]=="X"):
				return btn3
			if (btn4["text"]=="X"):
				return btn1
			if (btn8["text"]=="X"):
				return btn9
		elif buttons == btn8:
			possible= [btn7,btn5,btn9]
			if (btn8["text"]=="X" and btn9["text"]=="X"):
				return btn7
			if (btn8["text"]=="X" and btn2["text"]=="X"):
				return btn5
			if (btn8["text"]=="X" and btn7["text"]=="X"):
				return btn9 
			if (btn7["text"]=="X"):
				return btn9
			if (btn5["text"]=="X"):
				return btn2
			if (btn9["text"]=="X"):
				return btn7
		elif buttons == btn9:
			possible= [btn6,btn5,btn8]
			if (btn9["text"]=="X" and btn3["text"]=="X"):
				return btn6
			if (btn9["text"]=="X" and btn1["text"]=="X"):
				return btn5
			if (btn9["text"]=="X" and btn7["text"]=="X"):
				return btn8
			if (btn6["text"]=="X"):
				return btn3
			if (btn5["text"]=="X"):
				return btn1
			if (btn8["text"]=="X"):
				return btn7
	else:
		choice=(random.choice(btn))
		return choice

	choice=(random.choice(possible))
	return choice	
tk.mainloop()