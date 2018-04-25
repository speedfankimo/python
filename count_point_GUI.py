#!/usr/bin/python
# -*- coding: utf8 -*-

from tkinter import *
# import game_def

import pygame.mixer
sounds = pygame.mixer
sounds.init()

# sounds have to be passed otherwise they will play all together


def wait_finish(channel):
    while channel.get_busy():
        pass


correct_sound = sounds.Sound("correct.wav")
wrong_sound = sounds.Sound("wrong.wav")
finish_sound = sounds.Sound("horse.wav")

# improt GUI interface
app = Tk()
app.title("The tkinter applicaition")
# width x height + x_offset + y_offset:
app.geometry('450x150+500+300')

# create the variable text in label
num_correct = IntVar()
num_correct.set(0)

num_wrong = IntVar()
num_wrong.set(0)

num_total = IntVar()
num_total.set(0)

# fundction to increae the count and play the sound


def correct():
    num_correct.set(num_correct.get() + 1)
    num_total.set(num_total.get() + 1)
    wait_finish(correct_sound.play())


def wrong():
    num_wrong.set(num_wrong.get() + 1)
    num_total.set(num_total.get() + 1)
    wait_finish(wrong_sound.play())


correct_number = Label(app, textvariable=num_correct)
correct_number.pack(side='left', padx=5)

wrong_number = Label(app, textvariable=num_wrong)
wrong_number.pack(side='right', padx=5)

total_number = Label(app, text='total', textvariable=num_total)
total_number.pack(side='bottom', padx=1, pady=1)


l1 = Label(app, text='Pls choose Correct or Wrong?', bg="blue", fg="white")
l1.pack(side='top', padx=5, pady=5)

b1 = Button(app, text="Correct", width=10,
            command=correct)
b1.pack(side='left', padx=20, pady=20)

b2 = Button(app, text="Wrong", width=10,
            command=wrong)
b2.pack(side='right', padx=20, pady=20)


app.mainloop()
