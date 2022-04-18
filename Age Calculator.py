import tkinter as tk
from datetime import date
today = date.today()
 
def age():
    d= int(e1.get())
    m=int(e2.get())
    y=int(e3.get())
    age =today.year-y-((today.month, today.day)<(m,d))
    t1.config(state='normal')
    t1.delete('1.0', tk.END)
    t1.insert(tk.END,age)
    t1.config(state='disabled')
 

window = tk.Tk()
window.geometry("350x300")
window.config(bg="#003049")
window.title('Age Calculator')
 
l1 = tk.Label(window,text="Age Calculator",font=("roboto", 20),fg="white",bg="#003049")
l2 = tk.Label(window,font=("roboto",14),text="Enter Your Birth Date.",fg="white",bg="#003049")
 
l_d=tk.Label(window,text="Date: ",font=('roboto',12,"bold"),fg="white",bg="#003049")
l_m=tk.Label(window,text="Month: ",font=('roboto',12,"bold"),fg="white",bg="#003049")
l_y=tk.Label(window,text="Year: ",font=('roboto',12,"bold"),fg="white",bg="#003049")
e1=tk.Entry(window,width=8)
e2=tk.Entry(window,width=8)
e3=tk.Entry(window,width=8)
 
b1=tk.Button(window,text="Calculate Age",font=("roboto",13),command= age)
 
l3 = tk.Label(window,text="The Calculated Age is: ",font=('roboto',12,"bold"),fg="white",bg="#003049")
t1=tk.Text(window,width=8,height=0,state="disabled")

 
l1.place(x=70,y=5)
l2.place(x=60,y=60)
l_d.place(x=100,y=100)
l_m.place(x=100,y=130)
l_y.place(x=100,y=160)
e1.place(x=180,y=100)
e2.place(x=180,y=130)
e3.place(x=180,y=160)
b1.place(x=100,y=210)
l3.place(x=50,y=260)
t1.place(x=240,y=260) 
window.mainloop()