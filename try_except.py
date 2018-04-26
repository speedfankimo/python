#! usr/bin/python
# -*- coding:utf-8 -*-

#import GUI module 
from tkinter import *
#improt messagebox (showinfo,showwarning,showeerror,askquestion,askokcancel,askyesnocancel,askretrycancel)
import tkinter.messagebox

app = Tk()
app.title('Deliveries')
app.geometry('750x600+500+100')



# def click save and then save data to .text
def save_data():
	# try..except : when excuate the 'try' find the Exception then process the 'except', otherwise, ignore the 'except'
	try:
		with open('deliveries.txt', 'a') as file:
			file.write('Depot:\n%s\nDescription:\n%s\nAddress:\n%s\n' %(depot.get(), description.get(), address.get('1.0', END)))
			#once input delet the all string
			#depot.delete(0, END)
			description.delete(0, END)
			address.delet('1.0', END)
	# Exception statement to be as variable 'exception'		
	except Exception as exception:
		# change original window's tile to show the exception
		app.title(exception)
		# create another pop-out window to show the exception
		ex_app=Tk()
		ex_app.title('Excption')
		ex_app.geometry('400x70+600+300')
		Label(ex_app, text = 'Excption : %s' % (exception), fg="red").pack()
		# improt the messagebox.showerror
		error_app = tkinter.messagebox.showerror('Error','Record cannot write into becasue of : %s' %(exception))
		# improt the messagebox.askretrycancel
		error_app = tkinter.messagebox.askretrycancel('Error','Record cannot write into becasue of : %s' %(exception))
		if error_app == True:
			save_data()
		else:
			tkinter.messagebox.showinfo('MESSAGE', 'There is something wrong, pls recheck')


Label(app, text='服務據點(Depot):').pack()
# need to add the 'value' , 'variable' and 'StringVar' for Radiobutton modle in order to distinct the selection
depot = StringVar()
depot.set(None)
Radiobutton(app,text='三重',value = 'Snagchong',variable=depot).pack()
Radiobutton(app,text='新莊',value = 'XinZhoung',variable=depot).pack()
Radiobutton(app,text='板橋',value = 'BanQiao',variable=depot).pack()

Label(app, text='內容描述(Description):').pack()
description = Entry(app)
description.pack()

Label(app, text='寄送地址(Address):').pack()
address = Text(app)
address.pack()

Button(app, text='儲存(Save)', command=save_data).pack()

app.mainloop()
