class PlayfairCipher:
    def __init__(self) -> None:
        pass

    def __init__(self):
        pass

    def create_playfair_matrix(self, key):
        key = key.replace("J", "I").upper()
        seen = set()
        matrix = []
        for ch in key:
            if ch not in seen and ch.isalpha():
                seen.add(ch)
                matrix.append(ch)

        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        for ch in alphabet:
            if ch not in seen:
                matrix.append(ch)
                if len(matrix) == 25:
                    break

        return [matrix[i:i+5] for i in range(0, 25, 5)]

    def find_letter_coords(self, matrix, letter):
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == letter:
                    return row, col

    def playfair_encrypt(self, plain_text, matrix):
        plain_text = plain_text.replace("J", "I").upper()
        encrypted_text = ""
        i = 0
        while i < len(plain_text):
            if i + 1 == len(plain_text):  # Odd length
                pair = plain_text[i] + "X"
                i += 1
            elif plain_text[i] == plain_text[i + 1]:  # Same letters
                pair = plain_text[i] + "X"
                i += 1
            else:
                pair = plain_text[i:i + 2]
                i += 2
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])
            if row1 == row2:
                encrypted_text += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                encrypted_text += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
            else:
                encrypted_text += matrix[row1][col2] + matrix[row2][col1]
        return encrypted_text

    def playfair_decrypt(self, cipher_text, matrix):
        cipher_text = cipher_text.upper()
        decrypted_text = ""

        for i in range(0, len(cipher_text), 2):
            pair = cipher_text[i:i + 2]
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])
            if row1 == row2:
                decrypted_text += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:
                decrypted_text += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
            else:
                decrypted_text += matrix[row1][col2] + matrix[row2][col1]

        # Improved logic to remove padding 'X'
        result = ""
        i = 0
        while i < len(decrypted_text):
            if i + 1 < len(decrypted_text) and decrypted_text[i + 1] == "X":
                result += decrypted_text[i]
                i += 2
            else:
                result += decrypted_text[i]
                i += 1

        return result