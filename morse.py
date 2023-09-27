# Define Morse code mappings
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----',
    ' ': '/'
}

# Encode a message to Morse code
def encode(message):
    message = message.upper()
    morse_code = ''
    for char in message:
        if char in morse_code_dict:
            morse_code += morse_code_dict[char] + ' '
        elif char == ' ':
            morse_code += ' '
    return morse_code

# Decode Morse code to a message
def decode(morse_code):
    morse_code = morse_code.split(' ')
    decoded_message = ''
    for symbol in morse_code:
        if symbol == '/':
            decoded_message += ' '
        else:
            char = [key for key, value in morse_code_dict.items() if value == symbol]
            if char:
                decoded_message += char[0]
    return decoded_message
