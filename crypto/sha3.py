import hashlib

def encode(string):
    return hashlib.sha3_512(string.encode()).hexdigest()

def decode(string):
    return "SHA3 is one way enctyption"