from tkinter import *
import tkinter.messagebox as box
window = tk()
window.title('listbox example')
frame = frame(window)
listbox = listbox(frame)
listbox.insert(1, 'html5 in easy steps')
listbox.insert(2, 'css3 in easy steps')
listbox.insert(3, 'javascript in easy steps')
def dialog():
    box.showinfo('selection', 'your choice:' +\
                 listbox.get(listbox.curselection()))
btn = button(frame, text = 'choose', command = dialog)
btn.pack(side=right, padx=5)
listbox.pack(side=left)
frame.pack(padx=30, pady=30)
window.mainloop()
