from asset import *
from liability import *
from owner_equity import *
from expense import *
from general_journal import *
from income_summary import *
from revenue import *
from drawing import *
from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from datetime import datetime
from tkinter import messagebox
import tkinter as tk
from xlsxwriter.workbook import Workbook
import PIL.Image
import sqlite3
from PIL import Image, ImageGrab
from tkcalendar import DateEntry
from tkcalendar import Calendar, DateEntry
# from tkinter.ttk import *
import time
# from tkinter.ttk import *
# from tkinter import *
# from tkinter import ttk
# from datetime import datetime
# from tkinter import messagebox
# import tkinter as tk
# from xlsxwriter.workbook import Workbook
# import PIL.Image
# import sqlite3
# from PIL import Image, ImageGrab
# from tkcalendar import DateEntry
# from tkcalendar import Calendar, DateEntry
# from tkinter.ttk import *
# import time


class Accounting_management:
    def __init__(self,company_name):
        self.company_name=company_name
        self.export()
        self.loading()
        # self.view_t_account()
        self.get_data()
        self.interface()


    def view_t_account(self):
        root = Tk()
        self.get_data()
        root.geometry("1300x600")
        root.resizable(0, 0)
        root.title("Accounting")
        window_height = 500
        window_width = 1000
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        root.configure(background='powder blue')
        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 11))
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 13, 'bold'))
        currentMonth = datetime.now().month
        currentYear = datetime.now().year
        x = Label(root, text="View T_Accounts", font='Helvetica 18 bold', height=2, width=100, fg="black",
                  bg="steel blue").pack()
        frame = Frame(root)
        account_title = tk.StringVar()
        choices = []
        for k, v in Assets.assets.items():
            choices.append(v.title)
        for k, v in Liabilities.liabilities.items():
            choices.append(v.title)
        for k, v in Owner_Equity.owner_equity.items():
            choices.append(v.title)
        for k, v in Expense.expense.items():
            choices.append(v.title)
        for k, v in Revenue.revenue.items():
            choices.append(v.title)
        for k, v in Drawing.drawing.items():
            choices.append(v.title)
        def get():
            tree.delete(*tree.get_children())
            value= account_title.get()
            x = {}
            for k, v in Assets.assets.items():
                x[v.title] = v
            for k, v in Expense.expense.items():
                x[v.title] = v
            for k, v in Liabilities.liabilities.items():
                x[v.title] = v
            for k, v in Revenue.revenue.items():
                x[v.title] = v
            for k, v in Drawing.drawing.items():
                x[v.title] = v
            for k, v in Owner_Equity.owner_equity.items():
                x[v.title] = v

            acc_list = list(x.keys())
            # print("hello")
            # print(acc_list)
            # user = input("choose account : ")
            print("{:^20}|{:^20}".format("Debit", "Credit"))
            print("{:^20}|{:^20}".format(" ","_" * 20, "_" * 20))
            tree.insert('', 'end', values=(" ","_" * 20, "_" * 20))
            for k, v in Entries.entries.items():
                if v.account_id == x[value].id:
                    if v.amount_type == 'Debit':
                        print("{:^20}|{:^20}".format(Journal.journal[v.journal_id].date,v.amount, ""))
                        tree.insert('', 'end', values=(Journal.journal[v.journal_id].date,v.amount, ""))
                    else:
                        print("{:^20}|{:^20}".format(Journal.journal[v.journal_id].date,"", v.amount))
                        tree.insert('', 'end', values=(Journal.journal[v.journal_id].date,"", v.amount))
            print("{:^20}|{:^20}".format(" ","_" * 20, "_" * 20))
            tree.insert('', 'end', values=(" ","_" * 20, "_" * 20))
        account_title.set(choices[0])  # set the default option
        Label(root, text="Choose Account", font='Helvetica 12 bold', bg="powder blue").pack()
        popupMenu = OptionMenu(root, account_title, *choices).pack()
        but_1=Button(root, text="Confirm", command=get, height=2, width=10, bg="steel blue", fg="black").pack()
        frame.pack()
        def back():
            root.destroy()
            self.interface()

        button_close = Button(root, text="Close", command=back, height=2, width=10, bg="steel blue", fg="black").pack()
        tree = ttk.Treeview(frame, columns=(1, 2, 3), height=10, show="headings", style="mystyle.Treeview")
        tree.pack(side='left')
        tree.heading(1,text="Date")
        tree.heading(2, text="Debit")
        tree.heading(3, text="Credit")
        tree.column(1, width=300)
        tree.column(2, width=200)
        tree.column(3,width=200)
        scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
        scroll.pack(side='right', fill='y')
        tree.configure(yscrollcommand=scroll.set)
        root.mainloop()

    def loading(self):
        root=Tk()
        root.geometry("630x600")
        root.title("Accounting")
        canvas=Canvas(root,width=600,height=600)
        canvas.pack()
        my_image=PhotoImage(file="probitslogo.png")
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        window_height = 750
        window_width = 1375
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        root.overrideredirect(True)
        root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
        def disable_event():
            pass
        root.protocol("WM_DELETE_WINDOW", disable_event)
        canvas.create_image(0,0,anchor=NW,image=my_image)
        label_1=Label(root,text="ACCOUNTING CYCLE",font='Helvetica 30 italic',height=2, width=57, fg="white",bg="steel blue").place(x=17,y=550)
        self.get_data()
        root.after(1000, root.destroy)
        # progress = Progressbar(canvas, orient=HORIZONTAL,length=100, mode='determinate')
        #
        # def bar():
        #     progress['value'] = 20
        #     root.update_idletasks()
        #     time.sleep(1)
        #
        #     progress['value'] = 40
        #     root.update_idletasks()
        #     time.sleep(1)
        #
        #     progress['value'] = 50
        #     root.update_idletasks()
        #     time.sleep(1)
        #
        #     progress['value'] = 60
        #     root.update_idletasks()
        #     time.sleep(1)
        #
        #     progress['value'] = 80
        #     root.update_idletasks()
        #     time.sleep(1)
        #     progress['value'] = 100
        #
        # progress.pack(pady=10)
        # Button(canvas, text='Start', command=bar).pack(pady=10)
        root.mainloop()





    def interface(self):
        #600,630
        root = Tk()
        root.geometry("630x600")
        root.resizable(0, 0)
        root.title("Accounting")
        root.configure(background='powder blue')
        canvas = Canvas(root, width=700, height=600)
        canvas.place(x=0,y=0)
        canvas.configure(background="powder blue")
        my_image = PhotoImage(file="main_screen.png")
        canvas.create_image(-300, 0, anchor=NW, image=my_image)
        style = ttk.Style()
        menubar = Menu(root)
        def one():
            root.destroy()
            self.view_accounts()
        def two():
            root.destroy()
            self.journal_entry()
        def three():
            root.destroy()
            self.add_accounts()
        def four():
            root.destroy()
            self.view_journal()
        def five():
            root.destroy()
            self.view_trial_balance()
        def six():
            root.destroy()
            self.statements("income")
        def six_2():
            root.destroy()
            self.statements("owner equity")
        def six_3():
            root.destroy()
            self.statements("balance sheet")
        def seven():
            MsgBox = tk.messagebox.askquestion('Refresh Accounts', 'Are you sure you want to refresh all accounts?',icon='warning')
            if MsgBox=="yes":
                self.refresh()
                messagebox.showinfo("Refresh Successfull", "All accounts have been refreshed.")
                root.destroy()
                self.interface()
            else:
                root.destroy()
                self.interface()
        def eight():

            MsgBox = tk.messagebox.askquestion('Close Accounts', 'Are you sure you want to close all accounts?',icon='warning')
            if MsgBox=="yes":
                self.close_accounts()
                messagebox.showinfo("Closing.", "All accounts have been closed.")
                root.destroy()
                self.interface()
            # else:
            #     messagebox.showinfo("Closing","All accounts have already been closed.")
            #     root.destroy()
            #     self.interface()
            # else:
            #     root.destroy()
            #     self.interface()
        def nine():
            root.destroy()
        def ten():
            root.destroy()
            self.help()
        def eleven():
            root.destroy()
            self.view_t_account()
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=nine)
        menubar.add_cascade(label="File", menu=filemenu)

        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_separator()
        helpmenu.add_command(label="Accounts", command=one)
        helpmenu.add_command(label="General journal", command=four)
        helpmenu.add_command(label="Trial balance", command=five)
        helpmenu.add_command(label="T accounts", command=eleven)
        menubar.add_cascade(label="Views", menu=helpmenu)

        add = Menu(menubar, tearoff=0)
        add.add_separator()
        add.add_command(label="Account", command=three)
        add.add_command(label="Input journal entry",command=two)
        menubar.add_cascade(label="Add", menu=add)
        closing = Menu(menubar, tearoff=0)
        closing.add_separator()
        closing.add_command(label="Close Accounts", command=eight)
        menubar.add_cascade(label="Closing", menu=closing)

        statements=Menu(menubar,tearoff=0)
        statements.add_separator()
        statements.add_command(label="Income statement",command=six)
        statements.add_command(label="Owner\'s equity statement", command=six_2)
        statements.add_command(label="Balance sheet", command=six_3)
        menubar.add_cascade(label="Statements",menu=statements)

        others=Menu(menubar,tearoff=0)
        others.add_separator()
        others.add_command(label="Refresh all accounts", command=seven)
        others.add_command(label="Help", command=ten)
        menubar.add_cascade(label="Others", menu=others)

        root.config(menu=menubar)
        x = Label(root, text="Usman Fawad", font='Helvetica 14', height=3, width=100, fg="steel blue",bg="powder blue").place(x=500,y=650)
        window_height = 550
        window_width = 650   #650
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        #---------------------------------------------------------------------------------
        # def one():
        #     root.destroy()
        #     self.view_accounts()
        # def two():
        #     root.destroy()
        #     self.journal_entry()
        # def three():
        #     root.destroy()
        #     self.add_accounts()
        # def four():
        #     root.destroy()
        #     self.view_journal()
        # def five():
        #     root.destroy()
        #     self.view_trial_balance()
        # def six():
        #     root.destroy()
        #     self.statements("income")
        # def six_2():
        #     root.destroy()
        #     self.statements("owner equity")
        # def six_3():
        #     root.destroy()
        #     self.statements("balance sheet")
        # def seven():
        #     MsgBox = tk.messagebox.askquestion('Refresh Accounts', 'Are you sure you want to refresh all accounts?',icon='warning')
        #     if MsgBox=="yes":
        #         self.refresh()
        #         messagebox.showinfo("Refresh Successfull", "All accounts have been refreshed.")
        #         root.destroy()
        #         self.interface()
        #     else:
        #         root.destroy()
        #         self.interface()
        # def eight():
        #     MsgBox = tk.messagebox.askquestion('Close Accounts', 'Are you sure you want to close all accounts?',icon='warning')
        #     if MsgBox=="yes":
        #         self.close_accounts()
        #         messagebox.showinfo("Closing.", "All accounts have been closed.")
        #         root.destroy()
        #         self.interface()
        #     else:
        #         root.destroy()
        #         self.interface()
        # def nine():
        #     root.destroy()
        # def ten():
        #     root.destroy()
        #     self.help()
        # def eleven():
        #     root.destroy()
        #     self.view_t_account()
        # Label(root, text="Views",font='Helvetica 12 bold',bg="powder blue").place(y=65)
        # button_1=Button(root,text="View all accounts",font='Helvetica 8 bold',command=one, height=3, width=18, fg="white",bg="steel blue").place(y=100)
        # button_2=Button(root,text="Input Journal Entries",font='Helvetica 8 bold',height=3, width=18, fg="white",bg="steel blue",command=two).place(y=205)
        # Label(root, text="Add", font='Helvetica 12 bold', bg="powder blue").place(y=170)
        # Label(root, text="Statements", font='Helvetica 12 bold', bg="powder blue").place(y=270)
        # button_3=Button(root, text="Add an account", font='Helvetica 8 bold', height=3, width=18, fg="white",bg="steel blue",command=three).place(x=140,y=205)
        # button_4=Button(root, text="View General Journal", font='Helvetica 8 bold', height=3, width=18, fg="white",bg="steel blue",command=four).place(x=140,y=100)
        # button_5=Button(root, text="View Trial Balance", font='Helvetica 8 bold', height=3, width=18, fg="white",bg="steel blue",command=five).place(x=280, y=100)
        # Label(root, text="Closing", font='Helvetica 12 bold', bg="powder blue").place(y=370)
        # button_6=Button(root, text="Income Statement", font='Helvetica 8 bold', height=3, width=18, fg="white",bg="steel blue",command=six).place(y=305)
        # button_61= Button(root, text="Owner Equity Statement", font='Helvetica 8 bold', height=3, width=18, fg="white",bg="steel blue", command=six_2).place(x=140, y=305)
        # button_62= Button(root, text="Balance Sheet", font='Helvetica 8 bold', height=3, width=18, fg="white",bg="steel blue", command=six_3).place(x=280, y=305)
        # Label(root, text="Others", font='Helvetica 12 bold', bg="powder blue").place(y=470)
        # button_7=Button(root, text="Refresh all accounts", font='Helvetica 8 bold', height=3, width=18, fg="white",bg="steel blue",command=seven).place(y=505)
        # button_8=Button(root, text="Close Accounts",font='Helvetica 8 bold', height= 3, width =18,fg="white",bg='steel blue',command=eight).place( y=405)
        # button_9=Button(root,text="Quit",font="Helvetica 10 bold",height=3,width=30,fg="white",bg='steel blue',command=nine).place(y=600)
        # button_10=Button(root,text="Help",font="Helvetica 8 bold",height=3,width=18,fg="white",bg='steel blue',command=ten).place(x=140,y=505)
        # button_11 = Button(root, text="View T Accounts", font="Helvetica 8 bold", height=3, width=18, fg="white", bg='steel blue',command=eleven).place(x=420, y=100)
        root.mainloop()


        print("\n"*30)
        print("Accounts Management System")
        print("1) View Accounts  ")
        print("2) Input Journal Entries ")
        print("3) Add an account")
        print("4) View General Journal")
        print("5) View trial balance")
        print("6) Statements")
        print("7) View Owner's equity statement")
        print("8) View Balance sheet")
        print("9) Refresh all accounts")

        user=input("Choose an option: ")
        while user not in ["1","2","3","4","5","6","7","8","9"]:
            print("Incorrect option")
            user = input("Choose an option :")
        if user=="1":
            self.view_accounts()
        elif user=="2":
            self.journal_entry()
        elif user=="3":
            self.add_accounts()
        elif user=="4":
            self.view_journal()
        elif user=="5":
            self.view_trial_balance()
        elif user=="6":
            inpp=input("Enter what type of statement: ")
            self.statements(inpp)
        elif user=="7":
            self.owner_equity_statement()
        elif user=="9":
            self.refresh()

    def view_accounts(self):
        root = Tk()
        root.geometry("1300x600")
        root.resizable(0, 0)
        root.title("Accounting")
        window_height = 600
        window_width = 1300
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        root.configure(background='powder blue')
        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 11))
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 13, 'bold'))
        currentMonth = datetime.now().month
        currentYear = datetime.now().year
        x = Label(root, text="All Accounts", font='Helvetica 18 bold', height=2, width=100, fg="black",bg="steel blue").pack()
        y = Label(root, text=self.company_name.title(), font='Helvetica 18 bold', height=2, width=100, fg="black",bg="powder blue").pack()
        frame = Frame(root)
        frame.pack()
        tree = ttk.Treeview(frame, columns=(1, 2, 3, 4, 5, 6), height=20, show="headings", style="mystyle.Treeview")
        tree.pack(side='left')
        tree.heading(1, text="ID")
        tree.heading(2, text="ACCOUNT TITLE")
        tree.heading(3, text="DEBIT")
        tree.heading(4, text="CREDIT")
        tree.heading(5, text="DEBIT BALANCE")
        tree.heading(6, text="CREDIT BALANCE")
        tree.column(1, width=100)
        tree.column(2, width=300)
        tree.column(3, width=200)
        tree.column(4, width=200)
        tree.column(5, width=200)
        tree.column(6, width=200)
        scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
        scroll.pack(side='right', fill='y')
        tree.configure(yscrollcommand=scroll.set)
        def back():
            root.destroy()
            self.interface()
        button_close = Button(root, text="Close", command=back, height=2, width=10, bg="steel blue",fg="black").pack()
        print("\n"*50)
        print("-------------------SHOWING ALL ACCOUNTS---------------")
        print("\n" * 3)
        print("--------------------------Asset Accounts----------------------------")
        tree.insert('', 'end', values=(" ","Asset Accounts"," "," "," "," "))
        print("|{:^5}| |{:^35}| |{:^15}| |{:^15}| |{:^15}| |{:^15}|".format("Id","Title","Debit","Credit","Debit Balance","Credit Balance"))
        for k,v in Assets.assets.items():
            print("|{:^5}| |{:^35}| |{:^15}| |{:^15}| |{:^15}| |{:^15}|".format(k ,v.title,v.debit,v.credit,v.debit_balance,v.credit_balance))
            tree.insert('', 'end', values=(k,v.title,v.debit,v.credit,v.debit_balance,v.credit_balance))
        print("")
        tree.insert('', 'end', values=(" "," "," "," "," "," ",))
        print("--------------------------Liability Accounts-------------------------")
        tree.insert('', 'end', values=(" ","Liability Accounts", " ", " ", " ", " "))
        print("|{:^5}| |{:^35}| |{:^15}| |{:^15}| |{:^15}| |{:^15}|".format("Id", "Title", "Debit", "Credit","Debit Balance", "Credit Balance"))
        for k,v in Liabilities.liabilities.items():
            print("|{:^5}| |{:^35}| |{:^15}| |{:^15}| |{:^15}| |{:^15}|".format(k ,v.title,v.debit,v.credit,v.debit_balance,v.credit_balance))
            tree.insert('', 'end', values=(k, v.title, v.debit, v.credit, v.debit_balance, v.credit_balance))
        print("")
        tree.insert('', 'end', values=(" ", " ", " ", " ", " ", " ",))
        print("--------------------------Owner Equity Accounts-------------------------")
        tree.insert('', 'end', values=(" ","Owner Equity Accounts", " ", " ", " ", " "))
        print("|{:^5}| |{:^35}| |{:^15}| |{:^15}| |{:^15}| |{:^15}|".format("Id", "Title", "Debit", "Credit","Debit Balance", "Credit Balance"))
        for k,v in Owner_Equity.owner_equity.items():
            print("|{:^5}| |{:^35}| |{:^15}| |{:^15}| |{:^15}| |{:^15}|".format(k ,v.title,v.debit,v.credit,v.debit_balance,v.credit_balance))
            tree.insert('', 'end', values=(k, v.title, v.debit, v.credit, v.debit_balance, v.credit_balance))
        print("")
        tree.insert('', 'end', values=(" ", " ", " ", " ", " ", " ",))
        print("--------------------------Expense Accounts-------------------------")
        tree.insert('', 'end', values=(" ","Expense Accounts", " ", " ", " ", " "))
        print("|{:^5}| |{:^35}| |{:^15}| |{:^15}| |{:^15}| |{:^15}|".format("Id", "Title", "Debit", "Credit","Debit Balance", "Credit Balance"))
        for k,v in Expense.expense.items():
            print("|{:^5}| |{:^35}| |{:^15}| |{:^15}| |{:^15}| |{:^15}|".format(k ,v.title,v.debit,v.credit,v.debit_balance,v.credit_balance))
            tree.insert('', 'end', values=(k, v.title, v.debit, v.credit, v.debit_balance, v.credit_balance))
        tree.insert('', 'end', values=(" ", " ", " ", " ", " ", " ",))
        print("--------------------------Revenue Accounts-------------------------")
        tree.insert('', 'end', values=(" ","Revenue Accounts"," ", " ", " ", " "))
        print("|{:^5}| |{:^35}| |{:^15}| |{:^15}| |{:^15}| |{:^15}|".format("Id", "Title", "Debit", "Credit","Debit Balance", "Credit Balance"))
        for k, v in Revenue.revenue.items():
            print("|{:^5}| |{:^35}| |{:^15}| |{:^15}| |{:^15}| |{:^15}|".format(k, v.title, v.debit, v.credit,v.debit_balance, v.credit_balance))
            tree.insert('', 'end', values=(k, v.title, v.debit, v.credit, v.debit_balance, v.credit_balance))
        tree.insert('', 'end', values=(" ", " ", " ", " ", " ", " ",))
        print("--------------------------Drawing Accounts-------------------------")
        tree.insert('', 'end', values=(" ","Drawing Accounts", " ", " ", " ", " "))
        print("|{:^5}| |{:^35}| |{:^15}| |{:^15}| |{:^15}| |{:^15}|".format("Id", "Title", "Debit", "Credit","Debit Balance", "Credit Balance"))
        for k, v in Drawing.drawing.items():
            print("|{:^5}| |{:^35}| |{:^15}| |{:^15}| |{:^15}| |{:^15}|".format(k, v.title, v.debit, v.credit,v.debit_balance, v.credit_balance))
            tree.insert('', 'end', values=(k, v.title, v.debit, v.credit, v.debit_balance, v.credit_balance))
        tree.insert('', 'end', values=(" ", " ", " ", " ", " ", " ",))
        # for k,v in Income_summary.income_summary.items():
        #     print("|{:^5}| |{:^35}| |{:^15}| |{:^15}| |{:^15}| |{:^15}|".format(k, v.title, v.debit, v.credit,v.debit_balance, v.credit_balance))
        #     tree.insert('', 'end', values=(k, v.title, v.debit, v.credit, v.debit_balance, v.credit_balance))
        root.mainloop()
        user=input("Enter m to go back to main menu: ")
        if user.lower()=="m":
            self.interface()

    def get_data(self):
        conn=sqlite3.connect("accounts_db.db")
        a=  conn.cursor()
        l=  conn.cursor()
        o_e=conn.cursor()
        ent=conn.cursor()
        exp=conn.cursor()
        j=  conn.cursor()
        r=  conn.cursor()
        d=  conn.cursor()
        i=  conn.cursor()
        a.execute("Select * from Assets")
        l.execute("Select * from Liability")
        o_e.execute("Select * from Owner_Equity")
        ent.execute("Select * from Entries")
        exp.execute("Select * from Expense")
        j.execute("Select * from Journal")
        r.execute("Select * from Revenue")
        d.execute("Select * from Drawings")
        i.execute("Select * from Income_Summary")
        for all in a.fetchall():
            print(all,end=" ")
            Assets(all[0],all[1],all[2],all[3],all[4],all[5])
        for all in l.fetchall():
            print(all,end=" ")
            Liabilities(all[0],all[1],all[2],all[3],all[4],all[5])
        for all in o_e.fetchall():
            print(all,end=" ")
            Owner_Equity(all[0],all[1],all[2],all[3],all[4],all[5])
        for all in ent.fetchall():
            print(all,end=" ")
            Entries(all[0],all[1],all[2],all[3],all[4])
        for all in exp.fetchall():
            print(all,end=" ")
            Expense(all[0],all[1],all[2],all[3],all[4],all[5])
        for all in j.fetchall():
            print(all,end=" ")
            Journal(all[0],all[1],all[2])
        for all in r.fetchall():
            print(all,end=" ")
            Revenue(all[0],all[1],all[2],all[3],all[4],all[5])
        for all in d.fetchall():
            print(all,end=" ")
            Drawing(all[0],all[1],all[2],all[3],all[4],all[5])
        for all in i.fetchall():
            print(all, end=" ")
            Income_summary(all[0], all[1], all[2], all[3], all[4], all[5])


    def journal_entry(self):

        self.credit = 0

        self.debit = 0
        self.dr_list=[]
        self.cr_list=[]
        self.dr_acc_list = {}
        self.cr_acc_list = {}
        def Insert():
            global data_tkinter
            data_tkinter = [account_title.get(), dr_cr.get(), amount.get()]
            if amount.get().isdigit()==False:
                messagebox.showerror("Error", "Amount cannot contain alphabets, please enter digits only!")
                root.destroy()
                self.journal_entry()

            for all in data_tkinter:
                print(all, end=" : ")
            tree.insert('', tk.END, values=(data_tkinter))

            self.dr_list = []
            self.cr_list = []

            # while inpp.lower()=="y":
            y = Entries.create_object(data_tkinter[1], data_tkinter[2], data_tkinter[0])
            conn = sqlite3.connect("accounts_db.db")
            c = conn.cursor()
            x = list(y.journal_id)
            z = x[1] + x[2] + x[3]
            z = int(z)
            z += 1
            if len(str(z)) == 1:
                z = '0' + '0' + str(z)
            elif len(str(z)) == 2:
                z = '0' + str(z)
            f = x[0] + str(z)
            c.execute("INSERT into Entries VALUES(?,?,?,?,?)", (y.amount_type, y.id, y.amount, str(f), y.account_id))
            conn.commit()
            if data_tkinter[1].lower() == "debit":
                obj = list(data_tkinter[0])
                if obj[0] == "A":
                    original = int(Assets.assets[y.account_id].debit)
                    add_val = int(y.amount) + original
                    Assets.assets[y.account_id].update_debit(add_val)
                    self.debit += int(y.amount)
                    self.dr_list.append(y.id)
                    self.dr_acc_list[y.account_id] = y.amount
                    print("Value appended")

                elif obj[0] == "L":
                    original = int(Liabilities.liabilities[y.account_id].debit)
                    add_val = int(y.amount) + original
                    Liabilities.liabilities[y.account_id].update_debit(add_val)
                    self.debit += int(y.amount)
                    self.dr_list.append(y.id)
                    self.dr_acc_list[y.account_id] = y.amount

                elif obj[0] == "O":
                    original = int(Owner_Equity.owner_equity[y.account_id].debit)
                    add_val = int(y.amount) + original
                    Owner_Equity.owner_equity[y.account_id].update_debit(add_val)
                    self.debit += int(y.amount)
                    self.dr_list.append(y.id)
                    self.dr_acc_list[y.account_id] = y.amount

                elif obj[0] == "E":
                    original = int(Expense.expense[y.account_id].debit)
                    add_val = int(y.amount) + original
                    Expense.expense[y.account_id].update_debit(add_val)
                    self.debit += int(y.amount)
                    self.dr_list.append(y.id)
                    self.dr_acc_list[y.account_id] = y.amount

                elif obj[0] == "R":
                    original = int(Revenue.revenue[y.account_id].debit)
                    add_val = int(y.amount) + original
                    Revenue.revenue[y.account_id].update_debit(add_val)
                    self.debit += int(y.amount)
                    self.dr_list.append(y.id)
                    self.dr_acc_list[y.account_id] = y.amount

                elif obj[0] == "D":

                    original = int(Drawing.drawing[y.account_id].debit)
                    add_val = int(y.amount) + original
                    Drawing.drawing[y.account_id].update_debit(add_val)
                    self.debit += int(y.amount)
                    self.dr_list.append(y.id)
                    self.dr_acc_list[y.account_id] = y.amount

            elif data_tkinter[1].lower() == "credit":
                obj = list(data_tkinter[0])
                if obj[0] == "A":
                    original = int(Assets.assets[y.account_id].credit)
                    add_val = int(y.amount) + original
                    Assets.assets[y.account_id].update_credit(add_val)
                    self.credit += int(y.amount)
                    self.cr_list.append(y.id)
                    self.cr_acc_list[y.account_id] = y.amount

                elif obj[0] == "L":
                    original = int(Liabilities.liabilities[y.account_id].credit)
                    add_val = int(y.amount) + original
                    Liabilities.liabilities[y.account_id].update_credit(add_val)
                    self.credit += int(y.amount)
                    self.cr_list.append(y.id)
                    self.cr_acc_list[y.account_id] = y.amount

                elif obj[0] == "O":
                    original = int(Owner_Equity.owner_equity[y.account_id].credit)
                    add_val = int(y.amount) + original
                    Owner_Equity.owner_equity[y.account_id].update_credit(add_val)
                    self.credit += int(y.amount)
                    self.cr_list.append(y.id)
                    self.cr_acc_list[y.account_id] = y.amount

                elif obj[0] == "E":
                    original = int(Expense.expense[y.account_id].credit)
                    add_val = int(y.amount) + original
                    Expense.expense[y.account_id].update_credit(add_val)
                    self.credit += int(y.amount)
                    self.cr_list.append(y.id)
                    self.cr_acc_list[y.account_id] = y.amount

                if obj[0] == "R":
                    original = int(Revenue.revenue[y.account_id].credit)
                    add_val = int(y.amount) + original
                    Revenue.revenue[y.account_id].update_credit(add_val)
                    self.credit += int(y.amount)
                    self.cr_list.append(y.id)
                    self.cr_acc_list[y.account_id] = y.amount

                if obj[0] == "D":
                    original = int(Drawing.drawing[y.account_id].credit)
                    add_val = int(y.amount) + original
                    Drawing.drawing[y.account_id].update_credit(add_val)
                    self.credit += int(y.amount)
                    self.cr_list.append(y.id)
                    self.cr_acc_list[y.account_id] = y.amount
        def confirmation():
            global data_journal
            data_journal = [cal.selection_get(), description.get()]
            global x
            x = Journal.create_object(data_journal[0], data_journal[1])
            conn = sqlite3.connect("accounts_db.db")
            c = conn.cursor()
            c.execute("INSERT into Journal VALUES(?,?,?)", (x.id, x.date, x.description))
            conn.commit()
            print(self.debit)
            print(self.credit)
            if self.credit==self.debit:
                messagebox.showinfo("Success", "Your entries have been recorded successfully.")
                root.destroy()
                print("Entries successfully recorded")
                self.journal_entry()
            else:
                for zz in self.dr_list:
                    del Entries.entries[zz]
                    conn = sqlite3.connect("accounts_db.db")
                    c = conn.cursor()
                    c.execute(("DELETE from Entries where id = ? "),(zz,))
                    conn.commit()
                    conn.close()
                for gg in self.cr_list:
                    del Entries.entries[gg]
                    conn = sqlite3.connect("accounts_db.db")
                    c = conn.cursor()
                    c.execute(("DELETE from Entries where id = ? "), (gg,))
                    conn.commit()
                    conn.close()
                conn = sqlite3.connect("accounts_db.db")
                c = conn.cursor()
                c.execute(("DELETE from Journal where id = ? "), (x.id,))
                conn.commit()
                conn.close()
                del Journal.journal[x.id]
                print(self.dr_acc_list)
                print(self.cr_acc_list)
                for k,v in self.dr_acc_list.items():
                    print(k[0])
                    print(v)
                    if k[0] == "A":
                        print("Came here")
                        original = int(Assets.assets[k].debit)
                        sub_val = original - int(v)
                        Assets.assets[k].update_debit(sub_val)
                        print("Subtracted the value successfully")
                    elif k[0] == "L":
                        original = int(Liabilities.liabilities[k].debit)
                        sub_val = original - int(v)
                        Liabilities.liabilities[k].update_debit(sub_val)
                    elif k[0] == "O":
                        original = int(Owner_Equity.owner_equity[k].debit)
                        sub_val = original - int(v)
                        Owner_Equity.owner_equity[k].update_debit(sub_val)
                    elif k[0] == "E":
                        original = int(Expense.expense[k].debit)
                        sub_val = original - int(v)
                        Expense.expense[k].update_debit(sub_val)
                    elif k[0] == "R":
                        original = int(Revenue.revenue[k].debit)
                        sub_val = original - int(v)
                        Revenue.revenue[k].update_debit(sub_val)
                    elif k[0] == "D":
                        original = int(Drawing.drawing[k].debit)
                        sub_val = original - int(k)
                        Drawing.drawing[k].update_debit(sub_val)
                for k,v in self.cr_acc_list.items():
                    if k[0] == "A":
                        original = int(Assets.assets[k].credit)
                        sub_val = original - int(v)
                        Assets.assets[k].update_credit(sub_val)
                    elif k[0] == "L":
                        original = int(Liabilities.liabilities[k].credit)
                        sub_val = original - int(v)
                        Liabilities.liabilities[k].update_credit(sub_val)
                    elif k[0] == "O":
                        original = int(Owner_Equity.owner_equity[k].credit)
                        sub_val = original - int(v)
                        Owner_Equity.owner_equity[k].update_credit(sub_val)
                    elif k[0] == "E":
                        original = int(Expense.expense[k].credit)
                        sub_val = original - int(v)
                        Expense.expense[k].update_credit(sub_val)
                    if k[0] == "R":
                        original = int(Revenue.revenue[k].credit)
                        sub_val = original - int(v)
                        Revenue.revenue[k].update_credit(sub_val)
                    if k[0] == "D":
                        original = int(Drawing.drawing[k].credit)
                        sub_val = original - (v)
                        Drawing.drawing[k].update_credit(sub_val)

                print("Dr and Cr not balance, hence values cannot be added.",self.debit,self.credit)
                messagebox.showerror("Error", "Debit and Credit values are not balanced.")
                root.destroy()
                self.journal_entry()

        # def Insert_2():
        #     global data_tkinter_2
        #     data_tkinter_2=[description.get(),date_tkinter.get()]


        root = tk.Tk()
        root.geometry("600x600")
        window_height = 600
        window_width = 1200
        root.resizable(0,0)
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        root.configure(background='powder blue')
        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 11))
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 13, 'bold'))
        x = Label(root, text="Input Journal Entries", font='Helvetica 18 bold', height=2, width=100, fg="black",bg="steel blue").pack()
        Label(root, text="Select Journal Date",font='Helvetica 12 bold',bg="powder blue").place(x=850,y=100)
        cal = Calendar(root,font="Helvetica 10 bold", selectmode='day',cursor="hand1", year=2019, month=12, day=5)
        cal.place(x=850,y=130)
        frame = Frame(root)
        frame.place(y=100)
        tree = ttk.Treeview(frame, columns=(1, 2, 3), height=10, show="headings", style="mystyle.Treeview")
        tree.pack(side='left')
        tree.heading(1, text="Account ID")
        tree.heading(2, text="Debit/Credit")
        tree.heading(3, text="Amount")
        tree.column(1,width=100)
        tree.column(2,width=150)
        tree.column(3,width=150)
        scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
        scroll.pack(side='right', fill='y')
        tree.configure(yscrollcommand=scroll.set)

        frame_2 = Frame(root)
        frame_2.place(x=450,y=100)
        tree_2 = ttk.Treeview(frame_2, columns=(1, 2), height=10, show="headings", style="mystyle.Treeview")
        tree_2.pack(side='left')
        tree_2.heading(1, text="Account ID")
        tree_2.heading(2, text="Account Title")
        tree_2.column(1, width=100)
        tree_2.column(2, width=250)
        scroll = ttk.Scrollbar(frame_2, orient="vertical", command=tree.yview)
        scroll.pack(side='right', fill='y')
        tree.configure(yscrollcommand=scroll.set)
        #
        # def back():
        #     root.destroy()
        #     self.interface()
        #
        # button_close = Button(root, text="Close", command=back, height=2, width=10, bg="steel blue", fg="black").pack()

        for k, v in Assets.assets.items():
            tree_2.insert('', 'end', values=(k, v.title))
        tree_2.insert('', 'end', values=(" ", " ", " ", " ", " ", " ",))
        for k, v in Liabilities.liabilities.items():
            tree_2.insert('', 'end', values=(k, v.title))
        tree_2.insert('', 'end', values=(" ", " ", " ", " ", " ", " ",))
        for k, v in Owner_Equity.owner_equity.items():
            tree_2.insert('', 'end', values=(k, v.title))
        tree_2.insert('', 'end', values=(" ", " ", " ", " ", " ", " ",))
        for k, v in Expense.expense.items():
            tree_2.insert('', 'end', values=(k, v.title))
        tree_2.insert('', 'end', values=(" ", " ", " ", " ", " ", " ",))
        for k, v in Revenue.revenue.items():
            tree_2.insert('', 'end', values=(k, v.title))
        tree_2.insert('', 'end', values=(" ", " ", " ", " ", " ", " ",))
        for k, v in Drawing.drawing.items():
            tree_2.insert('', 'end', values=(k, v.title))
        tree_2.insert('', 'end', values=(" ", " ", " ", " ", " ", " ",))

        description= tk.StringVar()
        Label(root, text="Enter Journal Description", font='Helvetica 12 bold', bg="powder blue").place(x=450,y=340)
        e4 = tk.Entry(root, textvariable=description, fg="black",width=50).place(x=450, y=380,height=50)
        account_title = tk.StringVar()
        choices = []
        for k,v in Assets.assets.items():
            choices.append(k)
        for k,v in Liabilities.liabilities.items():
            choices.append(k)
        for k,v in Owner_Equity.owner_equity.items():
            choices.append(k)
        for k,v in Expense.expense.items():
            choices.append(k)
        for k,v in Revenue.revenue.items():
            choices.append(k)
        for k,v in Drawing.drawing.items():
            choices.append(k)

        if choices!=[]:
            account_title.set(choices[0])  # set the default option
        Label(root, text="Choose Account",font='Helvetica 12 bold',bg="powder blue").place(y=340)
        popupMenu = OptionMenu(root, account_title, *choices).place(x=160,y=340)
        # # on change dropdown value
        # def change_dropdown(*args):
        #     global dropdown
        #     dropdown = str(account_title.get())
        #     return dropdown
        # # link function to change dropdown
        # # account_title.trace('w', change_dropdown)
        # print(change_dropdown())
        choices_2=["Debit","Credit"]
        dr_cr = tk.StringVar()
        dr_cr.set(choices_2[0])
        amount = tk.StringVar()
        Label(root, text="Choose Value Type",font='Helvetica 12 bold',bg="powder blue").place(y=380)
        popupMenu = OptionMenu(root, dr_cr, *choices_2).place(x=160,y=380)
        Label(root,text="Enter Amount",font='Helvetica 12 bold',bg="powder blue").place(y=420)
        e3 = tk.Entry(root, textvariable=amount,fg="black").place(x=160,y=420)
        b1 = tk.Button(text="Add Entry", command=Insert,height=2, width=10,font='Helvetica 12 bold', bg="steel blue", fg="black")
        b1.place(x=160,y=450)
        b2= tk.Button(text="Confirm Journal Entry",command= confirmation,height=2, width=30,font='Helvetica 12 bold', bg="steel blue", fg="black")
        b2.place(x=780,y=550)
        def back_main():
            root.destroy()
            self.interface()
        b2 = tk.Button(text="Back to main", command=back_main, height=2, width=30, font='Helvetica 12 bold',bg="steel blue", fg="black")
        b2.place(x=450,y=550)
        root.mainloop()


        #-------------------------------------------------------------------
        print("\n"*30)
        # inp=input("Do you want to create a new journal? Y/N: ")
        # while inp.lower() not in ["y","n"]:
        #     inp = input("Do you want to create a new journal? Y/N: ")
        # if inp.lower()=="y":
        x=Journal.create_object(data_tkinter[0],data_tkinter[1])
        conn=sqlite3.connect("accounts_db.db")
        c=conn.cursor()
        c.execute("INSERT into Journal VALUES(?,?,?)",(x.id,x.date,x.description))
        conn.commit()
        # inpp=input("Add entries to this journal? Y/N: ")
        debit = 0
        credit = 0
        self.dr_list=[]
        self.cr_list=[]
        self.dr_acc_list={}
        self.cr_acc_list={}
        # while inpp.lower()=="y":
        y=Entries.create_object(data_tkinter[1],data_tkinter[2],data_tkinter[0])
        conn = sqlite3.connect("accounts_db.db")
        c = conn.cursor()
        c.execute("INSERT into Entries VALUES(?,?,?,?,?)", (y.amount_type,y.id,y.amount,x.id,y.account_id))
        conn.commit()
        if data_tkinter[1].lower()=="dr":
            obj=list(data_tkinter[1])
            if obj[0]=="A":
                original=int(Assets.assets[y.account_id].debit)
                add_val=int(y.amount)+original
                Assets.assets[y.account_id].update_debit(add_val)
                debit +=int(y.amount)
                self.dr_list.append(y.id)
                self.dr_acc_list[y.account_id]=y.amount

            elif obj[0]=="L":
                original=int(Liabilities.liabilities[y.account_id].debit)
                add_val=int(y.amount)+original
                Liabilities.liabilities[y.account_id].update_debit(add_val)
                debit += int(y.amount)
                self.dr_list.append(y.id)
                self.dr_acc_list[y.account_id] = y.amount

            elif obj[0]=="O":
                original=int(Owner_Equity.owner_equity[y.account_id].debit)
                add_val=int(y.amount)+original
                Owner_Equity.owner_equity[y.account_id].update_debit(add_val)
                debit += int(y.amount)
                self.dr_list.append(y.id)
                self.dr_acc_list[y.account_id] = y.amount

            elif obj[0]=="E":
                original=int(Expense.expense[y.account_id].debit)
                add_val=int(y.amount)+original
                Expense.expense[y.account_id].update_debit(add_val)
                debit += int(y.amount)
                self.dr_list.append(y.id)
                self.dr_acc_list[y.account_id] = y.amount

            elif obj[0]=="R":
                original=int(Revenue.revenue[y.account_id].debit)
                add_val=int(y.amount)+original
                Revenue.revenue[y.account_id].update_debit(add_val)
                debit += int(y.amount)
                self.dr_list.append(y.id)
                self.dr_acc_list[y.account_id] = y.amount

            elif obj[0]=="D":
                original=int(Drawing.drawing[y.account_id].debit)
                add_val=int(y.amount)+original
                Drawing.drawing[y.account_id].update_debit(add_val)
                debit += int(y.amount)
                self.dr_list.append(y.id)
                self.dr_acc_list[y.account_id] = y.amount

        elif data_tkinter[1].lower()=="cr":
            obj=list(data_tkinter[1])
            if obj[0]=="A":
                original=int(Assets.assets[y.account_id].credit)
                add_val=int(y.amount)+original
                Assets.assets[y.account_id].update_credit(add_val)
                credit += int(y.amount)
                self.cr_list.append(y.id)
                self.cr_acc_list[y.account_id] = y.amount

            elif obj[0]=="L":
                original=int(Liabilities.liabilities[y.account_id].credit)
                add_val=int(y.amount)+original
                Liabilities.liabilities[y.account_id].update_credit(add_val)
                credit += int(y.amount)
                self.cr_list.append(y.id)
                self.cr_acc_list[y.account_id] = y.amount

            elif obj[0]=="O":
                original=int(Owner_Equity.owner_equity[y.account_id].credit)
                add_val=int(y.amount)+original
                Owner_Equity.owner_equity[y.account_id].update_credit(add_val)
                credit += int(y.amount)
                self.cr_list.append(y.id)
                self.cr_acc_list[y.account_id] = y.amount

            elif obj[0]=="E":
                original=int(Expense.expense[y.account_id].credit)
                add_val=int(y.amount)+original
                Expense.expense[y.account_id].update_credit(add_val)
                credit += int(y.amount)
                self.cr_list.append(y.id)
                self.cr_acc_list[y.account_id] = y.amount

            if obj[0]=="R":
                original=int(Revenue.revenue[y.account_id].credit)
                add_val=int(y.amount)+original
                Revenue.revenue[y.account_id].update_credit(add_val)
                credit += int(y.amount)
                self.cr_list.append(y.id)
                self.cr_acc_list[y.account_id] = y.amount

            if obj[0]=="D":
                original=int(Drawing.drawing[y.account_id].credit)
                add_val=int(y.amount)+original
                Drawing.drawing[y.account_id].update_credit(add_val)
                credit += int(y.amount)
                self.cr_list.append(y.id)
                self.cr_acc_list[y.account_id] = y.amount

            # inpp = input("Add more entries to this journal? Y/N: ")
            # if inpp.lower()=="n":
            if credit==debit:
                messagebox.showinfo("Information", "Informative message")
                print("Entries successfully recorded")
                self.interface()
            else:
                for zz in self.dr_list:
                    del Entries.entries[zz]
                    conn = sqlite3.connect("accounts_db.db")
                    c = conn.cursor()
                    c.execute(("DELETE from Entries where id = ? "),(zz,))
                    conn.commit()
                    conn.close()
                for gg in self.cr_list:
                    del Entries.entries[gg]
                    conn = sqlite3.connect("accounts_db.db")
                    c = conn.cursor()
                    c.execute(("DELETE from Entries where id = ? "), (gg,))
                    conn.commit()
                    conn.close()
                conn = sqlite3.connect("accounts_db.db")
                c = conn.cursor()
                c.execute(("DELETE from Journal where id = ? "), (x.id,))
                conn.commit()
                conn.close()
                del Journal.journal[x.id]
                print(self.dr_acc_list)
                print(self.cr_acc_list)
                for k,v in self.dr_acc_list.items():
                    print(k[0])
                    if k[0] == "A":
                        original = int(Assets.assets[k].debit)
                        sub_val = original - int(v)
                        Assets.assets[k].update_debit(sub_val)
                    elif k[0] == "L":
                        original = int(Liabilities.liabilities[k].debit)
                        sub_val = original - int(v)
                        Liabilities.liabilities[k].update_debit(sub_val)
                    elif k[0] == "O":
                        original = int(Owner_Equity.owner_equity[k].debit)
                        sub_val = original - int(v)
                        Owner_Equity.owner_equity[k].update_debit(sub_val)
                    elif k[0] == "E":
                        original = int(Expense.expense[k].debit)
                        sub_val = original - int(v)
                        Expense.expense[k].update_debit(sub_val)
                    elif k[0] == "R":
                        original = int(Revenue.revenue[k].debit)
                        sub_val = original - int(v)
                        Revenue.revenue[k].update_debit(sub_val)
                    elif k[0] == "D":
                        original = int(Drawing.drawing[k].debit)
                        sub_val = original - int(k)
                        Drawing.drawing[k].update_debit(sub_val)
                for k,v in self.cr_acc_list.items():
                    if k[0] == "A":
                        original = int(Assets.assets[k].credit)
                        sub_val = original - int(v)
                        Assets.assets[k].update_credit(sub_val)
                    elif k[0] == "L":
                        original = int(Liabilities.liabilities[k].credit)
                        sub_val = original - int(v)
                        Liabilities.liabilities[k].update_credit(sub_val)
                    elif k[0] == "O":
                        original = int(Owner_Equity.owner_equity[k].credit)
                        sub_val = original - int(v)
                        Owner_Equity.owner_equity[k].update_credit(sub_val)
                    elif k[0] == "E":
                        original = int(Expense.expense[k].credit)
                        sub_val = original - int(v)
                        Expense.expense[k].update_credit(sub_val)
                    if k[0] == "R":
                        original = int(Revenue.revenue[k].credit)
                        sub_val = original - int(v)
                        Revenue.revenue[k].update_credit(sub_val)
                    if k[0] == "D":
                        original = int(Drawing.drawing[k].credit)
                        sub_val = original - (v)
                        Drawing.drawing[k].update_credit(sub_val)

                print("Dr and Cr not balance, hence values cannot be added.",self.debit,self.credit)
                messagebox.showerror("Error", "Error message")
                self.interface()
