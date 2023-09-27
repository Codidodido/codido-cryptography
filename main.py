import tkinter as tk
from tkinter import ttk
import hashlib
import morse
import base64

def return_result(entry, text):
    entry.configure(state="normal")
    entry.delete(0, tk.END)
    entry.insert(0, text)
    entry.configure(state="readonly")

def show_caesar():
    caesar_input.configure()

def caesar(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)
    return result

def morse_code(string):
    return morse.encode(string)

def binary(string):
    result = ""
    for char in string:
        binary_char = bin(ord(char))[2:]  # Convert character to binary (remove '0b' prefix)
        result += "0"+binary_char+" "
    return result

def base64_encode(string):
    string_bytes = string.encode('utf-8')
    result = base64.b64encode(string_bytes).decode('utf-8')
    return result

def to_hex(string):
    string_bytes = string.encode('utf-8')
    return string_bytes.hex()

def md5_hash(string):
    return hashlib.md5(string.encode()).hexdigest()

def sha1_hash(string):
    return hashlib.sha1(string.encode()).hexdigest()

def sha3_hash(string):
    return hashlib.sha3_512(string.encode()).hexdigest()

def encode():
    encrypt_mode = str(radio.get())
    text = str(encode_input.get())
    encrypt_text = ""
    
    if encrypt_mode == "1":
        encrypt_text = md5_hash(text)
    elif encrypt_mode == "2":
        encrypt_text = sha1_hash(text)
    elif encrypt_mode == "3":
        encrypt_text = sha3_hash(text)
    elif encrypt_mode == "5":
        encrypt_text = morse_code(text)
    elif encrypt_mode == "6":
        encrypt_text = binary(text)
    elif encrypt_mode == "7":
        encrypt_text = base64_encode(text)
    elif encrypt_mode == "8":
        encrypt_text = to_hex(text)
    
    return_result(encode_result, encrypt_text)

def decode():
    pass

win = tk.Tk()
win.title("Encryption")
win.geometry('640x360')

# Create a style for ttk widgets (to apply a modern theme)
style = ttk.Style()
style.theme_use('clam')

# Create a frame for radio buttons
radio_frame = ttk.Frame(win)
radio_frame.pack(pady=10, padx=10, fill='x')

# Create a label for encryption type
type_label = ttk.Label(radio_frame, text="Encryption Type:")
type_label.pack(side='left')

# Create radio buttons for encryption types
radio = tk.IntVar()
radio_md5 = ttk.Radiobutton(radio_frame, text="MD5", variable=radio, value=1)
radio_sha1 = ttk.Radiobutton(radio_frame, text="SHA1", variable=radio, value=2)
radio_sha3 = ttk.Radiobutton(radio_frame, text="SHA3_512", variable=radio, value=3)
radio_morse = ttk.Radiobutton(radio_frame, text="Morse", variable=radio, value=5)
radio_binary = ttk.Radiobutton(radio_frame, text="Binary", variable=radio, value=6)
radio_base64 = ttk.Radiobutton(radio_frame, text="Base64", variable=radio, value=7)
radio_hex = ttk.Radiobutton(radio_frame, text="Hex", variable=radio, value=8)
radio_md5.pack(side='left', padx=5)
radio_sha1.pack(side='left', padx=5)
radio_sha3.pack(side='left', padx=5)
radio_morse.pack(side='left', padx=5)
radio_binary.pack(side='left', padx=5)
radio_base64.pack(side='left', padx=5)
radio_hex.pack(side='left', padx=5)

# Create an input entry for encoding
encode_frame = ttk.Frame(win)
encode_frame.pack(pady=10, padx=10, fill='x')
encode_label = ttk.Label(encode_frame, text="Input:")
encode_label.pack(side='left')
encode_input = ttk.Entry(encode_frame)
encode_input.pack(side='left', fill='x', expand=True, padx=5)
encode_button = ttk.Button(encode_frame, text="Encode", command=encode)
encode_button.pack(side='left', padx=5)

# Create an input entry for decoding
decode_frame = ttk.Frame(win)
decode_frame.pack(pady=10, padx=10, fill='x')
decode_label = ttk.Label(decode_frame, text="Input:")
decode_label.pack(side='left')
decode_input = ttk.Entry(decode_frame)
decode_input.pack(side='left', fill='x', expand=True, padx=5)
decode_button = ttk.Button(decode_frame, text="Decode", command=decode)
decode_button.pack(side='left', padx=5)

# Create a result entry for displaying encoded/decoded text
result_frame = ttk.Frame(win)
result_frame.pack(pady=10, padx=10, fill='x')
result_label = ttk.Label(result_frame, text="Result:")
result_label.pack(side='left')
encode_result = ttk.Entry(result_frame, state="disabled")
encode_result.pack(side='left', fill='x', expand=True, padx=5)

# Start the main loop
win.mainloop()
