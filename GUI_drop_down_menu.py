#! usr/bin/python
# -*- coding:utf-8 -*-

from tkinter import *

app = Tk()
app.title('Deliveries')

app.geometry('750x600+500+100')

# def click save and then save data to .txt format
def save_data():
    with open('deliveries.txt', 'a') as file:
        file.write('Depot:\n%s\nDescription:\n%s\nAddress:\n%s\n' %
                   (depot.get(), description.get(), address.get('1.0', END)))
        # once input delet the all string
        #depot.delete(0, END)
        description.delete(0, END)
        address.delete('1.0', END)


def depot_location(file):
    depots = []
    with open(file) as depot_file:
        for line in depot_file:
            # rstrip()移除句尾的空白或亦可設定為其他字串
            depots.append(line.rstrip())
        return depots


Label(app, text='服務據點(Depot):').pack()
# need to add the 'StringVar' for OptionMenu modle and then OptionMenu() the second argument must be the indicted variable and the third is *list
depot = StringVar()
depot.set('Pls Choose the Depots')
sort_depots = sorted(depot_location('depots.txt'))
OptionMenu(app, depot, *sort_depots).pack()


Label(app, text='內容描述(Description):').pack()
description = Entry(app)
description.pack()

Label(app, text='寄送地址(Address):').pack()
address = Text(app)
address.pack()

Button(app, text='儲存(Save)', command=save_data).pack()

app.mainloop()
