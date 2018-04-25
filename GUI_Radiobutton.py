#! usr/bin/python
# -*- coding:utf-8 -*-

from tkinter import *

app = Tk()
app.title('Deliveries')
app.geometry('750x600+500+100')

# def click save and then save data to .text
def save_data():
    with open('deliveries.txt', 'a') as file:
        file.write('Depot:\n%s\nDescription:\n%s\nAddress:\n%s\n' %
                   (depot.get(), description.get(), address.get('1.0', END)))
        # once input delet the all string
        #depot.delete(0, END)
        description.delete(0, END)
        address.delete('1.0', END)


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
