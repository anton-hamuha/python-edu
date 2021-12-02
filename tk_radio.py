from tkinter import*
import tkinter.messagebox as box
window = tk()
window.title('radio button example')
frame = frame(window)
book = stringvar()



radio_1 = radiobutton(frame, text = 'html5',\
                      variable=book, value='html5 in easy steps')
radio_2 = radiobutton(frame, text='css3 in easy steps',\
                      variable = book, value = 'css3 in easy steps')
radio_3 = radiobutton(frame, text='js',\
                      variable = book, value = 'javascript in easy steps')

radio_1.select()
def dialog():
    box.showinfo('selection',\
                 'your choice: \n' + book.get())
btn = button(frame, text = 'choose', command = dialog)
btn.pack(side=right, padx=5)
radio_1.pack(side=left)
radio_2.pack(side=left)
radio_3.pack(side=left)
frame.pack(padx=30, pady=30)


window.mainloop()
