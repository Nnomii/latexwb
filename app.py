import tkinter as tk
from PIL import ImageTk, Image
import sympy as sp
import sys
from threading import Thread


# Updates the image field to inform the user that the expression image is generating
def generate(event=None):
    image.configure(image='')
    image.configure(text='Generating...')


# Make image command (transforms latex input into a resulting expression image)
def make_image(event=None):
    try:
        sp.preview('\Huge $' + latex_entry.get() + '$', viewer='file', filename='images/res.png')
        res = ImageTk.PhotoImage(Image.open('images/res.png'))
        image.configure(text='')
        image.configure(image=res)
        image.image = res
    except Exception as e:
        # An exception at this point means that there is a syntax error in the user's latex input
        image.configure(image='')
        image.configure(text=str(e).split(')')[-1].replace(r'\r\n', '\n')) # Displays the latex error


# Command tied to the convert button to start the image creation process
def convert(event=None):
    t1 = Thread(target=generate)
    t2 = Thread(target=make_image)
    t1.start()
    t2.start()


# Initialise window
root = tk.Tk()
root.option_add('*font', 'Lato')
root.title('Latex Whiteboard')
root.geometry('900x400')
root.iconphoto(False, ImageTk.PhotoImage(Image.open('images/x_icon.png')))
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
root.bind('<Return>', convert)

# Resulting expression image
result_frame = tk.Frame(root)
result_frame.grid(column=1, row=0, sticky=tk.N, pady=150)
image = tk.Label(result_frame)
image.pack()

root.mainloop()
