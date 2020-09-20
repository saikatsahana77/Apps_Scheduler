import tkinter as tk
from tkinter.ttk import *
import sqlite3
from tkinter import filedialog
import os

app_list = []


def add_to_list():
    global app_list
    conn = sqlite3.connect('app.db')
    c = conn.cursor()
    c.execute("SELECT * FROM APPS")
    rec = c.fetchall()
    for r in rec:
        app_list.append(r[0])
    conn.commit()
    conn.close()


def save_to_db():
    global app_list
    conn = sqlite3.connect('app.db')
    c = conn.cursor()
    c.execute("DELETE FROM APPS")
    for i in app_list:
        c.execute("INSERT INTO APPS VALUES(:app)",
                  {
                      'app': i,
                  })
    conn.commit()
    conn.close()


def add():
    global app_list
    filenames = filedialog.askopenfilenames(
        initialdir="/", title="Select File/Files", filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    for filename in filenames:
        if (filename != ""):
            app_list.append(filename)
            listBox.insert(parent='', index='end',
                           values=((app_list.index(filename))+1, filename))


def delete():
    global app_list
    curItems = listBox.selection()
    k = []
    for item in curItems:
        k.append((listBox.item(item)["values"][0])-1)
    k.sort(reverse=True)
    for i in k:
        app_list.pop(i)
    for record in listBox.get_children():
        listBox.delete(record)
    for idx, i in enumerate(app_list):
        listBox.insert(parent='', index='end', values=(idx, i))


def run():
    global app_list
    for app in app_list:
        os.startfile(app)


def entered1(event):
    btn1.configure(
        bg="#343434",
        fg="#ffffff",
    )


def left1(event):
    btn1.configure(
        bg="#ffffff",
        fg="#000000",
    )


def entered2(event):
    btn2.configure(
        bg="#343434",
        fg="#ffffff",
    )


def left2(event):
    btn2.configure(
        bg="#ffffff",
        fg="#000000",
    )


def entered3(event):
    btn3.configure(
        bg="#343434",
        fg="#ffffff",
    )


def left3(event):
    btn3.configure(
        bg="#ffffff",
        fg="#000000",
    )


def on_closing():
    save_to_db()
    root.destroy()


root = tk.Tk()
root.title("App Runner")
root.geometry("600x600")
root.resizable(0, 0)
root.iconbitmap("./icon.ico")
add_to_list()
style = Style()
style.theme_use("clam")
style.configure("Treeview", font=("Arial", 12))
style.configure("Treeview.Heading", font=("Arial", 16))
style.configure('TButton', font=('Arial', 15, 'bold'),
                borderwidth='2')
canvas = tk.Canvas(root, width=600, height=600, bg="#070769")
canvas.create_text(300, 30, fill="white", font="Arial 20 bold",
                   text="Run Apps In Just One Click!!")
cols = ('ID', 'Application')
listBox = Treeview(canvas, columns=cols, show='headings',
                   selectmode="extended", height=18)
listBox.column("ID", width=70, minwidth=100)
listBox.column("Application", width=330, minwidth=450)
for idx, i in enumerate(app_list):
    listBox.insert(parent='', index='end', values=(idx, i))
vsb = Scrollbar(canvas, orient="vertical", command=listBox.yview)
vsb.place(x=502, y=70, height=398)
listBox.configure(yscrollcommand=vsb.set)
vsb1 = Scrollbar(canvas, orient="horizontal", command=listBox.xview)
vsb1.place(x=98, y=468, width=416)
listBox.configure(xscrollcommand=vsb1.set)
listBox.heading(cols[0], text=cols[0])
listBox.heading(cols[1], text=cols[1])
listBox.pack(padx=40, pady=70)
canvas.pack(fill=tk.BOTH)
canvas1 = tk.Canvas(root, bg="#070769", width=600)
btn1 = tk.Button(canvas1, text="Add Application",
                 font='Arial 15 bold', command=add, padx=5, pady=3)
btn1.grid(row=0, column=0, padx=18, columnspan=2, pady=8)
btn2 = tk.Button(canvas1, text="Delete Application", font='Arial 15 bold',
                 command=delete, padx=5, pady=3)
btn2.grid(row=0, column=4, columnspan=2, padx=18)
btn3 = tk.Button(canvas1, text="Run Apps!",
                 font='Arial 15 bold', command=run, padx=5, pady=3)
btn3.grid(row=0, column=2, padx=18, columnspan=2)
btn1.bind("<Enter>", entered1)
btn1.bind("<Leave>", left1)
btn2.bind("<Enter>", entered2)
btn2.bind("<Leave>", left2)
btn3.bind("<Enter>", entered3)
btn3.bind("<Leave>", left3)
canvas1.pack(expand=True, fill=tk.BOTH)
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
