import tkinter.tix
import tkinter.ttk
from tkinter import *
from tkinter import ttk
import mysql.connector



db = mysql.connector.connect(
    host="192.168.13.100",
    user="user12",
    password="75352",
    db="user12"
)


def CreateProductsWindow(fio=None, role=None):
    # new window
    products_window = Tk()
    products_window.title("Register")
    products_window.geometry("500x500")

    # db query
    if fio!=None:
        cursor=db.cursor()
        cursor.execute('''SELECT RoleName FROM Role WHERE RoleID=%s''' % role)
        role_name = cursor.fetchone()

        fi = fio.split()
        login_info = Label(products_window, text=f"User:{fi[0]} {fi[1]}")
        login_info.pack(anchor=NE, padx=2, pady=2)

        role_info = Label(products_window, text=f"Role:{role_name[0]}")
        role_info.pack(anchor=NE, padx=2, pady=2)

    else:
        login_info = Label(products_window, text=f"User: -")
        login_info.pack(anchor=NE, padx=2, pady=2)

        role_info = Label(products_window, text=f"Role: -")
        role_info.pack(anchor=NE, padx=2, pady=2)

    # определяем данные для отображения
    people = [("Tom", 38, "tom@email.com"), ("Bob", 42, "bob@email.com"), ("Sam", 28, "sam@email.com")]

    # определяем столбцы
    columns = ("name", "age", "email")

    tree = ttk.Treeview(columns=columns, show="headings")
    tree.pack(fill=BOTH, expand=1)
    # tree.configure()

    # определяем заголовки
    tree.heading("name", text="Имя")
    tree.heading("age", text="Возраст")
    tree.heading("email", text="Email")


    def print_to_console():
        selected = tree.focus()
        item = tree.item(selected, 'values')
        print(item)

    menu = Menu(products_window, tearoff=0)
    menu.add_command(label='print', command=print_to_console)

    def show(event):
        menu.post(event.x_root, event.y_root)

    for col in columns:
        tree.column(col, stretch=YES, width=166)

    for person in people:
        tree.insert("", END, values=person)

    tree.bind("<Button-3>", show)

