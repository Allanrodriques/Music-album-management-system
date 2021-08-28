from tkinter import *

from tkinter.ttk import Combobox
from tkinter import Toplevel

from PIL import Image, ImageTk
from tkinter import messagebox
from main import Music_1
import pymysql


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Window")
        self.root.geometry("1357x700+0+0")
        self.root.config(bg="white")
        # ===BG Image===
        self.bg = ImageTk.PhotoImage(file="images/2890210.jpg")
        bg = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        # ===Left Image===
        self.left = ImageTk.PhotoImage(file="images/music8.jpeg")
        left = Label(self.root, image=self.left).place(x=30, y=95, relwidth=0.33, relheight=0.73)

        # ====Login Frame====
        top = Toplevel(root)
        frame1 = Frame(self.root, bg="white")
        frame1.place(x=480, y=100, width=700, height=500)

        title = Label(frame1, text="Login Here", font=("Arial", 30, "bold"), bg="white", fg="blue").place(x=50, y=30)

        email = Label(frame1, text="Registered Email", font=("Arial", 20, "bold"), bg="white", fg="grey").place(x=50,
                                                                                                                y=145)
        self.txt_email = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_email.place(x=50, y=185, width=350)

        password = Label(frame1, text="Password", font=("Arial", 20, "bold"), bg="white", fg="grey").place(x=50, y=265)
        self.txt_password = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_password.place(x=50, y=300, width=350)

        btn_login = Button(frame1, text="Login", command=self.login, font=("arial", 20), bg="royalblue", fg="lightblue",
                           bd=0, cursor="hand2", ).place(x=50, y=420, relwidth=0.8, relheight=0.1)

        btn_register = Button(self.root, text="Register", font=("arial", 20), bg="blue", fg="white", bd=0,
                       cursor="hand2",command=self.register_window).place(x=130, y=500, relwidth=0.2, relheight=0.05)

    def register_window(self):
        self.root.destroy()
        import register

    def editor_window(self):
        self.root.destroy()
        import init

    def login(self):
        if self.txt_email.get() == "" or self.txt_password.get() == "":
            messagebox.showerror("Error", "All fields are compulsory",parent=self.root)
        else:
            
            con = pymysql.connect(host="localhost", user="root", password="9822442264", database="register")
            cur = con.cursor()
            cur.execute("select * from register_1 where email=%s and password=%s",
                            (self.txt_email.get(),
                             self.txt_password.get()
                             ))
            row=cur.fetchone()
            if row==None:

               messagebox.showerror('Error','Invalid Username or Password'

                                    ,parent=self.root)

               self.loginclear()

               self.email_txt.focus()

            else:
                open_main=messagebox.askyesno('YesNo','Do You want to login',parent=self.root)

                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Music_1(self.new_window)
                else:
                    if not open_main:
                        return
           
            con.commit()
            con.close()

    def new_win(self):
        self.new_window=Toplevel(self.root)
        self.app=Music_1(self.new_window)

            


if __name__== "__main__":
    root=Tk()
    obj=Login(root)   
    root.mainloop()
