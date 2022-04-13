from tkinter import * # Import tkinter

class ScrollText:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Scroll Text Demo") # Set title

        frame1 = Frame(window)
        frame1.pack()
        scrollbar = Scrollbar(frame1)
        scrollbar.pack(side = BOTTOM, fill = X)
        text = Text(frame1, width = 40, height = 10, wrap = WORD,
                    xscrollcommand = scrollbar.set)
        text.pack()
        scrollbar.config(command = text.xview)

        window.mainloop() # Create an event loop

ScrollText() # Create GUI



