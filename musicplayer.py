#code for music player
from tkinter import *
from tkinter import ttk
import os
from pygame import mixer
from tkinter import filedialog
root = Tk()
mixer.init()
root.geometry("1020x800")

mixer.music.load("/storage/emulated/0/Documents/welcome.mp3")
mixer.music.play()

def search(event):
	global var
	file = None
	file = filedialog.askopenfilename()
	var.set(os.path.basename(file))
	if file:
		mixer.music.load(file)
	else:
		file = None
		
def Play():
	global var2
	mixer.music.play()
	var2.set("")
	var2.set("PLAYING....")
	
def Stop():
	mixer.music.stop()
	var2.set("")
	var2.set("STOPPED....")
	
def Pause():
	mixer.music.pause()
	var2.set("")
	var2.set("PAUSED....")
	
def UnPause():
	mixer.music.unpause()
	var2.set("")
	var2.set("PLAYING....")
	
root.config(bg = "orange")

#label = Label(root, text = "Status")
#label.pack(side = "left")
	
var = StringVar()
entry2 = Entry(root, width = 25, font = ("Times", 5, "bold"), textvariable = var)
entry2.pack()

frame = Frame(root, bg = "orange")
frame.pack(expand = True, fill = "both")

frame2 = Frame(root,bg = "red")
frame2.pack(expand = True, fill = "both")

frame3 = Frame(root, width = 1020, height = 400, bg = "orange")
frame3.pack(expand = True, side = BOTTOM)



label = Label(frame, text = "Status : ", bg = "orange")
label.pack(side= "left")

var2 = StringVar()
entry = Entry(frame, width = 15, font = ("Times", 10), textvariable = var2)
entry.pack(side = "left", padx = 20)

btn4 = Button(frame, text= "SEARCH")
btn4.pack(side = "left")
btn4.bind("<Button-1>", search)

btn = Button(frame2, text = "PLAY", font = ("Times", 10), command = Play)
btn.pack(expand = True, side = "left")

btn2 = Button(frame2, text = "STOP", font = ("Times", 10), command = Stop)
btn2.pack(expand = True, side = "left")

btn3 = Button(frame2, text = "PAUSE", font = ("Times", 10), command = Pause)
btn3.pack(expand = True, side = "left")

btn5 = Button(frame2 , text = "UNPAUSE",font = ("Times", 10), command = UnPause)
btn5.pack(side = "left")

label2 = Label(frame3, text ="●To search songs use can use search button.", bg = "orange")
label2.pack(pady = 10,side = "top")

label2 = Label(frame3, text ="●Use buttons to play or stop the song.", bg = "orange")
label2.pack(pady = 10,side = "top")



root.mainloop()
