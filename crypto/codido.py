from cryptography.fernet import Fernet
import struct

# Generate a random encryption key

def generate_key():
    return Fernet.generate_key()

# Encrypt secret data and encode it into a custom file format
def encode(file_path, secret_data, encryption_key):
    cipher_suite = Fernet(encryption_key)
    encrypted_data = cipher_suite.encrypt(secret_data.encode())
    
    with open(file_path, 'wb') as file:
        # Encode the encrypted data length as a 4-byte integer
        encoded_length = struct.pack('I', len(encrypted_data))
        file.write(encoded_length)

        # Write the encrypted data
        file.write(encrypted_data)

# Decrypt and decode secret data from the custom file format
def decode(file_path, encryption_key):
    cipher_suite = Fernet(encryption_key)
    with open(file_path, 'rb') as file:
        # Read the encoded length of the encrypted data
        encoded_length = file.read(4)
        data_length = struct.unpack('I', encoded_length)[0]

        # Read and decrypt the encrypted data
        encrypted_data = file.read(data_length)
        secret_data = cipher_suite.decrypt(encrypted_data)
        return secret_data.decode()
    
key = generate_key()
encode("sec.codidodido","Boooooof",key)
print(decode("sec.codidodido",key))