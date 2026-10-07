## This is where the instructions for using the encyrption library
## pip install cryptography


from cryptography.fernet import Fernet
key = Fernet.generate_key()
print(key) ## This is the key that should be passed for each assignment
## this document is just to be used for testing
f = Fernet(key)
token = f.encrypt(b"A really secret message. Not for prying eyes.")
##print(token) ## this will show the encrypted message
##print(f.decrypt(token))