import ecdsa, os

if not os.path.exists('cipher/ecc/keys'):
    os.makedirs('cipher/ecc/keys')

class ECCCipher:
    def __init__(self):
        pass
    
    def generate_keys(self):
        sk = ecdsa.SigningKey.generate()
        vk = sk.get_verifying_key()
        
        with open('cipher/ecc/keys/private_key.pem', 'wb') as f:
            f.write(sk.to_pem())
        with open('cipher/ecc/keys/public_key.pem', 'wb') as f:
            f.write(vk.to_pem())
    
    def load_keys(self):
        with open('cipher/ecc/keys/private_key.pem', 'rb') as f:
            private_key = ecdsa.SigningKey.from_pem(f.read())
        with open('cipher/ecc/keys/public_key.pem', 'rb') as f:
            public_key = ecdsa.VerifyingKey.from_pem(f.read())
        return private_key, public_key

    def sign(self, message, private_key):
        return private_key.sign(message.encode('ascii'))
    
    def verify(self, message, signature, public_key):
        try:
            return public_key.verify(signature, message.encode('ascii'))
        except ecdsa.BadSignatureError:
            return False
        except Exception as e:
            return f"Verification failed: {str(e)}"