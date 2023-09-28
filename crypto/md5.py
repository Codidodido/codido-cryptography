import hashlib

def encode(string):
    return hashlib.md5(string.encode()).hexdigest()

def decode(string):
    return "MD5 is one way enctyption"

def byte_encode(byte):
    return hashlib.md5(byte.encode())