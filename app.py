import tkinter as tk
from PIL import ImageTk, Image
import sympy as sp
import sys


# Convert command (converts latex input and updates the resulting expression image)
def convert():
    try:
        sp.preview('\Huge $' + latex_entry.get() + '$', viewer='file', filename='images/res.png')
        res = ImageTk.PhotoImage(Image.open('images/res.png'))
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
root.geometry('900x400')
icon = ImageTk.PhotoImage(Image.open('images/x_icon.png'))
root.iconphoto(False, icon)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)

# Insert logo
logoframe = tk.Frame(root, bg='white')
logoframe.grid(column=0, row=0, sticky=tk.N)
logo = ImageTk.PhotoImage(Image.open('images/latex_whiteboard.png'))
logo_label = tk.Label(logoframe, image=logo, borderwidth=0)
logo_label.image = logo
logo_label.grid(column=0, row=0, sticky=tk.N, pady=100)

# Label for latex entry
enter_latex_string_image = ImageTk.PhotoImage(Image.open('images/enter_latex_expression.png'))
latex_label = tk.Label(root, image=enter_latex_string_image, width=350)
latex_label.image = enter_latex_string_image
latex_label.grid(column=1, row=0, sticky=tk.N, pady=5)

# Latex entry
latex_entry = tk.Entry(root, width=70)
latex_entry.grid(column=1, row=0, sticky=tk.N, pady=40)

# Convert button
convert_image = ImageTk.PhotoImage(Image.open('images/convert.png'))
convert_button = tk.Button(root, image=convert_image, command=convert, borderwidth=0.5)
convert_button.image = convert_image
convert_button.grid(column=1, row=0, sticky=tk.N, pady=80)

# Resulting expression image
result_frame = tk.Frame(root)
result_frame.grid(column=1, row=0, sticky=tk.N, pady=150)
image = tk.Label(result_frame)
image.pack()

root.mainloop()
