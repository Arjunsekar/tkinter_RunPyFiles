"""
Created on Fri May  1 09:49:10 2020
@author: arjun sd
"""
import os
from tkinter import *
import tkinter as tk
from tkinter import messagebox as msg
from tkinter.ttk import Notebook
from tkinter.filedialog import askopenfilenames

global filez
def runFiles(input):
    os.system('python '+input)
    print(input+" Script ran successfully")
    msg.showinfo("Execution Successful", input+" Script ran successfully")
class InsGui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Batch Runs of py files")
        self.geometry("800x500")
        self.menu = tk.Menu(self, bg="lightgrey", fg="black")
        self.notebook = Notebook(self)
        main_tab = tk.Frame(self.notebook)
        self.notebook.add(main_tab,text="Main Page")
        self.notebook.pack(fill=tk.NONE, expand=1)
        self.list_of_scripts = tk.Text(main_tab, bg="white", fg="black")
        self.list_of_scripts.pack(side=tk.BOTTOM)
        self.select_button = tk.Button(self, text="SELECT THE PY FILES TO RUN", command=self.select)
        self.select_button.pack(side=tk.TOP)       
    def select(self):
        global filez
        filez = askopenfilenames(title='Choose files')
        self.tk.splitlist(filez)
        for i in filez:         
            runFiles(i)
        msg.showinfo("Execution Successful", "The Python script has ran successfully")
    
        

if __name__ == "__main__":
    insgui = InsGui()
    insgui.mainloop()
    