import hashlib
from Crypto.Cipher import AES
import os
global sha1

def encryption(filename,key):
    iv =os.urandom(16)
    cypher= AES.new(key.encode("utf-8"),AES.MODE_CBC,iv)
    with open(filename, "rb") as f:
        unsafe_data= f.read()

    mixed_data= unsafe_data + b"\0" * (16-len(unsafe_data)%16)

    encrypt_data = cypher.encrypt(mixed_data)
    with open(filename + '.enc', 'wb') as f:
        f.write(iv)
        f.write(encrypt_data) 
    os.remove(filename)
    print("encryption complete")

def decryption(filename,key):
    with open(filename, 'rb') as f:
        iv = f.read(16)
        encrypt_code = f.read()
    cypher = AES.new(key.encode('utf-8'), AES.MODE_CBC,iv)
    mixed_data = cypher.decrypt(encrypt_code) 
    plaintext = mixed_data.rstrip(b'\0') 
    with open(filename[:-4], 'wb') as f:
        f.write(plaintext)
    os.remove(filename)
    print("decryption complete")



apofash=input("Would you like to encrypt or decrypt a file.\nInput encrypt or decrypt: ")


if (apofash=="encrypt"):
    key=input("Give the key for encryption: ")
    filename=input("Give the file you would like to encrypt: ")
    md5=hashlib.md5()
    key_enc= key.encode()
    md5.update(key_enc)
    hexedkey = md5.hexdigest()
    encryption(filename,hexedkey)
    
    
    

elif(apofash=="decrypt"):
    key=input("Give the key for decryption: ")
    filename=input("Give the file you would like to decrypt: ")
    md5=hashlib.md5()
    key_enc = key.encode()
    md5.update(key_enc)
    hexedkey = md5.hexdigest()
    decryption(filename,hexedkey)
    



else:
    print("Wrong answer was given")




