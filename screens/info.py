# The info screen displaying relevant information along with the version number
import tkinter


def display(root):
    info_screen = tkinter.Toplevel(root)
    info_screen.resizable(False, False)
    info_screen.option_add('*font', 'Lato')
    info_screen.title('Info')
    info_screen.geometry('600x300')
    info_screen.iconbitmap('images/x_icon.ico')
