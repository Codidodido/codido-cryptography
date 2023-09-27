from tkinter import *

import hashlib
import morse


def ReturnResult(entry,text):
    entry.configure(state="normal")
    entry.delete(0,END)
    entry.insert(0,text)
    entry.configure(state="readonly")

def showCaesar():
    caesarInput.configure()

def Caesar(string,shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters in plain text
        if (char.isupper()):
            result += chr((ord(char) + shift-65) % 26 + 65)
            # Encrypt lowercase characters in plain text
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)
    return result


def Morse(string):
    return morse.encode(string)

def Binary(string):
    result = ""
    for i in string:
        result += bin(ord(i))
    return result[2:]

def MD5(string):
    return hashlib.md5(string.encode()).hexdigest()

def SHA1(string):
    return hashlib.sha1(string.encode()).hexdigest()

def SHA3(string):
    return hashlib.sha3_512(string.encode()).hexdigest()

def Encode():
    encryptMode = str(radio.get())
    text = str(encodeInput.get())
    encryptText = ""
    if(encryptMode=="1"):
        encryptText = MD5(text)
    elif(encryptMode=="2"):
        encryptText = SHA1(text)
    elif(encryptMode=="3"):
        encryptText = SHA3(text)
    elif(encryptMode=="5"):
        encryptText = Morse(text)
    elif(encryptMode=="6"):
        encryptText = Binary(text)
    
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
radioSHA3 = Radiobutton(radioBox,text="SHA3_512",variable=radio,value=3)
radioCaesar = Radiobutton(radioBox,text="Caesar",variable=radio,value=4,command=showCaesar)
radioMorse = Radiobutton(radioBox,text="Morse",variable=radio,value=5)
radioBinary = Radiobutton(radioBox,text="Binary",variable=radio,value=6)
caesarInput = Entry(radioBox);


encodeBox = Frame(win)
encodeLabel = Label(encodeBox,text="Encode Input : ")
encodeInput = Entry(encodeBox)
encodeButton = Button(encodeBox,text="Encode",command=Encode)


decodeBox = Frame(win)
decodeLabel = Label(decodeBox,text="Decode Input")
decodeInput = Entry(decodeBox)
decodeButton = Button(decodeBox,text="Decode",command=Decode)

encodeResult = Entry(win,width=40,state="disabled")

radioBox.pack( side = TOP )
typeLabel.pack(side = TOP)
radioMD5.pack(side = LEFT)
radioSHA.pack(side = LEFT)
radioSHA3.pack(side=LEFT)
radioMorse.pack(side=LEFT)
radioBinary.pack(side=LEFT)

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
