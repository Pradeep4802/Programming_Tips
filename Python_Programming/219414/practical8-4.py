from tkinter import*
from tkinter import messagebox
root=Tk()
root.configure(background="cyan")
root.geometry("700x700")
L=Label(root,text="COLLEGE NAME: Mulund Collage Of Commerce",font=("Times",15),fg="black",relief="groove",bd=3,bg="pink")
L.grid(row=0,column=0)
L0=Label(root,text="COLLEGE Address:Mulund West Mumbai-80",font=("Times",15),fg="black",relief="groove",bd=3,bg="pink")
L0.grid(row=1,column=0,pady=5)
Label(text="***************---------*************-----------**************-----------***********").grid(row=2,column=0)
Label(text="--------*************-----------****").grid(row=2,column=1)
L1=Label(root,text="fisrt Name:",font=('calibari',11,'bold'),height=1,width=20,relief="sunken",bd=3,bg="magenta")
L1.grid(row=3,column=0,pady=5)
E1=Entry(root,bd='2')
E1.grid(row=3,column=1,padx=1)
L2=Label(root,text="Last Name:",font=('calibari',11,'bold'),height=1,width=20,relief="sunken",bd=3,bg="magenta")
L2.grid(row=4,column=0,pady=5)
E2=Entry(root,bd='2',relief="groove")
E2.grid(row=4,column=1,padx=1)
L3=Label(root,text="Gender:",font=('calibari',11,'bold'),height=2,width=20,relief="sunken",bd=3,bg="magenta")
L3.grid(row=5,column=0,pady=5)
x=IntVar()
R1=Radiobutton(root,text="Male",variable=x,value=1,relief="groove",height=2,width=5).grid(row=5,column=1,pady=5)
R2=Radiobutton(root,text="Female",variable=x,value=2,relief="groove",height=2,width=5).grid(row=5,column=2,pady=5)
L4=Label(root,text="Age:",font=('calibari',11,'bold'),height=1,width=20,relief="sunken",bd=3,bg="magenta")
L4.grid(row=6,column=0,pady=3)
s=Spinbox(root,from_=0 ,to=100,width=15).grid(row=6,column=1,pady=3,padx=1)
L5=Label(root,text="Hobbies:",font=('calibari',11,'bold'),height=1,width=20,relief="sunken",bd=3,bg="magenta")
L5.grid(row=7,column=0,pady=3)
a1=IntVar()
a2=IntVar()
a3=IntVar()
a4=IntVar()
c1=Checkbutton(text="Singing",font=('calibari',11,'bold'),variable=a1,offvalue=0,onvalue=1,bg="yellow")
c1.grid(row=8,column=0)
c2=Checkbutton(text="Swimming",font=('calibari',11,'bold'),variable=a2,offvalue=0,onvalue=1,bg="yellow")
c2.grid(row=8,column=1)
c3=Checkbutton(text="Dancing",font=('calibari',11,'bold'),variable=a3,offvalue=0,onvalue=1,bg="yellow")
c3.grid(row=9,column=0,pady=3)
c4=Checkbutton(text="Reading",font=('calibari',11,'bold'),variable=a4,offvalue=0,onvalue=1,bg="yellow")
c4.grid(row=9,column=1,pady=3)
L6=Label(root,text="Address:",font=('calibari',11,'bold'),height=1,width=20,relief="sunken",bd=3,bg="magenta")
L6.grid(row=10,column=0,pady=3)
E3=Text(root,bd='2',relief="groove",height=1,width=20)
E3.grid(row=10,column=1,padx=1)
L7=Label(root,text="Select ur favourite programming language!!!",font=('calibari',11,'bold'),height=1,width=35,relief="sunken",bd=3,bg="magenta")
L7.grid(row=11,column=0,pady=3)
b1=IntVar()
b2=IntVar()
b3=IntVar()
b4=IntVar()
C1=Checkbutton(text="C",font=('calibari',11,'bold'),variable=b1,offvalue=0,onvalue=1,bg="yellow")
C1.grid(row=12,column=0)
C2=Checkbutton(text="C++",font=('calibari',11,'bold'),variable=b2,offvalue=0,onvalue=1,bg="yellow")
C2.grid(row=12,column=1)
C3=Checkbutton(text="JAVA",font=('calibari',11,'bold'),variable=b3,offvalue=0,onvalue=1,bg="yellow")
C3.grid(row=13,column=0,pady=2)
C4=Checkbutton(text="PYTHON",font=('calibari',11,'bold'),variable=b4,offvalue=0,onvalue=1,bg="yellow")
C4.grid(row=13,column=1,pady=2)
def mess():
    m=messagebox.showinfo("BIODATA","Thank u visiting my Form!!")
B2=Button(root,text="SUBMIT",font=('calibari',10,'bold'),bg='green',command=mess,height=2,width=7,relief="ridge")
B2.grid(row=14,column=0,pady=5,padx=3)
root.mainloop()