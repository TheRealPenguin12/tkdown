from tkinter.ttk import *
from tkinter import *
from PIL import Image as PILImage
from PIL import ImageTk
import re

def LoadMarkdown(window, file):
    with open(file) as md:
        pass
class Window(Tk):
    def __init__(self, title="Tk", size=[500, 400], pos=[100, 100]):
        super().__init__()
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}+{pos[0]}+{pos[1]}")

        
class Bold(Label):
    def __init__(self, window, text="", size=10):
        super().__init__(window, text=text, font=("Sans Serif", size, "bold"))
        
class Italic(Label):
    def __init__(self, window, text="", size=10):
        super().__init__(window, text=text, font=("Sans Serif", size, "italic"))

        
class H1(Label):
    def __init__(self, window, text="", size=40):
        super().__init__(window, text=text, font=("Sans Serif", size, "bold"))
        
class H2(Label):
    def __init__(self, window, text="", size=35):
        super().__init__(window, text=text, font=("Sans Serif", size))
        
class H3(Label):
    def __init__(self, window, text="", size=30):
        super().__init__(window, text=text, font=("Sans Serif", size))
        
class H4(Label):
    def __init__(self, window, text="", size=25):
        super().__init__(window, text=text, font=("Sans Serif", size))
        
class H5(Label):
    def __init__(self, window, text="", size=20):
        super().__init__(window, text=text, font=("Sans Serif", size))
        
class H6(Label):
    def __init__(self, window, text="", size=15):
        super().__init__(window, text=text, font=("Sans Serif", size))

        
class Strong(Label):
    def __init__(self, window, text="", size=10):
        super().__init__(window, text=text, font=("Sans Serif", size, "bold italic"))

class Image(Label):
    def __init__(self, window, path, size=None):
        if size:
            self.pil_img = PILImage.open(path).resize(size, PILImage.ANTIALIAS)
        else:
            self.pil_img = PILImage.open(path)
        self.tk_img = ImageTk.PhotoImage(self.pil_img)
        super().__init__(window, image=self.tk_img)
        
class Text(Label):
    def __init__(self, window, text="", size=10, font="Sans Serif"):
        super().__init__(window, text=text, font=(font, size))

window = Window()
LoadMarkdown(window, "README.md").pack()
window.mainloop()
