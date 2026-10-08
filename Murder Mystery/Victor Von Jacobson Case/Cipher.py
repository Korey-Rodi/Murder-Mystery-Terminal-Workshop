## File for decrypting messages
## pip install cryptography (you must have this installed for this project )


from cryptography.fernet import Fernet
##uncomment the below code once you have located the key 
# and assigned it to the key variable
'''
key =
f = Fernet(key)
'''

#Fernet is a symmetric (secret-key) authenticated cryptography specification and implementation
# that makes sure a message cannot be read or changed without the right key
print(f.decrypt("what you are trying to decrypt"))