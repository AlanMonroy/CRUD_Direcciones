from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("450x400")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 400,
    width = 450,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    225.0, 200.0,
    image=background_img)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    294.5, 156.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry0.place(
    x = 189.0, y = 144,
    width = 211.0,
    height = 23)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    294.5, 196.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry1.place(
    x = 189.0, y = 184,
    width = 211.0,
    height = 23)

entry2_img = PhotoImage(file = f"img_textBox2.png")
entry2_bg = canvas.create_image(
    294.5, 236.5,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry2.place(
    x = 189.0, y = 224,
    width = 211.0,
    height = 23)

entry3_img = PhotoImage(file = f"img_textBox3.png")
entry3_bg = canvas.create_image(
    294.5, 274.5,
    image = entry3_img)

entry3 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry3.place(
    x = 189.0, y = 262,
    width = 211.0,
    height = 23)

entry4_img = PhotoImage(file = f"img_textBox4.png")
entry4_bg = canvas.create_image(
    294.5, 312.5,
    image = entry4_img)

entry4 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry4.place(
    x = 189.0, y = 300,
    width = 211.0,
    height = 23)

entry5_img = PhotoImage(file = f"img_textBox5.png")
entry5_bg = canvas.create_image(
    294.5, 116.5,
    image = entry5_img)

entry5 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry5.place(
    x = 189.0, y = 104,
    width = 211.0,
    height = 23)

entry6_img = PhotoImage(file = f"img_textBox6.png")
entry6_bg = canvas.create_image(
    294.5, 36.5,
    image = entry6_img)

entry6 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry6.place(
    x = 189.0, y = 24,
    width = 211.0,
    height = 23)

entry7_img = PhotoImage(file = f"img_textBox7.png")
entry7_bg = canvas.create_image(
    294.5, 76.5,
    image = entry7_img)

entry7 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry7.place(
    x = 189.0, y = 64,
    width = 211.0,
    height = 23)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 50, y = 348,
    width = 140,
    height = 28)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 260, y = 348,
    width = 140,
    height = 28)

img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b2.place(
    x = 155, y = 348,
    width = 140,
    height = 28)

window.resizable(False, False)
window.mainloop()
