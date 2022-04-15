from tkinter import *
 
def divide_numbers():
    result =float(e1.get()) / float(e2.get())
    result  = round(result,4)
    label_text.set(result)
 
window = Tk()
window.geometry("400x200")
window.title('Elasticity Calculator')
label_text = StringVar();
Label(window,text='Elasticity Calculator').grid(row=0, column=1)
Label(window, text="").grid(row=1, column=0)
Label(window, text="Stress:").grid(row=2, column=0)
Label(window, text="").grid(row=3, column=0)
Label(window, text="Strain:").grid(row=4,column=0)
Label(window, text="").grid(row=5, column=0)
Label(window, text="Elasticity:").grid(row=7,column=0,padx=10)
result=Label(window, text="", textvariable=label_text).grid(row=7,column=1)
 
e1 = Entry(window)
e2 = Entry(window)
 
e1.grid(row=2, column=1)
e2.grid(row=4, column=1)
 
b4 = Button(window, text="Calculate", width=10, command = divide_numbers)
b4.grid(row=5, column=1, padx=5, pady=5)
 
window.mainloop()