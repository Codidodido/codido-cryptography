import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import scrolledtext
import tkinter.font as tkfont
from crypto import base_64, binary, caesar, codido, hex, md5, morse, sha1, sha3, stegan

def return_result(entry, text):
    entry.configure(state="normal")
    entry.delete(0, tk.END)
    entry.insert(0, text)
    entry.configure(state="readonly")

def update_log_bar(text):
    log_bar.insert(tk.END,text+"\n")
    log_bar.yview(tk.END)

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
win.geometry('740x360')

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
eraser_button = ttk.Button(result_frame, text="Eraser", command=eraser)
eraser_button.pack(side='left', padx=5)

def encode_image():
    input_file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")])
    output_file_path = filedialog.asksaveasfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")],defaultextension=".png")
    secret_text = stegan.encode(input_file_path, output_file_path ,stegan_input.get())
    return_result(result_display, f"Text encoded successfully in image. Path: {output_file_path}!")

def decode_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")])
    decoded_text = stegan.decode(file_path)
    return_result(result_display, decoded_text)

# Create a frame for the steganography section
stegano_frame = ttk.LabelFrame(win,text="Steganography")
stegano_frame.pack(side='left', pady=10, padx=10,fill="x")

# Create labels and entries for steganography
encode_label = ttk.Label(stegano_frame, text="Secret Text:")
encode_label.grid(row=1, column=0, padx=(0, 5))

stegan_input = ttk.Entry(stegano_frame)
stegan_input.grid(row=1, column=1, columnspan=2, sticky='ew')

# Create an encode button
encode_button = ttk.Button(stegano_frame, text="Encrypt Image", command=encode_image)
encode_button.grid(row=2, column=0, padx=(0, 5))

# Create a decode button
decode_button = ttk.Button(stegano_frame, text="Decode Image", command=decode_image)
decode_button.grid(row=2, column=1, padx=(0, 5))


def generate_file():
    file_path = filedialog.asksaveasfilename(filetypes=[("Codido Files", "*.codido")],defaultextension=".codido")
    secretkey = codido.generate_key()
    codido.encode(file_path," ",secretkey)
    secretkey_input.delete(0, tk.END)
    secretkey_input.insert(0, secretkey)
    update_log_bar(f"o> file generated.\nPath: {file_path}\nSecret key: {secretkey}")
    return_result(file_path_input,file_path)

def modify_file():
    try:
        secret_key = secretkey_input.get()
        file_path = file_path_input.get()
        if file_path is None or file_path == "":
            return 0
        secret_data = codido.encode(file_path,codido_input.get("0.0", "end-1c"),secret_key)
        update_log_bar("o> file modified")
    except Exception as e:
        update_log_bar("o> "+str(e))

def decode_file():
    try:
        secret_key = secretkey_input.get()
        file_path = filedialog.askopenfilename(filetypes=[("Codido Files", "*.codido")],defaultextension=".codido")
        if file_path is None or file_path == "":
            return 0
        else:
            secret_data = codido.decode(file_path,secret_key)
            return_result(result_display,secret_data)
            update_log_bar("o> file decoded")
            return_result(file_path_input,file_path)
    except Exception as e:
        update_log_bar("o> "+str(e))

# Create a LabelFrame for the Codidodido section
codidodido_frame = ttk.LabelFrame(win, text="Codidodido File")
codidodido_frame.pack(side='right', pady=10, padx=10, fill="both", expand=True)

# Create labels and entries
generate_button = ttk.Button(codidodido_frame, text="Generate File", command=generate_file)
generate_button.grid(row=0, column=0, padx=(0, 5),sticky="w")

secretkey_label = ttk.Label(codidodido_frame, text="Secret Key:")
secretkey_label.grid(row=0, column=1, padx=(0, 5))

secretkey_input = ttk.Entry(codidodido_frame)
secretkey_input.grid(row=0, column=2, padx=(0, 5),sticky="ew")


encode_label = ttk.Label(codidodido_frame, text="Secret Text:")
encode_label.grid(row=1, column=1, padx=(0, 5), sticky="w")

codido_input = tk.Text(codidodido_frame, height=5, width=1)
codido_input.grid(row=1, column=2,rowspan=3,columnspan=2, padx=(0, 5), sticky="ew")

# Create buttons
codido_encode_button = ttk.Button(codidodido_frame, text="Encode File", command=modify_file)
codido_encode_button.grid(row=1, column=0, padx=(0, 5), sticky="w")

codido_decode_button = ttk.Button(codidodido_frame, text="Decode File", command=decode_file)
codido_decode_button.grid(row=2, column=0, padx=(0, 5), sticky="w")

file_path_input = ttk.Entry(codidodido_frame,width=12, text="File: ")
file_path_input.grid(row=3, column=0, padx = (0, 5), sticky="w")

# Create a ScrolledText widget\
custom_font = tkfont.Font(family="Helvetica", size=8)
log_bar = scrolledtext.ScrolledText(codidodido_frame, width=25, height=7, wrap=tk.WORD,bg="black",fg="white",font=custom_font)
log_bar.grid(row=0,column=4,rowspan=4,columnspan = 2,padx=(0,5))



# Start the main loop
win.mainloop()
