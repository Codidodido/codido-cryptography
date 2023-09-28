import hashlib

def encode(string):
    return hashlib.sha1(string.encode()).hexdigest()

def decode(string):
    return "SHA1 is one way enctyption"