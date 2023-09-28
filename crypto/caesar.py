def encode(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            # Determine whether the character is uppercase or lowercase
            is_upper = char.isupper()
            
            # Convert the character to its alphabetical index (0-25)
            char_index = ord(char.lower()) - ord('a')
            
            # Apply the Caesar shift and wrap around the alphabet
            shifted_index = (char_index + shift) % 26
            
            # Convert the shifted index back to a character
            shifted_char = chr(shifted_index + ord('a'))
            
            # Convert the character back to uppercase if it was originally uppercase
            if is_upper:
                shifted_char = shifted_char.upper()
            
            encrypted_text += shifted_char
        else:
            # Keep non-alphabetical characters unchanged
            encrypted_text += char
    
    return encrypted_text

def decode(encrypted_text, shift):
    # To decrypt, use a negative shift to reverse the encryption
    return encode(encrypted_text, -shift)
