import tkinter
import windows
import mysql.connector
from tkinter import *
from windows import *

db = mysql.connector.connect(
    host="192.168.13.100",
    user="user12",
    password="75352",
    db="user12"
)

window = Tk()
window.title("benis")
window.geometry("300x300")





def RegWindowDestroy():
    cursor = db.cursor()
    login = login_entry.get()
    password = password_entry.get()
    cursor.execute('''SELECT UserFIO,UserLogin,UserPassword,UserRole FROM User 
                        WHERE UserLogin="%s" and UserPassword="%s"''' % (login, password))
    strochka = cursor.fetchone()



    if strochka is None:
        window.destroy()
        CreateProductsWindow()
        return
    window.destroy()
    CreateProductsWindow(strochka[0], strochka[3])

login_label = Label(window,text="Login")
login_label.pack(padx=8, pady=8)

login_entry = Entry(window)
login_entry.pack(padx=8, pady=8)

password_label = Label(window,text="Password")
password_label.pack(padx=8, pady=8)

password_entry = Entry(window)
password_entry.pack(padx=8, pady=8)

btn_reg = Button(window,text="Login", command=RegWindowDestroy)
btn_reg.pack(padx=8, pady=8)

btn_ne_reg = Button(window,text="Continue without register ", command=RegWindowDestroy)
btn_ne_reg.pack(padx=8, pady=8)

window.mainloop()
