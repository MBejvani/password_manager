from tkinter import *
class pwg:
    
    def __init__(self, win):
        self.r1_x = 30
        self.r2_x = 150
        
        self.lbl1=Label(win, text='First Name')
        self.lbl1.place(x=self.r1_x, y=20)
        self.t1=Entry()
        self.t1.insert(0,"FirstName")
        self.t1.place(x=self.r2_x, y=20)
        
        self.lbl2=Label(win, text='Last Name')
        self.lbl2.place(x=self.r1_x, y=50)
        self.t2=Entry()
        self.t2.insert(0,"Last Name")
        self.t2.place(x=self.r2_x, y=50)
        
        self.lbl3=Label(win, text='Phone Number')
        self.lbl3.place(x=self.r1_x, y=80)
        self.t3=Entry()
        self.t3.insert(0,"09121613641")
        self.t3.place(x=self.r2_x, y=80)

        self.lbl4=Label(win, text='Birthday')
        self.lbl4.place(x=self.r1_x, y=110)
        self.t4=Entry()
        self.t4.insert(0,"20240124")
        self.t4.place(x=self.r2_x, y=110)

        self.lbl5=Label(win, text='User Name')
        self.lbl5.place(x=self.r1_x, y=160)
        self.t5=Entry()
        self.t5.insert(0,"bj1854")
        self.t5.place(x=self.r2_x, y=160)

        self.lbl6=Label(win, text='Website')
        self.lbl6.place(x=self.r1_x, y=190)
        self.t6=Entry()
        self.t6.insert(0,"google.com")
        self.t6.place(x=self.r2_x, y=190)

        self.lbl7=Label(win, text='Password Length')
        self.lbl7.place(x=self.r1_x, y=220)
        self.t7=Entry()
        self.t7.insert(0,"8")
        self.t7.place(x=self.r2_x, y=220)

        #---------------------------

        self.b1=Button(win, text='Generate',fg='blue' , command=self.Generate)
        self.b1.place(x=330, y=20)
##        self.b2.bind('<Button-1>', self.sub)
##        self.b2.place(x=200, y=150)
        
        self.v1 = IntVar()
        self.c1 = Checkbutton(win, text = "Adaptive Password", variable=self.v1)
        self.c1.place(x=330, y=50)
        

        self.b2=Button(win, text='Save',fg='green' , command=self.Save)
        self.b2.place(x=330, y=130)

        import time
        curr = time.time()
        ti=time.ctime(curr)
        self.lbl6=Label(win, text=ti)
        self.lbl6.place(x=330, y=160)

        
        self.tp=Entry(bg="yellow",bd=3)
        self.tp.place(x=330, y=100)

##        if self.v1.get()==1:
##            print("sdfsfdsf")
        
    def Generate(self):
        self.tp.delete(0, 'end')
        import string, secrets
        characters = string.ascii_letters + string.digits + string.punctuation
        password = [''.join(secrets.choice(characters) for _ in range(int(self.t7.get()))),
                    self.t1.get()]
        if self.v1.get() == 0:
            self.tp.insert(END, password[0])
        elif self.v1.get() == 1:
            self.tp.insert(END, password[1])
        
    def Save(self):
        import time
        curr = time.time()
        pass_list = open("Passwords.txt","a")
##        date and time
        L=time.ctime(curr)+"  --->  "+self.tp.get()+"\n"
        pass_list.write(L)
        pass_list.close()

window=Tk()

pwg(window)
window.title('Password Generator')
window.geometry("500x300+10+10")

window.mainloop()
