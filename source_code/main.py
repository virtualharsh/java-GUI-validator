from tkinter import *
from tkinter import filedialog as fd
from tkinter.ttk import *
import os
import filecmp
from pathlib import Path


filename=""

def show():
        # packing the objects
        inputLabel.pack(side=TOP,pady=10)
        textInput.pack(side=TOP)
        expectedLabel.pack(side=TOP,pady=10)
        textexpected.pack(side=TOP)
        checkButton.pack(side=TOP,pady=20)
        status.pack(side=TOP,pady=10)

def check():
    if(textInput.get(1.0, "end-1c")==""):
        strStatus.set("no input provided")
    else:
        inp = textInput.get(1.0, "end-1c")
        os.system(f'javac "{filename}"')
        f = filename.split('.')[0]
        f = f.split('/')[len(f.split('/'))-1]
        os.system(f'java {f} {inp} > output.txt')

        ex = textexpected.get(1.0, "end-1c")
        ex+="\n"
        output = Path('output.txt').read_text()

        if(ex==output):
            strStatus.set("LOGICAL SUCCESS")
        else:
            strStatus.set("LOGICAL ERROR ")
        # os.remove('demo.class')
        os.remove('output.txt')

def showFileDialog():
    global filename
    filename = fd.askopenfilename()
    if filename!="":
        str.set("selected file : " + filename)
        show()

# initializing the root
root = Tk()
root.title("Java Testcase Validator")
root.geometry('750x500+100+100')
root.resizable(False,False)


# adding elements on root
str = StringVar()
str.set("No input files selected")

# label for displaying path
label = Label(textvariable =str)

# styling button with style class
st = Style()
st.configure('W.TButton', font= ('Arial', 10, 'bold'),foreground='Green')
# button
selectButton = Button(text ="Select your input file",style = 'W.TButton', command = showFileDialog)

selectButton.pack(side=TOP,pady=20)
label.pack(side=TOP,pady=10)

# label for input file
inputLabel =  Label(text = "Input a testcase below",font=("",10))
textInput = Text(root, height = 1, width = 52)

expectedLabel =  Label(text = "Input a expected output for given input",font=("",10))
textexpected = Text(root, height = 1, width = 52)

# check button 
checkButton = Button(text ="Check the code !",style = 'W.TButton', command = check)
strStatus = StringVar()
strStatus.set("")
# label for displaying path
status = Label(textvariable =strStatus)
root.mainloop()