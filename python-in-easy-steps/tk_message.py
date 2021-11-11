from tkinter import*
import tkinter.messagebox as box
window = tk()
window.title('message box example')
def dialog():
    var = box.askyesno('message box', 'proceed?')
    if var == 1:
        box.showinfo('yes box', 'proceeding...')
    else:
        box.showwarning('no box', 'cancelling...')
btn = button(window, text = 'click', command=dialog)
btn.pack(padx=150, pady=50)
window.mainloop()
