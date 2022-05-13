from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os

root = Tk()
root.minsize(650, 650)
root.maxsize(650, 650)

openImage = ImageTk.PhotoImage(Image.open("open.png"))
saveImage = ImageTk.PhotoImage(Image.open("save.png"))

runImage = (Image.open("run.png"))
ResizedRunImage = runImage.resize((25,25), Image.ANTIALIAS)
NewResizedRunImage = ImageTk.PhotoImage(ResizedRunImage)


labelFileName = Label(root, text="file name")
labelFileName.place(relx = 0.28, rely = 0.03, anchor=CENTER)

InputFileName = Entry(root)
InputFileName.place(relx = 0.46, rely = 0.03, anchor=CENTER)

MyText = Text(root, height=35, width=80)
MyText.place(relx=0.5, rely= 0.55, anchor=CENTER)

name = " "
def openFile():
    global name
    InputFileName.delete(0, END)
    MyText.delete(1.0, END)
    HTMLFile = filedialog.askopenfilename(title = "Open Html File", filetypes = (("HTMLFile", "*.html"),))
    name = os.path.basename(HTMLFile)
    formatedName = name.split(".")[0]
    InputFileName.insert(END, formatedName)
    root.title(formatedName)
    HTMLFile = open(name, "r")
    Paragraph = HTMLFile.read()
    MyText.insert(END, Paragraph)
    
def save():
    print("save")
    
def run():
    print("run")

openButton = Button(root, image=openImage, text="Open File", command=openFile)
openButton.place(relx = 0.05, rely = 0.03, anchor=CENTER)

saveButton = Button(root, image=saveImage, text="Save File", command=save)
saveButton.place(relx = 0.11, rely = 0.03, anchor=CENTER)

RunButton = Button(root, image=NewResizedRunImage, text="Run File", command=run)
RunButton.place(relx = 0.17, rely = 0.03, anchor=CENTER)

root.mainloop()
