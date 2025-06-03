import os
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA1

if not os.path.exists('cipher/rsa/keys'):
    os.makedirs('cipher/rsa/keys')

class RSACipher:
    def __init__(self):
        pass

    def generate_keys(self):
        key = RSA.generate(1024)
        self.private_key = key
        self.public_key = key.publickey()

        with open(r"M:\NguyenPhuQuy-2280602665\lab-03\cipher\rsa\keys\public_key.pem", "wb") as p:
            p.write(self.public_key.exportKey('PEM'))

        with open(r"M:\NguyenPhuQuy-2280602665\lab-03\cipher\rsa\keys\private_key.pem", "wb") as p:
            p.write(self.private_key.exportKey('PEM'))

    def load_keys(self):
        with open('cipher/rsa/keys/public_key.pem', 'rb') as p:
            public_key = RSA.import_key(p.read())
        with open('cipher/rsa/keys/private_key.pem', 'rb') as p:
            private_key = RSA.import_key(p.read())
        return private_key, public_key

    def encrypt(self, message, key):
        cipher = PKCS1_OAEP.new(key)
        return cipher.encrypt(message.encode('ascii')).hex()

    def decrypt(self, ciphertext, key):
        try:
            # ciphertext đã là bytes, không cần fromhex
            cipher = PKCS1_OAEP.new(key)
            decrypted = cipher.decrypt(ciphertext)
            return decrypted.decode('ascii')
        except ValueError as e:
            return f"Invalid format: {str(e)}"
        except Exception as e:
            return f"Decryption failed: {str(e)}"

    def sign(self, message, key):
        h = SHA1.new(message.encode('ascii'))
        signer = PKCS1_v1_5.new(key)
        return signer.sign(h)

    def verify(self, message, signature, key):
        try:
            h = SHA1.new(message.encode('ascii'))
            verifier = PKCS1_v1_5.new(key)
            return verifier.verify(h, signature)
        except:
            return False