from tkinter import *
import random

root = Tk()
root.title('Dice roller!')
root.geometry("500x500")


# roll dice
def roll_dice():
    d1 = random.choice(my_dice)
    d2 = random.choice(my_dice)

    # update labels
    dice_label1.config(text=d1)
    dice_label2.config(text=d2)


# create dice
my_dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685', ]

# frame
my_frame = Frame(root)
my_frame.pack(pady=20)

# dice labels
dice_label1 = Label(my_frame, text='', font=("Arial", 100))
dice_label1.grid(row=0, column=0, padx=5)

dice_label2 = Label(my_frame, text='', font=("Arial", 100))
dice_label2.grid(row=0, column=1, padx=5)

# create button
my_button = Button(root, text="roll dice", command=roll_dice)
my_button.pack(pady=20)

root.mainloop()
