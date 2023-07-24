# Code of Text Editor using Python......


# Importing Required libraries & Modules
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

class TextEditor:

  # Defining Constructor
  def __init__(self,root):
    self.root = root
    self.root.title("Text Editor")
    self.root.geometry("1200x700+200+150")
    self.filename = None
    self.title = StringVar()
    self.status = StringVar()

    self.titlebar = Label(self.root,textvariable=self.title,font=("times new roman",15,"bold"),bd=2,relief=GROOVE)
    self.titlebar.pack(side=TOP,fill=BOTH)
    self.settitle()

    self.statusbar = Label(self.root,textvariable=self.status,font=("times new roman",15,"bold"),bd=2,relief=GROOVE)
    self.statusbar.pack(side=BOTTOM,fill=BOTH)
    self.status.set("Welcome To Text Editor")

    self.menubar = Menu(self.root,font=("times new roman",15,"bold"),activebackground="skyblue")
    self.root.config(menu=self.menubar)

    self.filemenu = Menu(self.menubar,font=("times new roman",12,"bold"),activebackground="skyblue",tearoff=0)
    self.filemenu.add_command(label="New",accelerator="Ctrl+N",command=self.newfile)
    self.filemenu.add_command(label="Open",accelerator="Ctrl+O",command=self.openfile)
    self.filemenu.add_command(label="Save",accelerator="Ctrl+S",command=self.savefile)
    self.filemenu.add_command(label="Save As",accelerator="Ctrl+A",command=self.saveasfile)
    self.filemenu.add_separator()
    self.filemenu.add_command(label="Exit",accelerator="Ctrl+E",command=self.exit)
    self.menubar.add_cascade(label="File", menu=self.filemenu)


    self.editmenu = Menu(self.menubar,font=("times new roman",12,"bold"),activebackground="skyblue",tearoff=0)
    self.editmenu.add_command(label="Cut",accelerator="Ctrl+X",command=self.cut)
    self.editmenu.add_command(label="Copy",accelerator="Ctrl+C",command=self.copy)
    self.editmenu.add_command(label="Paste",accelerator="Ctrl+V",command=self.paste)
    self.editmenu.add_separator()
    self.editmenu.add_command(label="Undo",accelerator="Ctrl+U",command=self.undo)
    self.menubar.add_cascade(label="Edit", menu=self.editmenu)


    self.helpmenu = Menu(self.menubar,font=("times new roman",12,"bold"),activebackground="skyblue",tearoff=0)
    self.helpmenu.add_command(label="About",command=self.infoabout)
    self.menubar.add_cascade(label="Help", menu=self.helpmenu)


    scrol_y = Scrollbar(self.root,orient=VERTICAL)
    self.txtarea = Text(self.root,yscrollcommand=scrol_y.set,font=("times new roman",15,"bold"),state="normal",relief=GROOVE)
    scrol_y.pack(side=RIGHT,fill=Y)
    scrol_y.config(command=self.txtarea.yview)
    self.txtarea.pack(fill=BOTH,expand=1)

    self.shortcuts()

  def settitle(self):
    if self.filename:
      self.title.set(self.filename)
    else:
      self.title.set("Untitled")


  def newfile(self,*args):
    self.txtarea.delete("1.0",END)
    self.filename = None
    self.settitle()
    self.status.set("New File Created")

    # Defining Open File Funtion
  def openfile(self,*args):
    try:
      self.filename = filedialog.askopenfilename(title = "Select file",filetypes = (("All Files","*.*"),("Text Files","*.txt"),("Python Files","*.py")))
      if self.filename:
        infile = open(self.filename,"r")
        self.txtarea.delete("1.0",END)
        for line in infile:
          self.txtarea.insert(END,line)
        infile.close()
        self.settitle()
        self.status.set("Opened Successfully")
    except Exception as e:
      messagebox.showerror("Exception",e)

  # Defining Save File Funtion
  def savefile(self,*args):
    try:
      if self.filename:
        data = self.txtarea.get("1.0",END)
        outfile = open(self.filename,"w")
        outfile.write(data)
        outfile.close()
        self.settitle()
        self.status.set("Saved Successfully")
      else:
        self.saveasfile()
    except Exception as e:
      messagebox.showerror("Exception",e)


  # Defining Save As File Funtion
  def saveasfile(self,*args):
    try:
      untitledfile = filedialog.asksaveasfilename(title = "Save file As",defaultextension=".txt",initialfile = "Untitled.txt",filetypes = (("All Files","*.*"),("Text Files","*.txt"),("Python Files","*.py")))
      data = self.txtarea.get("1.0",END)
      outfile = open(untitledfile,"w")
      outfile.write(data)
      outfile.close()
      self.filename = untitledfile
      self.settitle()
      self.status.set("Saved Successfully")
    except Exception as e:
      messagebox.showerror("Exception",e)

  # Defining Exit Funtion
  def exit(self,*args):
    op = messagebox.askyesno("WARNING","Your Unsaved Data May be Lost!!")
    if op>0:
      self.root.destroy()
    else:
      return

  # Defining Cut Funtion
  def cut(self,*args):
    self.txtarea.event_generate("<<Cut>>")

  # Defining Copy Funtion
  def copy(self,*args):
          self.txtarea.event_generate("<<Copy>>")

  # Defining Paste Funtion
  def paste(self,*args):
    self.txtarea.event_generate("<<Paste>>")

  # Defining Undo Funtion
  def undo(self,*args):
    try:
      if self.filename:
        self.txtarea.delete("1.0",END)
        infile = open(self.filename,"r")
        for line in infile:
          self.txtarea.insert(END,line)
        infile.close()
        self.settitle()
        self.status.set("Undone Successfully")
      else:
        self.txtarea.delete("1.0",END)
        self.filename = None
        self.settitle()
        self.status.set("Undone Successfully")
    except Exception as e:
      messagebox.showerror("Exception",e)

  # Defining About Funtion
  def infoabout(self):
    messagebox.showinfo("About Text Editor","A Simple Text Editor\nCreated using Python.")

  # Defining shortcuts Funtion
  def shortcuts(self):
    self.txtarea.bind("<Control-n>",self.newfile)
    self.txtarea.bind("<Control-o>",self.openfile)
    self.txtarea.bind("<Control-s>",self.savefile)
    self.txtarea.bind("<Control-a>",self.saveasfile)
    self.txtarea.bind("<Control-e>",self.exit)
    self.txtarea.bind("<Control-x>",self.cut)
    self.txtarea.bind("<Control-c>",self.copy)
    self.txtarea.bind("<Control-v>",self.paste)
    self.txtarea.bind("<Control-u>",self.undo)

root = Tk()
TextEditor(root)
root.mainloop()
