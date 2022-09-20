import rsa

def get_passcode():
    with open("./private_key", "rb") as key:
        private_key = rsa.PrivateKey.load_pkcs1(key.read())

    with open("./passcode", "rb") as file:
        ciphertext = file.read()

    passcode = rsa.decrypt(ciphertext, private_key).decode("ascii")
    return passcode

