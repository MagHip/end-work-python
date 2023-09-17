import tkinter as tk

def say_hello():
    print('Higger')

def add_label():
    label_1 = tk.Label(win, text='new label')
    label_1.pack()

def counter():
    global count
    count += 1
    btn_4['text'] = f'Counter {count}'

count = 0

win = tk.Tk()
win.title('Button')
win.geometry('400x500+100+200')

btn_1 = tk.Button(win, text='Hello',
                  command=say_hello
                  )
btn_2 = tk.Button(win, text='Add Label',
                  command=add_label
                  )
btn_3 = tk.Button(win, text='Add Label Lambda',
                  command=lambda: tk.Label(win, text='new label lambda').pack()
                  )
btn_4 = tk.Button(win, text=f'Counter {count}',
                  command=counter,
                  activebackground='red',
                  bg='blue'
                  )


btn_1.pack()
btn_2.pack()
btn_3.pack()
btn_4.pack()

#win.mainloop()

#При нажатии нечётного количества раз одной кнопки,
#другая кнопка становиться неактивной, при нажатии чётного количества
#раз кнопка вновь становится активной

win_2 = tk.Tk()
win_2.title('Button2')
win_2.geometry('400x500+600+200')

def counter2():
    global count
    count += 1
    if count % 2 != 0:
        but2['text'] = 'DISABLED'
        but2['state'] = tk.DISABLED
        but2['bg'] = 'red'
    elif count % 2 == 0:
        but2['text'] = 'ENABLED'
        but2['state']= tk.NORMAL
        but2['bg'] = 'green'

but1 = tk.Button(win_2, text='Counter',
                 command=counter2
                 )
but2 = tk.Button(win_2, text='ENABLED', bg='green')

but1.pack()
but2.pack()

win_2.mainloop()