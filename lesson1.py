import tkinter as tk

#создаем окно

win = tk.Tk()
icon = tk.PhotoImage(file='rocket.png')
win.iconphoto(False, icon)
win.config(bg='#35ad6a')
win.title('Window1')
win.geometry('600x600+100+150')
win.minsize(100, 100)
win.maxsize(1000, 1000)
# win.resizable(False, False)

#главный цикл, запускающий окно
win.mainloop()