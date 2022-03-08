from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("1366x768")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 768,
    width = 1366,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    683.0, 384.0,
    image=background_img)

img0 = PhotoImage(file = f"barra_menu.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat",activebackground="#16660A")

b0.place(
    x = 5, y = 5,
    width = 90,
    height = 90)

window.resizable(False, False)
window.mainloop()
