class TranspositionCipher:
    def __init__(self):
        pass

    def encrypt(self, text, key):
        encrypted_text = ''
        for col in range(key):
            pointer = col
            while pointer < len(text):
                encrypted_text += text[pointer]
                pointer += key
        return encrypted_text

    def decrypt(self, text, key):
        # Tính số hàng cần thiết
        n = len(text)
        num_rows = (n + key - 1) // key
        cols = [num_rows] * key
        remaining = (num_rows * key) - n
        for i in range(remaining):
            cols[key - 1 - i] -= 1
        decrypted_text = [''] * num_rows
        pos = 0
        for col in range(key):
            for row in range(cols[col]):
                decrypted_text[row] += text[pos]
                pos += 1
        return ''.join(decrypted_text)