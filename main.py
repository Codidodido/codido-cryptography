from tkinter import *

import hashlib

def ReturnResult(entry,text):
    entry.configure(state="normal")
    entry.delete(0,END)
    entry.insert(0,text)
    entry.configure(state="readonly")


def MD5(string):
    return hashlib.md5(string.encode()).hexdigest()

def SHA1(string):
    return hashlib.sha1(string.encode()).hexdigest()

def Encode():
    encryptMode = str(radio.get())
    text = str(encodeInput.get())
    encryptText = ""
    if(encryptMode=="1"):
        encryptText = MD5(text)
    elif(encryptMode=="2"):
        encryptText = SHA1(text)
    ReturnResult(encodeResult,encryptText)

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

encodeBox = Frame(win)
encodeLabel = Label(encodeBox,text="Encode Input : ")
encodeInput = Entry(encodeBox)
encodeButton = Button(encodeBox,text="Encode",command=Encode)


decodeBox = Frame(win)
decodeLabel = Label(decodeBox,text="Decode Input")
decodeInput = Entry(decodeBox)
decodeButton = Button(decodeBox,text="Decode",command=Decode)

encodeResult = Entry(win,width=40,state="disabled")
decodeResult = Entry()
radioBox.pack( side = TOP )
typeLabel.pack(side = TOP)
radioMD5.pack(side = LEFT)
radioSHA.pack(side = LEFT)

encodeBox.pack()
encodeLabel.pack(side = LEFT)
encodeInput.pack(side = LEFT)
encodeButton.pack(side = LEFT)
encodeResult.pack()

decodeBox.pack()
decodeLabel.pack()
decodeInput.pack()
decodeButton.pack()

win.mainloop()
