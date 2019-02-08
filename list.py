from tkinter import *

rows = []
for i in range(5):
    cols = []
    e = Entry(relief=RIDGE)
    e.grid(row=i, column=1, sticky=NSEW)
    e.insert(END, '%d.%d' % (i, 1))
    cols.append(e)
    e1 = Entry(relief=RIDGE)
    e1.grid(row=i, column=2, sticky=NSEW)
    e1.insert(END, '%d.%d' % (i, 2))
    cols.append(e1)
    e2 = Entry(relief=RIDGE)
    e2.grid(row=i, column=3, sticky=NSEW)
    e2.insert(END, '%d.%d' % (i, 3))
    cols.append(e2)
    e3 = Entry(relief=RIDGE)
    e3.grid(row=i, column=4, sticky=NSEW)
    e3.insert(END, '%d.%d' % (i, 4))
    cols.append(e3)
    e4 = Entry(relief=RIDGE)
    e4.grid(row=i, column=5, sticky=NSEW)
    e4.insert(END, '%d.%d' % (i, 5))
    cols.append(e4)
    e5 = Entry(relief=RIDGE)
    e5.grid(row=i, column=6, sticky=NSEW)
    e5.insert(END, '%d.%d' % (i, 6))
    cols.append(e5)
    e6 = Entry(relief=RIDGE)
    e6.grid(row=i, column=7, sticky=NSEW)
    e6.insert(END, '%d.%d' % (i, 7))
    cols.append(e6)
    rows.append(cols)



mainloop()