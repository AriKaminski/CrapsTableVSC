from tkinter import *
window=Tk()

lbl=Label(window, text="Craps table game", fg='red', font=("Helvetica", 16))
lbl.place(x=320, y=50)

btn=Button(window, text="Start game", fg='blue')
btn.place(x=80, y=100)

txtfld=Entry(window, text="How much would you like to bet?", bd=5)
txtfld.place(x=80, y=150)

window.title('Craps Table game')
window.geometry("800x400+10+10")
window.mainloop()