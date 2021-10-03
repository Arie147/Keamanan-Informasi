from cryptography.fernet import Fernet

key = Fernet.generate_key()

file = open('key','wb')
file.write(key)
file.close()
print(key)
