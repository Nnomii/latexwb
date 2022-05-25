# The info screen displaying relevant information along with the version number
import tkinter

global displayed
displayed = None


def on_close(screen):
    global displayed
    displayed = None
    screen.destroy()


def display(root):
    global displayed
    if displayed is not None:
        displayed.lift()
    else:
        info_screen = tkinter.Toplevel(root)
        info_screen.resizable(False, False)
        info_screen.option_add('*font', 'Lato')
        info_screen.title('Info')
        info_screen.geometry('600x300')
        info_screen.iconbitmap('images/x_icon.ico')
        info_screen.protocol('WM_DELETE_WINDOW', lambda x=info_screen: on_close(x))
        displayed = info_screen
