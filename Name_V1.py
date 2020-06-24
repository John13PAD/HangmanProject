from tkinter import *

class username:
    def __init__(self, parent):
        background = "#EECFBB"
        
        self.username_frame = Frame(bg = background, pady = 10)
        self.username_frame.grid()        
        
        #Main header
        self.username_label= Label(self.username_frame, text = "Enter your username", fg = "#FAF0E4", bg = background, font=("Lottes Handwriting", 19, "bold"),
                                                               pady=10, padx=10)
        self.username_label.grid(row = 1, column=0)
        
        #Entry box for username
        self.username_entry= Entry(self.username_frame, width = 20, font = ("Century Gothic", "14", ))
        self.username_entry.grid(row = 3)        
        
        #Gets username from entry box
        
        
if __name__ == "__main__":
    root = Tk()
    root.title("Hangman")
    something = username(root)
    root.mainloop()