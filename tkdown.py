from tkinter.ttk import *
from tkinter import *

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
        
window = Window()
var1 = Bold(window, "Hi")
var1.pack()
var2 = Strong(window, text="Hi")
var2.pack()
H1(window, text="Hi").pack()
H2(window, text="Hi").pack()
H3(window, text="Hi").pack()
H4(window, text="Hi").pack()
H5(window, text="Hi").pack()
H6(window, text="Hi").pack()
window.mainloop()
