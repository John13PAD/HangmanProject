from tkinter import *

class username:
    def __init__(self, parent):
        background = "#EEB8B8"
        
        self.username_frame = Frame(bg = background, pady = 10)
        self.username_frame.grid()        
        
        #Main header
        self.save_error_label = Label(self.username_frame, text = "Please enter your username", fg = "maroon", bg = background, font=("Lottes Handwriting", 19, "bold"),
                                                               pady=10, padx=10)
        self.save_error_label.grid(row = 1, column=0)
        
        #Entry box for usernamehtee
        self.to_convert_entry = Entry(self.username_frame, width = 20, font = ("Century Gothic", "14", ))
        self.to_convert_entry.grid(row = 3)        
if __name__ == "__main__":
    root = Tk()
    root.title("Hangman")
    something = username(root)
    root.mainloop()