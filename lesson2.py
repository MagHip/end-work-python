import tkinter as tk

win = tk.Tk()

win.title('Label')
win.geometry('300x400+100+200')

label_1 = tk.Label(win, text='''Hail!
Arthur''',
                   bg='yellow',
                   fg='blue',
                   font=('Helvetica',20,'bold'),
                   padx=10, pady=15,
                   width=13, height=10,
                   anchor='ne', #must be n, ne, e, se, s, sw, w, nw, or center
                   relief=tk.RAISED,
                   bd='5',
                   justify=tk.LEFT
                   )
label_1.pack()

win.mainloop()