#                         Delete the values that were entered.
    def view_journal(self):
        self.get_data()
        root = Tk()
        root.geometry("1300x600")
        root.resizable(0, 0)
        root.title("Accounting")
        window_height = 700
        window_width = 1350
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        root.configure(background='powder blue')
        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 11))
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 13, 'bold'))
        currentMonth = datetime.now().month
        currentYear = datetime.now().year
        x = Label(root, text="General Journal", font='Helvetica 18 bold', height=2, width=100, fg="black",bg="steel blue").pack()
        y= Label(root, text=self.company_name.title(), font='Helvetica 18 bold', height=2, width=100, fg="black",bg="powder blue").pack()
        frame = Frame(root)
        frame.pack()
        tree = ttk.Treeview(frame, columns=(1, 2, 3, 4, 5, 6, 7), height=20, show="headings", style="mystyle.Treeview")
        tree.pack(side='left')
        tree.heading(1, text="ID")
        tree.heading(2, text="DESCRIPTION")
        tree.heading(3, text="DATE")
        tree.heading(4, text="DEBIT")
        tree.heading(5, text="CREDIT")
        tree.heading(6, text="ENTRY ID")
        tree.heading(7, text="ACCOUNT NAME")
        tree.column(1, width=100)
        tree.column(2, width=200)
        tree.column(3, width=100)
        tree.column(4, width=100)
        tree.column(5, width=100)
        tree.column(6, width=100)
        tree.column(7, width=200)
        scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
        scroll.pack(side='right', fill='y')
        tree.configure(yscrollcommand=scroll.set)

        def back():
            root.destroy()
            self.interface()

        button_close = Button(root, text="Close", command=back, height=2, width=10, bg="steel blue", fg="black").pack()

        def grab():
            im1 = PIL.Image.open(r"C:\Users\DeLL\Desktop\111.PNG")
            im2 = ImageGrab.grab(bbox=(100, 60, 1300, 620))
            im2.show()
        # photo = PhotoImage(file=r"C:\Users\DeLL\Desktop\screen.PNG")
        # here, image option is used to
        # set image on button
        # Button(root, image=photo, width=77, command=grab).pack()
        print(" ")
        print("-------------------------------------------General Journal-------------------------------------------")
        print("||{:^10}| |{:^25}| |{:^15}| |{:>15}| |{:>15}| |{:^10}| |{:^20}||".format("ID","Description","Date","Debit","Credit","Entry Id","Account Name"))
        print(" ")
        for k,v in Journal.journal.items():
            print("||{:^10}| |{:^25}| |{:^15}| |{:>15}| |{:>15}| |{:^10}| |{:^20}||".format(k,v.description,v.date," "," "," "," "))
            tree.insert('', 'end', values=(k, v.description,v.date," "," "," "," "))
            for a,b in Entries.entries.items():
                if b.journal_id==k:
                    if b.amount_type in ["dr","Debit"]:
                        if b.account_id[0]=="A":
                            print("||{:^10}| |{:^25}| |{:^15}| |{:>15}| |{:>15}| |{:^10}| |{:^20}||".format(" "," "," ",b.amount," ",a,Assets.assets[b.account_id].title))
                            tree.insert('', 'end', values=(" "," "," ",b.amount, " ",a,Assets.assets[b.account_id].title))
                        elif b.account_id[0]=="L":
                            print("||{:^10}| |{:^25}| |{:^15}| |{:>15}| |{:>15}| |{:^10}| |{:^20}||".format(" ", " ", " ",b.amount, " ", a,Liabilities.liabilities[b.account_id].title))
                            tree.insert('', 'end', values=(" "," "," ",b.amount, " ",a,Liabilities.liabilities[b.account_id].title))
                        elif b.account_id[0]=="O":
                            print("||{:^10}| |{:^25}| |{:^15}| |{:>15}| |{:>15}| |{:^10}| |{:^20}||".format(" ", " ", " ",b.amount, " ",a,Owner_Equity.owner_equity[b.account_id].title))
                            tree.insert('', 'end',values=(" ", " ", " ", b.amount, " ", a, Owner_Equity.owner_equity[b.account_id].title))
                        elif b.account_id[0]=="E":
                            print("||{:^10}| |{:^25}| |{:^15}| |{:>15}| |{:>15}| |{:^10}| |{:^20}||".format(" ", " ", " ",b.amount, " ",a,Expense.expense[b.account_id].title))
                            tree.insert('', 'end',values=(" ", " ", " ", b.amount, " ", a,Expense.expense[b.account_id].title))
                        elif b.account_id[0]=="R":
                            print("||{:^10}| |{:^25}| |{:^15}| |{:>15}| |{:>15}| |{:^10}| |{:^20}||".format(" ", " ", " ",b.amount, " ",a,Revenue.revenue[b.account_id].title))
                            tree.insert('', 'end',values=(" ", " ", " ", b.amount, " ", a, Revenue.revenue[b.account_id].title))
                        elif b.account_id[0]=="D":
                            print("||{:^10}| |{:^25}| |{:^15}| |{:>15}| |{:>15}| |{:^10}| |{:^20}||".format(" ", " ", " ",b.amount, " ",a,Drawing.drawing[b.account_id].title))
                            tree.insert('', 'end',values=(" ", " ", " ", b.amount, " ", a, Drawing.drawing[b.account_id].title))
                    elif b.amount_type in ["cr","Credit"]:
                        if b.account_id[0]=="A":
                            print("||{:^10}| |{:^25}| |{:^15}| |{:>15}| |{:>15}| |{:^10}| |{:^20}||".format(" ", " ", " "," ",b.amount, a,Assets.assets[b.account_id].title))
                            tree.insert('', 'end',values=(" ", " ", " "," ",b.amount, a, Assets.assets[b.account_id].title))
                        elif b.account_id[0]=="L":
                            print("||{:^10}| |{:^25}| |{:^15}| |{:>15}| |{:>15}| |{:^10}| |{:^20}||".format(" ", " ", " "," ", b.amount,a,Liabilities.liabilities[b.account_id].title))
                            tree.insert('', 'end',values=(" ", " ", " ", " ", b.amount, a, Liabilities.liabilities[b.account_id].title))
                        elif b.account_id[0]=="O":
                            print("||{:^10}| |{:^25}| |{:^15}| |{:>15}| |{:>15}| |{:^10}| |{:^20}||".format(" ", " ", " "," ", b.amount,a,Owner_Equity.owner_equity[b.account_id].title))
                            tree.insert('', 'end',values=(" ", " ", " ", " ", b.amount, a,Owner_Equity.owner_equity[b.account_id].title))
                        elif b.account_id[0]=="E":
                            print("||{:^10}| |{:^25}| |{:^15}| |{:>15}| |{:>15}| |{:^10}| |{:^20}||".format(" ", " ", " "," ", b.amount,a,Expense.expense[b.account_id].title))
                            tree.insert('', 'end',values=(" ", " ", " ", " ", b.amount, a, Expense.expense[b.account_id].title))
                        elif b.account_id[0]=="R":
                            print("||{:^10}| |{:^25}| |{:^15}| |{:>15}| |{:>15}| |{:^10}| |{:^20}||".format(" ", " ", " "," ", b.amount,a,Revenue.revenue[b.account_id].title))
                            tree.insert('', 'end',values=(" ", " ", " ", " ", b.amount, a, Revenue.revenue[b.account_id].title))
                        elif b.account_id[0]=="D":
                            print("||{:^10}| |{:^25}| |{:^15}| |{:>15}| |{:>15}| |{:^10}| |{:^20}||".format(" ", " ", " "," ", b.amount,a,Drawing.drawing[b.account_id].title))
                            tree.insert('', 'end',values=(" ", " ", " ", " ", b.amount, a, Drawing.drawing[b.account_id].title))
        root.mainloop()
        user=input("Enter m to go back to main menu: ")
        if user.lower()=="m":
            self.interface()

    def add_accounts(self):
        root = Tk()
        root.geometry("1300x600")
        root.resizable(0, 0)
        root.title("Accounting")
        window_height = 600
        window_width = 900
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        root.configure(background='powder blue')
        style = ttk.Style()
        x = Label(root, text="Add Account", font='Helvetica 18 bold', height=2, width=70, fg="black",bg="steel blue").pack()
        def insert():
            inp=account_title.get()
            account=account_type.get()
            # self.acc_list.append(account)
            if inp.lower() == "asset":
                x = Assets.create_object(account.title())
                conn = sqlite3.connect("accounts_db.db")
                c = conn.cursor()
                c.execute(("INSERT into Assets VALUES(?,?,?,?,?,?)"),(x.id, x.title, x.debit, x.credit, x.debit_balance, x.credit_balance))
                conn.commit()
                print("Added")
            elif inp.lower() == "liability":
                x = Liabilities.create_object(account.title())
                conn = sqlite3.connect("accounts_db.db")
                c = conn.cursor()
                c.execute(("INSERT into Liability VALUES(?,?,?,?,?,?)"),
                          (x.id, x.title, x.debit, x.credit, x.debit_balance, x.credit_balance))
                conn.commit()
            elif inp.lower() == "owner equity":
                x = Owner_Equity.create_object(account.title())
                conn = sqlite3.connect("accounts_db.db")
                c = conn.cursor()
                c.execute(("INSERT into Owner_Equity VALUES(?,?,?,?,?,?)"),
                          (x.id, x.title, x.debit, x.credit, x.debit_balance, x.credit_balance))
                conn.commit()
            elif inp.lower() == "expense":
                x = Expense.create_object(account.title())
                conn = sqlite3.connect("accounts_db.db")
                c = conn.cursor()
                c.execute(("INSERT into Expense VALUES(?,?,?,?,?,?)"),
                          (x.id, x.title, x.debit, x.credit, x.debit_balance, x.credit_balance))
                conn.commit()
            elif inp.lower() == "revenue":
                x = Revenue.create_object(account.title())
                conn = sqlite3.connect("accounts_db.db")
                c = conn.cursor()
                c.execute(("INSERT into Revenue VALUES(?,?,?,?,?,?)"),
                          (x.id, x.title, x.debit, x.credit, x.debit_balance, x.credit_balance))
                conn.commit()
            elif inp.lower() == "drawing":
                x = Drawing.create_object(account.title())
                conn = sqlite3.connect("accounts_db.db")
                c = conn.cursor()
                c.execute(("INSERT into Drawings VALUES(?,?,?,?,?,?)"),
                          (x.id, x.title, x.debit, x.credit, x.debit_balance, x.credit_balance))
                conn.commit()
            elif inp.lower() == "income summary":
                x = Income_summary.create_object(account.title())
                conn = sqlite3.connect("accounts_db.db")
                c = conn.cursor()
                c.execute(("INSERT into Income_Summary VALUES(?,?,?,?,?,?)"),
                          (x.id, x.title, x.debit, x.credit, x.debit_balance, x.credit_balance))
            root.destroy()
            self.add_accounts()

        account_title = tk.StringVar()
        account_type= tk.StringVar()
        Label(root, text="Enter Account title", font='Helvetica 12 bold', bg="powder blue").place(x=500,y=100)
        e4 = tk.Entry(root, textvariable=account_type, fg="black", width=50).place(x=500,y=130)
        print("\n"*30)
        # inp=input("Please enter the account type you want to add: ")
        choices=["Asset","Liability","Owner Equity","Expense","Revenue","Drawing"]
        account_title.set(choices[0])  # set the default option
        Label(root, text="Choose Account Type", font='Helvetica 12 bold', bg="powder blue").place(x=500,y=160)
        popupMenu = OptionMenu(root, account_title, *choices).place(x=500,y=190)
        def back():
            root.destroy()
            self.interface()
        button_add= Button(root, text="Add", command=insert, height=2, width=10, bg="steel blue", fg="black").place(x=500,y=250)
        frame = Frame(root)
        frame.place(y=80)
        tree = ttk.Treeview(frame, columns=(1, 2), height=20, show="headings", style="mystyle.Treeview")
        tree.pack(side='left')
        tree.heading(1, text="ID")
        tree.heading(2, text="ACCOUNT TITLE")
        tree.column(1, width=100)
        tree.column(2, width=300)
        scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
        scroll.pack(side='right', fill='y')
        tree.configure(yscrollcommand=scroll.set)
        tree.insert('', 'end', values=(" ", "Asset Accounts"))
        for k, v in Assets.assets.items():
            tree.insert('', 'end', values=(k, v.title))
        print("")
        tree.insert('', 'end', values=(" ", " ", " ", " ", " ", " ",))

        tree.insert('', 'end', values=(" ", "Liability Accounts", " ", " ", " ", " "))
        for k, v in Liabilities.liabilities.items():
            tree.insert('', 'end', values=(k, v.title))
        print("")
        tree.insert('', 'end', values=(" ", " ", " ", " ", " ", " ",))
        tree.insert('', 'end', values=(" ", "Owner Equity Accounts", " ", " ", " ", " "))
        for k, v in Owner_Equity.owner_equity.items():
            tree.insert('', 'end', values=(k, v.title))
        print("")
        tree.insert('', 'end', values=(" ", " ", " ", " ", " ", " ",))
        print("--------------------------Expense Accounts-------------------------")
        tree.insert('', 'end', values=(" ", "Expense Accounts", " ", " ", " ", " "))
        for k, v in Expense.expense.items():
            tree.insert('', 'end', values=(k, v.title))
        tree.insert('', 'end', values=(" ", " ", " ", " ", " ", " ",))
        print("--------------------------Revenue Accounts-------------------------")
        tree.insert('', 'end', values=(" ", "Revenue Accounts", " ", " ", " ", " "))
        for k, v in Revenue.revenue.items():
            tree.insert('', 'end', values=(k, v.title))
        tree.insert('', 'end', values=(" ", " ", " ", " ", " ", " ",))
        tree.insert('', 'end', values=(" ", "Drawing Accounts", " ", " ", " ", " "))
        for k, v in Drawing.drawing.items():
            tree.insert('', 'end', values=(k, v.title))
        tree.insert('', 'end', values=(" ", " ", " ", " ", " ", " ",))
        button_close = Button(root, text="Close", command=back, height=2, width=10, bg="steel blue", fg="black").place(x=400,y=530)


        # self.interface()

    def view_trial_balance(self):
        root = Tk()
        root.geometry("1300x600")
        root.resizable(0, 0)
        root.title("Accounting")
        window_height = 700
        window_width = 1350
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        root.configure(background='powder blue')
        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 11))
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 13, 'bold'))
        currentMonth = datetime.now().month
        currentYear = datetime.now().year
        x = Label(root, text="Trial Balance", font='Helvetica 18 bold', height=2, width=100, fg="black",
                  bg="steel blue").pack()
        y = Label(root, text=self.company_name.title(), font='Helvetica 18 bold', height=2, width=100, fg="black",
                  bg="powder blue").pack()
        frame = Frame(root)
        frame.pack()
        tree = ttk.Treeview(frame, columns=(1, 2, 3), height=20, show="headings", style="mystyle.Treeview")
        tree.pack(side='left')
        tree.heading(1, text="Account Title")
        tree.heading(2, text="Debit")
        tree.heading(3, text="Credit")
        tree.column(1, width=400)
        tree.column(2, width=150)
        tree.column(3, width=150)
        scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
        scroll.pack(side='right', fill='y')
        tree.configure(yscrollcommand=scroll.set)

        def back():
            root.destroy()
            self.interface()

        button_close = Button(root, text="Close", command=back, height=2, width=10, bg="steel blue", fg="black").pack()
        def grab():
            im1 = PIL.Image.open(r"C:\Users\DeLL\Desktop\111.PNG")
            im2 = ImageGrab.grab(bbox=(100, 60, 1300, 620))
            im2.show()
