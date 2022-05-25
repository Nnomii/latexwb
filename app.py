import tkinter as tk
import sympy as sp
import win32clipboard as clip
import win32con

from io import BytesIO
from PIL import ImageTk, Image
from threading import Thread
import screens.info

# Version number & global variables
version = 1.0
global image_exists
image_exists = False


# Updates the image field to inform the user that the expression image is generating
def generate(event=None):
    image.configure(image='')
    image.configure(text='Generating...')


# Make image command (transforms latex input into a resulting expression image)
def make_image(event=None):
    global image_exists

    try:
        # Add packages to the preamble to customise the latex configuration
        preamble = "\\documentclass{article}\n" \
                   "\\pagestyle{empty}\n" \
                   "\\usepackage{amsmath, amssymb, amsfonts, euler}\n" \
                   "\\begin{document}"
        sp.preview('\Huge $' + latex_entry.get() + '$', viewer='file', preamble=preamble, filename='images/res.png')

        # The resulting image is saved under res.png for easy future access
        res = ImageTk.PhotoImage(Image.open('images/res.png'))
        image.configure(text='')
        image.configure(image=res)
        image.image = res
        copy_button.grid()
        copy_label.grid_remove()
        image_exists = True

    except Exception as e:
        # An exception at this point means that there is a syntax error in the user's latex input
        image.configure(image='')
        image.configure(text=str(e).split(')')[-1].replace(r'\r\n', '\n'))  # Displays the latex error
        copy_button.grid_remove()
        copy_label.grid_remove()
        image_exists = False


# Command tied to the convert button to start the image creation process
def convert(event=None):
    generate_thread = Thread(target=generate)
    make_image_thread = Thread(target=make_image)
    generate_thread.start()
    make_image_thread.start()


# Command used to copy the displayed image to the clipboard
def copy(event=None):
    global image_exists
    if image_exists:
        output = BytesIO()
        res = Image.open('images/res.png')
        res.convert('RGB').save(output, 'BMP')
        data = output.getvalue()[14:]
        output.close()

        # Add converted image to the clipboard
        clip.OpenClipboard()
        clip.EmptyClipboard()
        clip.SetClipboardData(win32con.CF_DIB, data)
        clip.CloseClipboard()

        # Display success message
        copy_label.grid()


if __name__ == '__main__':
    # Initialise window
    root = tk.Tk()
    root.resizable(False, False)
    root.option_add('*font', 'Lato')
    root.title('Latex Whiteboard')
    root.geometry('900x400')
    root.iconphoto(False, ImageTk.PhotoImage(Image.open('images/x_icon.png')))
    root.iconbitmap('images/x_icon.ico')
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=3)

    # Insert logo
    logo_frame = tk.Frame(root, bg='white')
    logo_frame.grid(column=0, row=0, sticky=tk.N)
    logo = ImageTk.PhotoImage(Image.open('images/latex_whiteboard.png'))
    logo_label = tk.Label(logo_frame, image=logo, borderwidth=0)
    logo_label.image = logo
    logo_label.grid(column=0, row=0, sticky=tk.N, pady=90)

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

    # Copy button
    copy_image = ImageTk.PhotoImage(Image.open('images/copy.png'))
    copy_button = tk.Button(root, image=copy_image, command=copy, borderwidth=0.5)
    copy_button.image = copy_image
    copy_button.grid(column=1, row=0, sticky=tk.N, pady=280)
    copy_button.grid_remove()

    # Copy label
    copy_label = tk.Label(text='Image successfully copied!')
    copy_label.grid(column=1, row=0, sticky=tk.N, pady=320)
    copy_label.grid_remove()

    # Resulting expression image
    result_frame = tk.Frame(root)
    result_frame.grid(column=1, row=0, sticky=tk.N, pady=150)
    image = tk.Label(result_frame)
    image.pack()

    # Info button
    info_image = ImageTk.PhotoImage(Image.open('images/info.png'))
    info_button = tk.Button(root, image=info_image, command=lambda x=root: screens.info.display(x),
                            borderwidth=0, bg='white')
    info_button.image = info_image
    info_button.grid(column=0, row=0, sticky=tk.E, pady=340, padx=35)

    # Version text
    version_label = tk.Label(root, text='Version ' + str(version), bg='white')
    version_label.grid(column=0, row=0, sticky=tk.W, pady=347, padx=40)

    root.mainloop()
