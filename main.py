import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from crypto import base_64, binary, caesar, codido, hex, md5, morse, sha1, sha3, stegan

def return_result(entry, text):
    entry.configure(state="normal")
    entry.delete(0, tk.END)
    entry.insert(0, text)
    entry.configure(state="readonly")

def eraser():
    encode_input.delete(0, tk.END)
    result_display.configure(state="normal")
    result_display.delete(0, tk.END)
    result_display.configure(state="readonly")
    decode_input.delete(0, tk.END)

def encode():
    encrypt_mode = str(radio.get())
    text = str(encode_input.get())
    encrypt_text = ""
    
    if encrypt_mode == "1":
        encrypt_text = md5.encode(text)
    elif encrypt_mode == "2":
        encrypt_text = sha1.encode(text)
    elif encrypt_mode == "3":
        encrypt_text = sha3.encode(text)
    elif encrypt_mode == "5":
        encrypt_text = morse.encode(text)
    elif encrypt_mode == "6":
        encrypt_text = binary.encode(text)
    elif encrypt_mode == "7":
        encrypt_text = base_64.encode(text)
    elif encrypt_mode == "8":
        encrypt_text = hex.encode(text)
    
    return_result(result_display, encrypt_text)

def decode():
    encrypt_mode = str(radio.get())
    text = str(decode_input.get())
    encrypt_text = ""
    
    if encrypt_mode == "1":
        encrypt_text = md5.decode(text)
    elif encrypt_mode == "2":
        encrypt_text = sha1.decode(text)
    elif encrypt_mode == "3":
        encrypt_text = sha3.decode(text)
    elif encrypt_mode == "5":
        encrypt_text = morse.decode(text)
    elif encrypt_mode == "6":
        encrypt_text = binary.decode(text)
    elif encrypt_mode == "7":
        encrypt_text = base_64.decode(text)
    elif encrypt_mode == "8":
        encrypt_text = hex.decode(text)
    
    return_result(result_display, encrypt_text)

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
result_display = ttk.Entry(result_frame, state="disabled")
result_display.pack(side='left', fill='x', expand=True, padx=5)

# Create a frame for the "Eraser" button
eraser_frame = ttk.Frame(win)
eraser_frame.pack(pady=10, padx=10, fill='x')
eraser_button = ttk.Button(eraser_frame, text="Eraser", command=eraser)
eraser_button.pack(side='left', padx=5)

def encode_image():
    input_file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")])
    output_file_path = filedialog.asksaveasfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")],defaultextension=".png")
    secret_text = stegan.encode(input_file_path, output_file_path ,encode_input.get())
    return_result(result_display, f"Text encoded successfully in image. Path: {output_file_path}!")

def decode_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")])
    decoded_text = stegan.decode(file_path)
    return_result(result_display, decoded_text)

# Create a frame for the steganography section
stegano_frame = ttk.Frame(win)
stegano_frame.pack(side='left', pady=10, padx=10,fill="x")

type_label = ttk.Label(stegano_frame, text="Steganography")
type_label.grid(row=0, column=0, pady=(0, 5))


# Create labels and entries for steganography
encode_label = ttk.Label(stegano_frame, text="Secret Text:")
encode_label.grid(row=1, column=0, padx=(0, 5))

encode_input = ttk.Entry(stegano_frame)
encode_input.grid(row=1, column=1, columnspan=2, sticky='ew')

# Create an encode button
encode_button = ttk.Button(stegano_frame, text="Encrypt Image", command=encode_image)
encode_button.grid(row=2, column=0, padx=(0, 5))

# Create a decode button
decode_button = ttk.Button(stegano_frame, text="Decode Image", command=decode_image)
decode_button.grid(row=2, column=1, padx=(0, 5))


# Start the main loop
win.mainloop()
