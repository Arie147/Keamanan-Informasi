from cryptography.fernet import Fernet

file = open('key','rb')
key = file.read()
file.close()

message= "Saya sedang belajar keamanan informasi".encode()

f = Fernet(key)
encrypted = f.encrypt(message)
print(encrypted)
