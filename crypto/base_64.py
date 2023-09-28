import base64

def encode(string):
    string_bytes = string.encode('utf-8')
    result = base64.b64encode(string_bytes).decode('utf-8')
    return result

def decode(encoded_string):
    try:
        # Decode the Base64 encoded string
        decoded_bytes = base64.b64decode(encoded_string.encode('utf-8'))
        
        # Convert the bytes to a string
        decoded_string = decoded_bytes.decode('utf-8')
        
        return decoded_string
    except Exception as e:
        # Handle decoding errors
        return f"Decoding error: {str(e)}"