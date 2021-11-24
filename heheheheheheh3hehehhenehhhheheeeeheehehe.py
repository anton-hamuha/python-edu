from tkinter import *
import tkinter.messagebox as box
window = tk()
window.title('entry example')
frame = frame(window)
entry = entry(frame)
def dialog():
    box.showinfo('greetings', 'welcome' + entry.get())
btn = button(frame, text = 'enter name', command=dialog)
btn.pack(side=right, padx=5)
entry.pack(side=left)
frame.pack(padx=20, pady=20)




window.mainloop()