#         # photo = PhotoImage(file=r"C:\Users\DeLL\Desktop\screen.PNG")
        # here, image option is used to
        # set image on button
        # Button(root, image=photo, width=77, command=grab).pack()
        print("\n"*30)
        print("-----------------------Trial Balance-----------------------")
        print("|{:^30}| |{:^15}| |{:^15}|".format("Account Title","Debit","Credit"))
        print(" ")
        debit_total=0
        credit_total=0
        dollar="$"
        for k,v in Assets.assets.items():
            print("|{:^30}| |{:>15}| |{:>15}|".format(v.title,dollar+str(v.debit_balance),v.credit_balance))
            tree.insert('', 'end', values=(v.title,dollar+str(v.debit_balance),v.credit_balance))
            debit_total+=int(v.debit_balance)
            credit_total+=int(v.credit_balance)
            dollar=""
        for a,b in Liabilities.liabilities.items():
            print("|{:^30}| |{:>15}| |{:>15}|".format(b.title, b.debit_balance, b.credit_balance))
            tree.insert('', 'end', values=(b.title, b.debit_balance, b.credit_balance))
            debit_total += int(b.debit_balance)
            credit_total += int(b.credit_balance)
        for t,y in Owner_Equity.owner_equity.items():
            print("|{:^30}| |{:>15}| |{:>15}|".format(y.title, y.debit_balance, y.credit_balance))
            tree.insert('', 'end', values=(y.title, y.debit_balance, y.credit_balance))
            debit_total += int(y.debit_balance)
            credit_total += int(y.credit_balance)
        for m,n in Expense.expense.items():
            print("|{:^30}| |{:>15}| |{:>15}|".format(n.title, n.debit_balance, n.credit_balance))
            tree.insert('', 'end', values=(n.title, n.debit_balance, n.credit_balance))
            debit_total += int(n.debit_balance)
            credit_total += int(n.credit_balance)
        for z,q in Revenue.revenue.items():
            print("|{:^30}| |{:>15}| |{:>15}|".format(q.title, q.debit_balance, q.credit_balance))
            tree.insert('', 'end', values=(q.title, q.debit_balance, q.credit_balance))
            debit_total += int(q.debit_balance)
            credit_total += int(q.credit_balance)
        for u,i in Drawing.drawing.items():
            print("|{:^30}| |{:>15}| |{:>15}|".format(i.title, i.debit_balance, i.credit_balance))
            tree.insert('', 'end', values=(i.title, i.debit_balance, i.credit_balance))
            debit_total += int(i.debit_balance)
            credit_total += int(i.credit_balance)
        # for q,w in Income_summary.income_summary.items():
        #     print("|{:^30}| |{:>15}| |{:>15}|".format(w.title, w.debit_balance, w.credit_balance))
        #     tree.insert('', 'end', values=(w.title, w.debit_balance, w.credit_balance))
        #     debit_total += int(w.debit_balance)
        #     credit_total += int(w.credit_balance)
        print("")
        tree.insert('', 'end', values=(" "," "," "))
        print("|{:^30}| |{:>15}| |{:>15}|".format("Total","$"+str(debit_total),"$"+str(credit_total)))
        tree.insert('', 'end', values=("Total","$"+str(debit_total),"$"+str(credit_total)))
        root.mainloop()
        user = input("Enter m to go back to main menu: ")
        if user.lower() == "m":
            self.interface()

    def statements(self,inp):
        print("\n"*30)


        if inp=="income":
            self.new_value = 0
            root = Tk()
            root.geometry("1000x600")
            root.resizable(0, 0)
            root.title("Accounting")
            window_height = 700
            window_width = 1350
            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            x_cordinate = int((screen_width / 2) - (window_width / 2))
            y_cordinate = int((screen_height / 2) - (window_height / 2))
            root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
            root.configure(background='powder blue')
            style = ttk.Style()
            style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 11))
            style.configure("mystyle.Treeview.Heading", font=('Calibri', 13, 'bold'))
            currentMonth = datetime.now().month
            currentYear = datetime.now().year
            x = Label(root, text="Income Statement", font='Helvetica 18 bold', height=2, width=100, fg="black",bg="steel blue").pack()
            y = Label(root, text="For the month Ending- " + str(currentMonth) + " " + str(currentYear), font='Helvetica 18 bold',height=1,width=80, bg="powder blue").pack()
            frame = Frame(root)
            frame.pack()
            tree = ttk.Treeview(frame, columns=(1, 2, 3, 4), height=20, show="headings", style="mystyle.Treeview")
            tree.pack(side='left')

            tree.heading(1, text=" ")
            tree.heading(2, text=" ")
            tree.heading(3, text=" ")
            tree.heading(4, text=" ")

            tree.column(1, width=200)
            tree.column(2, width=200)
            tree.column(3, width=200)
            tree.column(4, width=200)
            scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
            scroll.pack(side='right', fill='y')

            tree.configure(yscrollcommand=scroll.set)
            def back():
                root.destroy()
                self.interface()
            button_close=Button(root,text="Close",command=back,height=2,width=10,bg="steel blue",fg="black").pack()

            def grab():
                im1 = PIL.Image.open(r"C:\Users\DeLL\Desktop\111.PNG")
                im2 = ImageGrab.grab(bbox=(100, 60, 1300, 590))
                im2.show()

            # photo = PhotoImage(file=r"C:\Users\DeLL\Desktop\screen.PNG")
            # here, image option is used to
            # set image on button
            # Button(root, image=photo, width=77, command=grab).pack()
            print("----------------------------COMPANY NAME------------------------")
            print("--------------------------Income Statement----------------------")
            dollar_1="$"
            dollar_2="$"
            sum_rev=0
            sum_exp=0
            print("|{:^10}".format("Revenues"))
            tree.insert('', 'end', values=("Revenues"," "," "," "))
            for k,v in Revenue.revenue.items():
                if int(v.debit_balance)>int(v.credit_balance):
                    print("|{:^10} {:^30} |{:>15} | {:>15}|".format(" ",v.title," ","("+str(dollar_1)+str(v.debit_balance)+")"))
                    tree.insert('', 'end', values=(" ",v.title," ","("+str(dollar_1)+str(v.debit_balance)+")"))
                    sum_rev-=int(v.debit_balance)
                    dollar_1=""
                else:
                    print("|{:^10} {:^30} |{:>15} | {:>15}|".format(" ", v.title," ",str(dollar_1)+str(v.credit_balance)))
                    tree.insert('', 'end', values=(" ", v.title, " ",str(dollar_1)+str(v.credit_balance)))
                    sum_rev+=int(v.credit_balance)
                    dollar_1=""

            print("|{:^10}".format("Less: Expenses"))
            tree.insert('', 'end', values=("Less: Expenses"," "," "," "))
            for w,x in Expense.expense.items():
                if int(x.debit_balance)<int(x.credit_balance):
                    print("|{:^10} {:^30} |{:>15} | {:>15}|".format(" ", x.title, "("+str(dollar_2)+str(x.credit_balance)+")"," "))
                    tree.insert('', 'end', values=(" ", x.title, "("+str(dollar_2)+str(x.credit_balance)+")"," "))
                    sum_exp-=int(x.credit_balance)
                    dollar_2=""
                else:
                    sum_exp+=int(x.debit_balance)
                    print("|{:^10} {:^30} |{:>15} | {:^15}|".format(" ", x.title,str(dollar_2)+str(x.debit_balance)," "))
                    tree.insert('', 'end',values=(" ", x.title,str(dollar_2)+str(x.debit_balance), " "))
                    dollar_2=""
            print("|{:^10} {:^30} |{:>15} | {:>15}|".format(" ", " ","-------", " "))
            tree.insert('', 'end', values=(" "," ","----------", " "))
            print("|{:^10} {:^30} |{:>15} | {:>15}|".format(" ", "Total Expenses",sum_exp, " "))
            tree.insert('', 'end', values=(" ", "Total Expenses",sum_exp, " "))

            global new_value
            valuee=sum_rev-sum_exp
            new_valuee=valuee
            self.new_value=new_valuee
            if valuee>=0:
                print("|{:^10} {:^30} |{:>15} | {:>15}|".format(" ", " ", " ","-------"))
                tree.insert('', 'end', values=(" ", " "," ", "----------"))
                print("|{:^10} {:^30} |{:>15} | {:>15}|".format("Net Income", " ", " ","$"+str(valuee)))
                tree.insert('', 'end', values=("Net Income"," "," ","$ "+str(valuee)))
                print("|{:^10} {:^30} |{:>15} | {:>15}|".format(" ", " ", " ", "-------"))
                tree.insert('', 'end', values=(" ", " "," ", "----------"))
            else:
                print("|{:^10} {:^30} |{:>15} | {:>15}|".format(" ", " ", " ", "-------"))
                tree.insert('', 'end', values=(" ", " "," ", "----------"))
                print("|{:^10} {:^30} |{:>15} | {:>15}|".format("Net Loss", " ", " ","$"+str(valuee)))
                tree.insert('', 'end', values=("Net Loss", " ", " ","$"+str(valuee)))
                print("|{:^10} {:^30} |{:>15} | {:>15}|".format(" ", " ", " ", "----------"))
                tree.insert('', 'end', values=(" ", " "," ", "----------"))

            root.mainloop()
            user=input("Enter m to go back to the main menu: ")
            if user=="m":
                self.interface()

        if inp=="owner equity":
            self.new_equity = 0
            print("\n" * 30)
            root = Tk()
            root.geometry("1000x600")
            root.resizable(0, 0)
            root.title("Accounting")
            window_height = 700
            window_width = 1350
            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            x_cordinate = int((screen_width / 2) - (window_width / 2))
            y_cordinate = int((screen_height / 2) - (window_height / 2))
            root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
            root.configure(background='powder blue')
            style = ttk.Style()
            style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 11))
            style.configure("mystyle.Treeview.Heading", font=('Calibri', 13, 'bold'))
            currentMonth = datetime.now().month
            currentYear = datetime.now().year
            x = Label(root, text="Owner's Equity Statement", font='Helvetica 18 bold', height=2, width=100, fg="white",bg="steel blue").pack()
            y = Label(root, text="For the month Ended- " + str(currentMonth) + " " + str(currentYear),font='Helvetica 18 bold', height=1,width=80, bg="powder blue").pack()
            frame = Frame(root)
            frame.pack()
            tree = ttk.Treeview(frame, columns=(1, 2, 3), height=20, show="headings", style="mystyle.Treeview")
            tree.pack(side='left')

            tree.heading(1, text=" ")
            tree.heading(2, text=" ")
            tree.heading(3, text=" ")

            tree.column(1, width=200)
            tree.column(2, width=200)
            tree.column(3, width=200)
            scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
            scroll.pack(side='right', fill='y')

            tree.configure(yscrollcommand=scroll.set)
            def back():
                root.destroy()
                self.interface()
            button_close=Button(root,text="Close",command=back,height=2,width=10,bg="Steel blue",fg="white").pack()

            def grab():
                im1 = PIL.Image.open(r"C:\Users\DeLL\Desktop\111.PNG")
                im2 = ImageGrab.grab(bbox=(100, 60, 1300, 590))
                im2.show()

            # photo = PhotoImage(file=r"C:\Users\DeLL\Desktop\screen.PNG")
            # here, image option is used to
            # set image on button
            # Button(root, image=photo, width=77, command=grab).pack()
            print("----------------------------COMPANY NAME------------------------")
            print("----------------------Owner Equity Statement----------------------")
            print("")
            dollar_1 = "$"
            dollar_2 = "$"
            sum_o_e = 0
            sum_d = 0
            for u, i in Owner_Equity.owner_equity.items():
                if int(i.debit_balance) > int(i.credit_balance):
                    sum_o_e -= int(i.debit_balance)
                    print("|{:^30} |{:>15}| |{:>15}|".format(i.title, " ", "(" +i.debit_balance+ ")"))
                    tree.insert('', 'end', values=(i.title," ","(" +i.debit_balance+ ")"))
                else:
                    sum_o_e += int(i.credit_balance)
                    print("|{:^30} |{:>15}| |{:>15}|".format(i.title, " ", "$"+str(i.credit_balance)))
                    tree.insert('', 'end', values=(i.title, " ", "$"+str(i.credit_balance)))
            print("|{:^30} |{:>15}| |{:>15}|".format("Add: Income", " ", self.new_value))
            tree.insert('', 'end', values=("Add: Income"," ",self.new_value))

            #assigning new value to owner equity
            if self.new_value>0:
                Owner_Equity.owner_equity["O001"].credit+=self.new_value
                Owner_Equity.owner_equity["O001"].update_debit_credit_balance()
            else:
                Owner_Equity.owner_equity["O001"].debit+=self.new_value
                Owner_Equity.owner_equity["O001"].update_debit_credit_balance()

            for x, c in Drawing.drawing.items():
                if int(c.debit_balance) > int(c.credit_balance):
                    sum_d += int(c.debit_balance)
                    print("|{:^30} |{:>15}| |{:>15}|".format(c.title, c.debit_balance, " "))
                    Owner_Equity.owner_equity["O001"].debit+=sum_d
                    tree.insert('', 'end', values=(c.title,"$"+str(c.debit_balance)," "))
                else:
                    sum_d -= int(c.credit_balance)
                    print("|{:^30} |{:>15}| |{:>15}|".format(c.title, "(" + str(c.credit_balance) + ")", " "))
                    Owner_Equity.owner_equity["O001"].credit += sum_d
                    tree.insert('', 'end', values=(c.title, "(" +"$"+ str(c.credit_balance) + ")"," "))
            tree.insert('', 'end', values=("Less: Drawings", " ", sum_d))
            o_capital = (sum_o_e + int(self.new_value)) - sum_d

            print("|{:^30} |{:>15}| |{:>15}|".format("Owner's Capital", " ", o_capital))
            tree.insert('', 'end', values=(" "," ","--------------"))
            tree.insert('', 'end', values=("Owner's Capital"," ","$"+str(o_capital)))
            tree.insert('', 'end', values=(" "," ","--------------"))
            global new_equity
            new_equityy=o_capital
            self.new_equity=new_equityy
            root.mainloop()
        if inp=="balance sheet":
            root = Tk()
            root.geometry("1300x600")
            root.resizable(0, 0)
            root.title("Accounting")
            window_height = 700
            window_width = 1350
            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            x_cordinate = int((screen_width / 2) - (window_width / 2))
            y_cordinate = int((screen_height / 2) - (window_height / 2))
            root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
            root.configure(background='powder blue')
            style = ttk.Style()
            style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 11))
            style.configure("mystyle.Treeview.Heading", font=('Calibri', 13, 'bold'))
            currentMonth = datetime.now().month
            currentYear = datetime.now().year
            x = Label(root, text="Balance Sheet", font='Helvetica 18 bold', height=2, width=100, fg="black",
                      bg="steel blue").pack()
            y = Label(root, text=self.company_name.title(), font='Helvetica 18 bold', height=2, width=100, fg="black",
                      bg="powder blue").pack()
            frame = Frame(root)
            frame.pack()
            tree = ttk.Treeview(frame, columns=(1, 2, 3), height=20, show="headings", style="mystyle.Treeview")
            tree.pack(side='left')
            tree.heading(1, text="Account Title")
            tree.heading(2, text="Debit")
            tree.heading(3, text="Credit")
            tree.column(1, width=400)
            tree.column(2, width=150)
            tree.column(3, width=150)
            scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
            scroll.pack(side='right', fill='y')
            tree.configure(yscrollcommand=scroll.set)

            def back():
                root.destroy()
                self.interface()

            button_close = Button(root, text="Close", command=back, height=2, width=10, bg="steel blue",
                                  fg="black").pack()

            def grab():
                im1 = PIL.Image.open(r"C:\Users\DeLL\Desktop\111.PNG")
                im2 = ImageGrab.grab(bbox=(100, 60, 1300, 620))
                im2.show()

            # photo = PhotoImage(file=r"C:\Users\DeLL\Desktop\screen.PNG")
            # here, image option is used to
            # set image on button
            # Button(root, image=photo, width=77, command=grab).pack()
            print("\n" * 30)
            print("-----------------------Balance Sheet -----------------------")
            print("|{:^30}| |{:^15}| |{:^15}|".format("Account Title", "Debit", "Credit"))
            print(" ")
            asset_total = 0
            liability_equity_total = 0
            tree.insert('', 'end', values=("ASSETS"," "," "))
            for k, v in Assets.assets.items():
                print("|{:^30}| |{:>15}| |{:>15}|".format(v.title, v.debit_balance, v.credit_balance))
                tree.insert('', 'end', values=(v.title, v.debit_balance, v.credit_balance))
                asset_total += int(v.debit_balance)
                asset_total -= int(v.credit_balance)
            tree.insert('', 'end', values=("Total Assets",asset_total," "))

            tree.insert('', 'end', values=(" ", " ", " "))
            tree.insert('', 'end', values=("LIABILITIES", " ", " "))
            for a, b in Liabilities.liabilities.items():
                print("|{:^30}| |{:>15}| |{:>15}|".format(b.title, b.debit_balance, b.credit_balance))
                tree.insert('', 'end', values=(b.title, b.debit_balance, b.credit_balance))
                liability_equity_total += int(b.debit_balance)
                liability_equity_total += int(b.credit_balance)
            tree.insert('', 'end', values=(" ", " ", " "))
            tree.insert('', 'end', values=("OWNER'S EQUITY"," ", " "))
            for t, y in Owner_Equity.owner_equity.items():
                if self.new_equity!=0:
                    print("new equity= ",str(self.new_equity))
                    print("|{:^30}| |{:>15}| |{:>15}|".format(y.title, y.debit_balance, y.credit_balance))
                    tree.insert('', 'end', values=(y.title, y.debit_balance, self.new_equity))
                    liability_equity_total += int(y.debit_balance)
                    liability_equity_total += int(self.new_equity)
                else:
                    print("|{:^30}| |{:>15}| |{:>15}|".format(y.title, y.debit_balance, y.credit_balance))
                    tree.insert('', 'end', values=(y.title, y.debit_balance, y.credit_balance))
                    liability_equity_total += int(y.debit_balance)
                    liability_equity_total += int(y.credit_balance)
            tree.insert('', 'end', values=("Total Liabilites + Owner's Equity",liability_equity_total, " "))
            root.mainloop()



    def owner_equity_statement(self):
        print("\n" * 30)
        print("----------------------------COMPANY NAME------------------------")
        print("----------------------Owner Equity Statement----------------------")
        print("")
        dollar_1 = "$"
        dollar_2 = "$"
        sum_o_e=0
        sum_d=  0
        for k,v in Owner_Equity.owner_equity.items():
            if int(v.debit_balance)>int(v.credit_balance):
                sum_o_e-=int(v.debit_balance)
                print("|{:^30} |{:>15}| |{:>15}|".format(v.title," ","("+str(v.debit_balance)+")"))
            else:
                sum_o_e+=int(v.credit_balance)
                print("|{:^30} |{:>15}| |{:>15}|".format(v.title, " ", v.credit_balance))
        print("|{:^30} |{:>15}| |{:>15}|".format("Add: Income", " "," "))

        for x,c in Drawing.drawing.items():
            if int(c.debit_balance)>int(c.credit_balance):
                sum_d+=int(c.debit_balance)
                print("|{:^30} |{:>15}| |{:>15}|".format(v.title,v.debit_balance," "))
            else:
                sum_d-=int(c.credit_balance)
                print("|{:^30} |{:>15}| |{:>15}|".format(v.title, "("+str(c.credit_balance)+")", " "))
        o_capital=(sum_o_e)-sum_d
        print("|{:^30} |{:>15}| |{:>15}|".format("Owner's Capital", " ", o_capital))

    def close_accounts(self):
        # closing revenue to income summary
        for k,v in Revenue.revenue.items():
            debit = 0
            credit = 0
            if v.debit_balance>v.credit_balance:
                debit+=v.debit_balance
                v.credit+=v.debit_balance
                Revenue.revenue[k].update_credit(v.credit)
            else:
                credit+=v.credit_balance
                v.debit+=credit

                Revenue.revenue[k].update_debit(v.debit)
            if credit>debit:
                final_bal=credit-debit
                Income_summary.income_summary["I002"].credit += final_bal
            else:
                final_bal=debit-credit
                Income_summary.income_summary["I002"].debit += final_bal

        #closing expenses to income summary
        for k,v in Expense.expense.items():
            debit = 0
            credit = 0
            if v.debit_balance > v.credit_balance:
                debit += v.debit_balance
                v.credit += v.debit_balance
                Expense.expense[k].update_credit(v.credit)
            else:
                credit+=v.credit_balance
                v.debit+=v.credit_balance
                Expense.expense[k].update_debit(v.debit)
            if debit>credit:
                final_bal=debit-credit
                Income_summary.income_summary["I002"].debit+=final_bal
            else:
                final_bal=credit-debit
                Income_summary.income_summary["I002"].credit += final_bal

        # Income_summary.income_summary["I002"].update_debit_credit_balance()
        #Close owner's capital to income_summary


        if Income_summary.income_summary["I002"].credit_balance>Income_summary.income_summary["I002"].debit_balance:
            summary_value=Income_summary.income_summary["I002"].credit_balance
            #closing the summary
            Income_summary.income_summary["I002"].update_debit(summary_value)
            Owner_Equity.owner_equity["O001"].credit+=summary_value
            Owner_Equity.owner_equity["O001"].update_debit_credit_balance()
            Income_summary.income_summary["I002"].update_debit_credit_balance()
        elif Income_summary.income_summary["I002"].debit_balance>Income_summary.income_summary["I002"].credit_balance:
            summary_value = Income_summary.income_summary["I002"].debit_balance
            #closing summary
            Income_summary.income_summary["I002"].update_credit(summary_value)
            Owner_Equity.owner_equity["O001"].debit+=summary_value
            Owner_Equity.owner_equity["O001"].update_debit_credit_balance()
            Income_summary.income_summary["I002"].update_debit_credit_balance()

        #now closing drawings to owner's equity
        for k,v in Drawing.drawing.items():
            debit = 0
            credit = 0
            if v.debit_balance > v.credit_balance:
                debit += v.debit_balance

                v.credit += v.debit_balance
                Drawing.drawing[k].update_credit(v.credit)
            else:
                credit+=v.credit_balance
                v.debit+=v.credit_balance
                Drawing.drawing[k].update_debit(v.debit)
            final_bal=debit-credit
            Income_summary.income_summary["I002"].debit+=final_bal
        Income_summary.income_summary["I002"].update_debit_credit_balance()




    def refresh(self):

        conn=sqlite3.connect("accounts_db.db")
        c = conn.cursor()
        c.execute("Delete from Assets")
        Assets.assets.clear()
        c.execute("Delete from Entries")
        Entries.entries.clear()
        c.execute("Delete from Expense")
        Expense.expense.clear()
        c.execute("Delete from Journal")
        Journal.journal.clear()
        c.execute("Delete from Liability")
        Liabilities.liabilities.clear()
        c.execute("Delete from Owner_Equity")
        Owner_Equity.owner_equity.clear()
        c.execute("Delete from Revenue")
        Revenue.revenue.clear()
        c.execute("Delete from Drawings")
        Drawing.drawing.clear()
        conn.commit()
        Income_summary.income_summary["I002"].update_debit(0)
        Income_summary.income_summary["I002"].update_credit(0)
        # Income_summary.income_summary.update_debit_credit_balance()
    def help(self):
        root = Tk()
        root.geometry("1300x600")
        root.resizable(0, 0)
        root.title("Accounting")
        window_height = 700
        window_width = 1350
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        root.configure(background='powder blue')
        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 11))
        x = Label(root, text="Instruction Guide", font='Helvetica 18 bold', height=2, width=100, fg="black",
                  bg="steel blue").pack()

        def back():
            root.destroy()
            self.interface()

        button_close = Button(root, text="Close", command=back, height=2, width=10, bg="steel blue",
                              fg="black").pack()

    def export(self):
        import xlwt
        workbook = Workbook('accounting.xlsx')
        worksheet = workbook.add_worksheet()
        worksheet1 = workbook.add_worksheet()
        conn = sqlite3.connect('accounts_db.db')
        c = conn.cursor()
        c.execute("select * from Entries")
        mysel=c.execute("select * from Journal")
        worksheet.write(0,0,"General Journal")
        jj=0
        for i, row in enumerate(mysel):
            jj=i
            for j, value in enumerate(row):
                worksheet.write(i+1, j, value)

        print("Ive exported ")
        mysel1 = c.execute("select * from Entries")
        worksheet1.write(0, 0, "Entries")
        for l, row in enumerate(mysel1):
            for k, value in enumerate(row):
                worksheet1.write(l+1, k, value)
        workbook.close()

