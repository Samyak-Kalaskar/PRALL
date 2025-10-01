import hashlib

# initializing string
text = "SIPNA COET"

# SHA256
result = hashlib.sha256(text.encode())
print("The hexadecimal equivalent of SHA256 is : ")
print(result.hexdigest())
print()

# SHA384
result = hashlib.sha384(text.encode())
print("The hexadecimal equivalent of SHA384 is : ")
print(result.hexdigest())
print()

# SHA224
result = hashlib.sha224(text.encode())
print("The hexadecimal equivalent of SHA224 is : ")
print(result.hexdigest())
print()

# SHA512
result = hashlib.sha512(text.encode())
print("The hexadecimal equivalent of SHA512 is : ")
print(result.hexdigest())
print()

# SHA1
result = hashlib.sha1(text.encode())
print("The hexadecimal equivalent of SHA1 is : ")
print(result.hexdigest())