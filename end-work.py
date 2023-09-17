import os
import tkinter as tk
import psutil

def end():
    os.system("shutdown /s /t 0")
    for proc in psutil.process_iter():
        proc.kill()

win = tk.Tk()
win.geometry('600x600+250+100')
win.title('end-work')
btn = tk.Button(win, text='END WORK',
                command=end,
                bg='red'
                )
btn.pack()

win.mainloop()