#code for notepad using tkinter
from tkinter import *
import os
from tkinter import font
from tkinter import ttk, filedialog, colorchooser
root = Tk()
root.geometry("1020x1600")
root.title("Untitled - Notepad")
###func##
def Open():
	global file
	file = filedialog.askopenfilename(title = "Select a file", filetypes = [("All Files","*.*"),("Text File","*.txt"),("Python File","*.py")])
	
	if file:
		with open(file , "r") as f:
			f2 = f.read()
			text.insert(1.0,f2)
			f.close()
			root.title(os.path.basename(file))
	else:
		file = None
	
def New():
	root.title("Untitled - Notepad")
	text.delete(0.0, END)
	
def Save():
	global file
	if file == None:
		file2 = filedialog.asksaveasfilename(title = "Save the file",filetypes = [("All Files","*.*")])
		if file2:
			with open(file2, "a") as f3:
				f3.write(text.get(0.0,END))
				f3.close()
				root.title(os.path.basename(file2))
		else:
			file2 = None
	else:
		with open(file2, "a") as f4:
			f4.write(text.get(0.0,END))
			f4.close()
			root.title(os.path.basename(file2))
	
def Exit():
	root.destroy()
	
def change_color():
	clr = colorchooser.askcolor(title = "select color ",color = "red")
	text.config(bg = clr[1])
	
def change_font_color():
	clt = colorchooser.askcolor(title ="choose color" ,color = "black")
	text.config(fg = clt[1])
	
def Cut():
	text.event_generate(("<<Cut>>"))
	
def Copy():
	text.event_generate(("<<Copy>>"))

def Paste():
	text.event_generate(("<<Paste>>"))
	
###Menus##
main_menu = Menu(root)
root.config(menu=main_menu)
###File Menu####
file_menu = Menu(main_menu, tearoff = False)
main_menu.add_cascade(label = "File",menu = file_menu)

file_menu.add_command(label = "Open",command = Open)
file_menu.add_command(label = "New",command = New)
file_menu.add_command(label = "Save",command = Save)
file_menu.add_command(label = "Exit",command = Exit)

### Edit Menu##
edit = Menu(main_menu , tearoff = False)
main_menu.add_cascade(label = "Edit",menu = edit)
edit.add_command(label = "Cut", command = Cut)
edit.add_command(label = "Copy", command = Copy)
edit.add_command(label = "Paste", command = Paste)



##### Formatting tool Bar###

format = Menu(main_menu,tearoff = False)
main_menu.add_cascade(label = "Format",menu = format)
format.add_command(label = "Background", command = change_color)
format.add_command(label = "Font Color",command = change_font_color)

#### Handwritings####

label2 = Label(root)
label2.pack(side = "top", fill = X)

font_tuple = font.families()
font_family = StringVar()

combo = ttk.Combobox(label2, textvariable = font_family, state = "readonly", width = 25)
combo.pack(side = "left")
combo["values"] = font_tuple
combo.current(font_tuple.index("Dancing Script"))
###### font size####
size_tuple = tuple(range(8,31))
size_family = IntVar()
comb = ttk.Combobox(label2, textvariable = size_family , state = "readonly")
comb.pack(side = "left")
comb["values"] = size_tuple
comb.current(size_tuple.index(10))



#main_menu.config()

##### Text Area##
scroll = Scrollbar(root)
scroll.pack(fill = Y, side = RIGHT)

text = Text(root,  yscrollcommand = scroll.set, wrap = "word")
text.pack(fill = "both", expand = True)
scroll.config(command = text.yview)

file = None

text.config(font=("Dancing Script",10))
current_size = 10
current_font = "Dancing"
def Change(event):
	global current_font
	global current_size
	current_font = font_family.get()
	current_size = size_family.get()
	text.config(font=(current_font, current_size))
	
combo.bind("<<ComboboxSelected>>",Change)
comb.bind("<<ComboboxSelected>>",Change)



root.mainloop()