if __name__=="__main__":
    # c.export()
    # root = Tk()
    Accounting_management("UIT")
    # Progress bar widget
    # comp_name = StringVar()
    # label = Label(root, text="Enter your company's name: ").pack()
    # company_entry = Entry(root,textvariable=comp_name, width=25).pack()
    # progress = Progressbar(root, orient=HORIZONTAL,length=500, mode='determinate')
    #
    #
    # # Function responsible for the updation
    # # of the progress bar value
    # def bar():
    #     import time
    #     compan_name=comp_name.get()
    #     progress['value'] = 20
    #     root.update_idletasks()
    #     time.sleep(1)
    #
    #     progress['value'] = 40
    #     root.update_idletasks()
    #     time.sleep(1)
    #
    #     progress['value'] = 50
    #     root.update_idletasks()
    #     time.sleep(1)
    #
    #     progress['value'] = 60
    #     root.update_idletasks()
    #     time.sleep(1)
    #
    #     progress['value'] = 80
    #     root.update_idletasks()
    #     time.sleep(1)
    #     progress['value'] = 100
    #     root.destroy()
    #     g=Accounting_management(compan_name.upper())
    #
    #
    # progress.pack(pady=10)
    #
    # # This button will initialize
    # # the progress bar
    # Button(root, text='Run App', command=bar).pack(pady=10)
    #
    # # infinite loop
    # root.mainloop()