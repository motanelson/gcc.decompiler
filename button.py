import tkinter as tk
from tkinter import messagebox




class myapps:
    def __init__(self,root:tk.Tk):
        self.root=root
        self.root.title("user button")
        self.root.geometry("640x480")
        self.root.configure(background="black")
        self.label=tk.Label(background="white",foreground="black",text="   click me  ")
        self.label.pack(padx=10,pady=10)
        self.label.bind("<Button-1>",self.clicks)
    def clicks(self,event):
        messagebox.showinfo("hello world","exit me")
        self.root.quit()










root=tk.Tk()
apps=myapps(root)
root.mainloop()