from cryptography.fernet import Fernet

file = open('key','rb')
key = file.read()
file.close()

encrypted= b'gAAAAABhWagpBDFWx4RPCdlIvgWuN-wTN3JG7dASCehUOha5w-7ZjztGro5ktcV0LmSlX2QKcPqqBZhXFzjorT30-mbpjp6IssTybfNFUEvOV1u6lrtMVookn9QypUR8jwEg18gnfjKp'

f = Fernet(key)
decrypted = f.decrypt(encrypted)
print(decrypted)
