from cryptography.fernet import Fernet
key = Fernet.generate_key()
file = open('key.key', 'wb')  # Open the file as wb to write bytes
file.write(key)  # The key is type bytes still
file.close()
email = input("\n Enter your Email ID: ").encode()
passw = input(" Enter your password: ").encode()
f = Fernet(key)
enc_email = f.encrypt(email)
enc_pass = f.encrypt(passw)

file = open('cred.py', 'wb')

data = "email = '".encode()
file.write(data)
file.write(enc_email)
data = "'".encode()
file.write(data)

data = "\npassword = '".encode()
file.write(data)
file.write(enc_pass)
data = "'".encode()
file.write(data)
print("\nYour cryptography key =",key.decode())
print("Key saved in key.key and credentials saved in cred.py successfully.")