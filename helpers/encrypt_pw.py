import rsa

public_key, private_key = rsa.newkeys(512)

string = input("String to be encrypted: ")

encrypted_string = rsa.encrypt(string.encode(), public_key)

with open("private_key", "wb") as file:
    file.write(private_key.save_pkcs1("PEM"))

with open("passcode", "wb") as file:
    file.write(encrypted_string)

