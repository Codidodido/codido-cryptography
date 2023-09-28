def encode(string):
    string_bytes = string.encode('utf-8')
    return string_bytes.hex()

def decode(string):
    try:
        # Convert the hexadecimal string to bytes
        decoded_bytes = bytes.fromhex(string)
        
        # Convert the bytes to a string
        decoded_string = decoded_bytes.decode('utf-8')
        
        return decoded_string
    except Exception as e:
        # Handle decoding errors
        return f"Decoding error: {str(e)}"