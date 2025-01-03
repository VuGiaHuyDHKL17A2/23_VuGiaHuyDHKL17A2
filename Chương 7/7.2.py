from tkinter import * 

window = Tk() 
window.title("Xem gì") 

lbl = Label(window, text="Hello", font=("Arial Bold", 50))

window.geometry('280x80') 

lbl.grid(column=0, row=0) 
window.mainloop()