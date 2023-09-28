def encode(string):
    result = ""
    for char in string:
        binary_char = bin(ord(char))[2:]  # Convert character to binary (remove '0b' prefix)
        result += "0"+binary_char+" "
    return result

def decode(string):
    binary_chars = string.split()  # Split the binary string into individual binary characters
    decoded_string = ""

    for binary_char in binary_chars:
        try:
            decimal_value = int(binary_char, 2)  # Convert binary to decimal
            decoded_char = chr(decimal_value)  # Convert decimal to character
            decoded_string += decoded_char
        except ValueError:
            # Handle invalid binary characters
            return "Decoding error: Invalid binary character"

    return decoded_string