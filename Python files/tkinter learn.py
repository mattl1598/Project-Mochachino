#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      matthewl9
#
# Created:     06/02/2018
# Copyright:   (c) matthewl9 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from tkinter import *

def submit():
	print("Username",username.get())
	print("Firstname",firstname.get())
	print("Lastname",surname.get())
	clear()

def clear():
	username.delete(0,END)
	firstname.delete(0,END)
	surname.delete(0,END)
	username.focus_set()

def WriteToFile():
	file = open("names2.txt","w")
	#for count in range (5):
		#name = str(input("name"))
	file.write(username.get())
	file.write("\n")
	file.write(firstname.get())
	file.write("\n")
	file.write(surname.get())
		#if count < 4:
		   #file.write("\n")
	file.close
	clear()

#window creation
root = Tk()
root.geometry("270x300")
root.title("Student Details")
root.resizable(False, False)
root.configure(background = "Light Blue")

#form design
frame_heading = Frame(root)
frame_heading.grid(row=0,column=0,columnspan=2,padx=30,pady=5)

frame_entry = Frame(root)
frame_entry.grid(row=1,column=0,columnspan=2,padx=25,pady=10)

#place header
Label(frame_heading,text="Student Details Form",font=('Arial',16))\
.grid(row=0,column=0,padx=0,pady=5)

#place Labels
Label(frame_entry,text = "Username: ")\
.grid(row=0, column=0,padx=10,pady=5)
Label(frame_entry,text = "Firstname: ")\
.grid(row=1, column=0,padx=10,pady=10)
Label(frame_entry,text = "Surname: ")\
.grid(row=2, column=0,padx=10,pady=10)

#place text entry
username = Entry(frame_entry,width=15,bg="White")
username.grid(row = 0, column = 1, padx = 5,pady = 5)

firstname = Entry(frame_entry,width=15,bg="White")
firstname.grid(row = 1, column = 1, padx = 5,pady = 5)

surname = Entry(frame_entry,width=15,bg="White")
surname.grid(row = 2, column = 1, padx = 5,pady = 5)

#place buttons (this is jack and the beanstalk!)
submit_button = Button(root,text="submit",width = 7, command = submit)
submit_button.grid(row=2,column=0, padx=0,pady=5)

clear_button = Button(root,text="clear",width = 7, command = clear)
clear_button.grid(row=2,column=1, padx=0,pady=5)

write_button = Button(root,text="write",width = 7, command = WriteToFile)
write_button.grid(row=3,column=0, padx=5,pady=5)

def main():
    root.mainloop()
    print()

main()
