from tkinter import *

mode = ""


def Encode():
    pass

def Decode():
    pass

win = Tk()
win.title("Encryption")
win.geometry('640x360')

radio = IntVar()
radioBox = Frame(win)
typeLabel =  Label(radioBox,text="Encryption type")
radioMD5 = Radiobutton(radioBox,text="MD5",variable=radio,value=1)
radioSHA = Radiobutton(radioBox,text="SHA",variable=radio,value=2)


encodeLabel = Label(win,text="Encode Input")
encodeInput = Entry(win)
encodeButton = Button(win,text="Encode",command=Encode)

decodeLabel = Label(win,text="Decode Input")
decodeInput = Entry(win)
decodeButton = Button(win,text="Decode",command=Decode)

radioBox.pack( side = TOP )
typeLabel.pack(side = TOP)
radioMD5.pack(side = LEFT)
radioSHA.pack(side = LEFT)

encodeLabel.pack()
encodeInput.pack()
encodeButton.pack()

decodeLabel.pack()
decodeInput.pack()
decodeButton.pack()

win.mainloop()
