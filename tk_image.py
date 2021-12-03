from tkinter import*
window = tk()
window.title('image example')
img = photoimage(file='python.gif')
label = label(window, image=img, bg='yellow')
small_img = photoimage.subsample(img, x=2, y=2)
btn = button(window, image=small_img)

txt = text(window, width=25, height=7)
txt.image_create('1.0', 'python fun!')
txt.insert('1.1', 'python fun!')


can =\
canvas(window, width=100, height=100, bg='cyan')
can.create_image((50, 50), image=small_img)
can.create_line(0, 0, 100, 100, width=25, fill='yellow')

label.pack(side=top)
btn.pack(side=left, padx=10)
txt.pack(side=left)
can.pack(side=left, padx=10)


window.mainloop()
