#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.18
#  in conjunction with Tcl version 8.6
#    Nov 25, 2018 08:08:44 PM IST  platform: Windows NT
import login
import datetime
from tkinter import messagebox
import sys
import dbs
import home
import update
import addnew
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import transaction_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    transaction_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    transaction_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def make_entry(self):
        self.flatno_1 = self.flatnoentry.get().lower()
        self.main_amount= self.maintanence_entry.get()
        self.pay_roll = self.paymodeentry.get()
        self.manual_date1= self.manual_date.get()
        self.month_name= self.month_entry.get()
        self.remark_1 = self.remarks_entry.get()
        self.payment_date=str(datetime.date.today())
        print(self.flatno_1)
        print(self.main_amount)
        print(self.pay_roll)
        print(self.manual_date1)
        print(self.month_name)
        print(self.remark_1)
        print(self.payment_date)
        if(len(self.flatno_1)>1):
            # prepare a cursor object using cursor() method
            cursor = dbs.db.cursor()

            # Prepare SQL query to INSERT a record into the database.
            sql = "INSERT INTO monthly_pay(flat_no, \
            maintainance, payment_mode, manual_date,payment_date, month,remark) \
            VALUES ('%s', '%s', '%s', '%s' , '%s','%s','%s')" % \
            (self.flatno_1,self.main_amount,self.pay_roll,self.manual_date1,self.payment_date,self.month_name,self.remark_1)
            sql1="select * from flat_details where flat_no='%s'"%(self.flatno_1)
            cursor1=dbs.db.cursor()
            cursor1.execute(sql1)
            result1=cursor1.fetchall()
            
            for row in result1:
                val=int(row[12])
            total_due=val-int(self.main_amount)
            print(total_due)
            sql2="update flat_details set total_due='%s' where flat_no='%s'"%(total_due,self.flatno_1)
            cursor2=dbs.db.cursor()
            
            try:
                cursor.execute(sql)
                cursor2.execute(sql2)
                # Commit your changes in the database
                dbs.db.commit()
                messagebox.showinfo("SAVED", "Information Successfully Submitted")
            except:
                # Rollback in case there is any error
                dbs.db.rollback()
                dbs.db.close()
                messagebox.showerror("Error", "Contact To Developer!")
        else:
            messagebox.showerror("Error", "Please Enter Correct Detail")
    def logout1(self):
        root.destroy()
        login.vp_start_gui()
    def searchbtn2(self):
        root.destroy()
        update.vp_start_gui1()
    def home_btn(self):
        root.destroy()
        home.vp_start_gui()
    def add_btn(self):
        root.destroy()
        addnew.vp_start_gui()
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font9 = "-family Arial -size 9 -weight normal -slant roman "  \
            "-underline 0 -overstrike 0"

        top.geometry("630x630+363+79")
        top.title("Rent Schedule")
        top.configure(background="#2c3e50")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        top.configure(takefocus="1")

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.Button1 = tk.Button(top,command=self.add_btn)
        self.Button1.place(relx=0.032, rely=0.127, height=44, width=147)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#f1f1f1")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''ADD NEW FLAT ENTRY''')

        self.Button1_2 = tk.Button(top,command=self.logout1)
        self.Button1_2.place(relx=0.032, rely=0.603, height=34, width=117)
        self.Button1_2.configure(activebackground="#d9d9d9")
        self.Button1_2.configure(activeforeground="#000000")
        self.Button1_2.configure(background="#f1f1f1")
        self.Button1_2.configure(disabledforeground="#a3a3a3")
        self.Button1_2.configure(foreground="#000000")
        self.Button1_2.configure(highlightbackground="#d9d9d9")
        self.Button1_2.configure(highlightcolor="black")
        self.Button1_2.configure(pady="0")
        self.Button1_2.configure(text='''LOGOUT''')

        

        self.Button1_4 = tk.Button(top,command=self.home_btn)
        self.Button1_4.place(relx=0.032, rely=0.032, height=44, width=147)
        self.Button1_4.configure(activebackground="#d9d9d9")
        self.Button1_4.configure(activeforeground="#000000")
        self.Button1_4.configure(background="#f1f1f1")
        self.Button1_4.configure(disabledforeground="#a3a3a3")
        self.Button1_4.configure(foreground="#000000")
        self.Button1_4.configure(highlightbackground="#d9d9d9")
        self.Button1_4.configure(highlightcolor="black")
        self.Button1_4.configure(pady="0")
        self.Button1_4.configure(text='''HOME''')

        self.Button1_5 = tk.Button(top,command=self.searchbtn2)
        self.Button1_5.place(relx=0.032, rely=0.222, height=44, width=147)
        self.Button1_5.configure(activebackground="#d9d9d9")
        self.Button1_5.configure(activeforeground="#000000")
        self.Button1_5.configure(background="#f1f1f1")
        self.Button1_5.configure(disabledforeground="#a3a3a3")
        self.Button1_5.configure(font=font9)
        self.Button1_5.configure(foreground="#000000")
        self.Button1_5.configure(highlightbackground="#d9d9d9")
        self.Button1_5.configure(highlightcolor="black")
        self.Button1_5.configure(pady="0")
        self.Button1_5.configure(text='''SEARCH''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.349, rely=0.111, height=21, width=144)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font9)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''FLAT-NO''')

        self.flatnoentry = tk.Entry(top)
        self.flatnoentry.place(relx=0.683, rely=0.111, height=20, relwidth=0.292)

        self.flatnoentry.configure(background="white")
        self.flatnoentry.configure(disabledforeground="#a3a3a3")
        self.flatnoentry.configure(font="TkFixedFont")
        self.flatnoentry.configure(foreground="#000000")
        self.flatnoentry.configure(highlightbackground="#d9d9d9")
        self.flatnoentry.configure(highlightcolor="black")
        self.flatnoentry.configure(insertbackground="black")
        self.flatnoentry.configure(selectbackground="#c4c4c4")
        self.flatnoentry.configure(selectforeground="black")

        self.Label2_7 = tk.Label(top)
        self.Label2_7.place(relx=0.349, rely=0.238, height=21, width=144)
        self.Label2_7.configure(activebackground="#f9f9f9")
        self.Label2_7.configure(activeforeground="black")
        self.Label2_7.configure(background="#d9d9d9")
        self.Label2_7.configure(disabledforeground="#a3a3a3")
        self.Label2_7.configure(font=font9)
        self.Label2_7.configure(foreground="#000000")
        self.Label2_7.configure(highlightbackground="#d9d9d9")
        self.Label2_7.configure(highlightcolor="black")
        self.Label2_7.configure(text='''CASH/CHEQUE/TR''')

        self.Button2 = tk.Button(top, command=self.make_entry)
        self.Button2.place(relx=0.492, rely=0.603, height=34, width=107)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#f1f1f1")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''SAVE''')

        self.Button2_9 = tk.Button(top)
        self.Button2_9.place(relx=0.746, rely=0.603, height=34, width=107)
        self.Button2_9.configure(activebackground="#d9d9d9")
        self.Button2_9.configure(activeforeground="#000000")
        self.Button2_9.configure(background="#f1f1f1")
        self.Button2_9.configure(disabledforeground="#a3a3a3")
        self.Button2_9.configure(foreground="#000000")
        self.Button2_9.configure(highlightbackground="#d9d9d9")
        self.Button2_9.configure(highlightcolor="black")
        self.Button2_9.configure(pady="0")
        self.Button2_9.configure(text='''RESET''')

        self.Label6 = tk.Label(top)
        self.Label6.place(relx=0.349, rely=0.302, height=21, width=144)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(activeforeground="black")
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(highlightbackground="#d9d9d9")
        self.Label6.configure(highlightcolor="black")
        self.Label6.configure(text='''DATE''')

        self.Label8 = tk.Label(top)
        self.Label8.place(relx=0.349, rely=0.175, height=21, width=144)
        self.Label8.configure(activebackground="#f9f9f9")
        self.Label8.configure(activeforeground="black")
        self.Label8.configure(background="#d9d9d9")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(highlightbackground="#d9d9d9")
        self.Label8.configure(highlightcolor="black")
        self.Label8.configure(text='''MAINTAINCE AMOUNT''')

        self.paymodeentry = tk.Entry(top)
        self.paymodeentry.place(relx=0.683, rely=0.238, height=20
                , relwidth=0.292)
        self.paymodeentry.configure(background="white")
        self.paymodeentry.configure(disabledforeground="#a3a3a3")
        self.paymodeentry.configure(font="TkFixedFont")
        self.paymodeentry.configure(foreground="#000000")
        self.paymodeentry.configure(highlightbackground="#d9d9d9")
        self.paymodeentry.configure(highlightcolor="black")
        self.paymodeentry.configure(insertbackground="black")
        self.paymodeentry.configure(selectbackground="#c4c4c4")
        self.paymodeentry.configure(selectforeground="black")

        self.maintanence_entry = tk.Entry(top)
        self.maintanence_entry.place(relx=0.683, rely=0.175, height=20
                , relwidth=0.292)
        self.maintanence_entry.configure(background="white")
        self.maintanence_entry.configure(disabledforeground="#a3a3a3")
        self.maintanence_entry.configure(font="TkFixedFont")
        self.maintanence_entry.configure(foreground="#000000")
        self.maintanence_entry.configure(highlightbackground="#d9d9d9")
        self.maintanence_entry.configure(highlightcolor="black")
        self.maintanence_entry.configure(insertbackground="black")
        self.maintanence_entry.configure(selectbackground="#c4c4c4")
        self.maintanence_entry.configure(selectforeground="black")

        self.manual_date = tk.Entry(top)
        self.manual_date.place(relx=0.683, rely=0.302, height=20, relwidth=0.292)

        self.manual_date.configure(background="white")
        self.manual_date.configure(disabledforeground="#a3a3a3")
        self.manual_date.configure(font="TkFixedFont")
        self.manual_date.configure(foreground="#000000")
        self.manual_date.configure(highlightbackground="#d9d9d9")
        self.manual_date.configure(highlightcolor="black")
        self.manual_date.configure(insertbackground="black")
        self.manual_date.configure(selectbackground="#c4c4c4")
        self.manual_date.configure(selectforeground="black")

        self.Label7 = tk.Label(top)
        self.Label7.place(relx=0.349, rely=0.429, height=21, width=148)
        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(activeforeground="black")
        self.Label7.configure(background="#d9d9d9")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(highlightbackground="#d9d9d9")
        self.Label7.configure(highlightcolor="black")
        self.Label7.configure(text='''REMARKS''')

        self.remarks_entry = tk.Entry(top)
        self.remarks_entry.place(relx=0.683, rely=0.429, height=20
                , relwidth=0.292)
        self.remarks_entry.configure(background="white")
        self.remarks_entry.configure(disabledforeground="#a3a3a3")
        self.remarks_entry.configure(font="TkFixedFont")
        self.remarks_entry.configure(foreground="#000000")
        self.remarks_entry.configure(highlightbackground="#d9d9d9")
        self.remarks_entry.configure(highlightcolor="black")
        self.remarks_entry.configure(insertbackground="black")
        self.remarks_entry.configure(selectbackground="#c4c4c4")
        self.remarks_entry.configure(selectforeground="black")

        self.lab43 = tk.Label(top)
        self.lab43.place(relx=0.349, rely=0.365, height=21, width=144)
        self.lab43.configure(activebackground="#f9f9f9")
        self.lab43.configure(activeforeground="black")
        self.lab43.configure(background="#d9d9d9")
        self.lab43.configure(disabledforeground="#a3a3a3")
        self.lab43.configure(foreground="#000000")
        self.lab43.configure(highlightbackground="#d9d9d9")
        self.lab43.configure(highlightcolor="black")
        self.lab43.configure(text='''MONTH''')

        self.month_entry = tk.Entry(top)
        self.month_entry.place(relx=0.683, rely=0.365, height=20, relwidth=0.292)

        self.month_entry.configure(background="white")
        self.month_entry.configure(disabledforeground="#a3a3a3")
        self.month_entry.configure(font="TkFixedFont")
        self.month_entry.configure(foreground="#000000")
        self.month_entry.configure(highlightbackground="#d9d9d9")
        self.month_entry.configure(highlightcolor="black")
        self.month_entry.configure(insertbackground="black")
        self.month_entry.configure(selectbackground="#c4c4c4")
        self.month_entry.configure(selectforeground="black")

if __name__ == '__main__':
    vp_start_gui()




