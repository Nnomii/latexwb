import tkinter as tk
from PIL import ImageTk, Image
import sympy as sp
import sys


# Convert command (converts latex input and updates the resulting expression image)
def convert():
    try:
        sp.preview('\Huge $' + latex_entry.get() + '$', viewer='file', filename='images/res.png')
        res = ImageTk.PhotoImage(Image.open("images/res.png"))
        image.configure(text='')
        image.configure(image=res)
        image.image = res
    except Exception as e:
        image.configure(image='')
        image.configure(text=str(e).split(')')[-1].replace(r'\r\n', '\n'))


# Initialise window
root = tk.Tk()
root.option_add('*font', 'Lato')
root.title('Latex Whiteboard')
root.geometry('700x400')

# Label for latex entry
latex_label = tk.Label(root, text='Enter latex string:')
latex_label.pack()

# Latex entry
latex_entry = tk.Entry(root, width=70)
latex_entry.pack()

# Convert button
convert_button = tk.Button(root, text='Convert', command=convert)
convert_button.pack(pady=10)

# Resulting expression image
res = None
image = tk.Label(root, image=res)
image.pack(pady=10)

root.mainloop()
