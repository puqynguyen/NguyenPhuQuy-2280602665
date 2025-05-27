def create_playfair_matrix(key):
        key = key.replace("J", "I").upper()
        seen = set()
        matrix = []
        # Chỉ thêm ký tự mới vào ma trận
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

        # Chia thành 5×5
        return [matrix[i:i+5] for i in range(0,25,5)]
    
def main():
    key = "abc"
    print(create_playfair_matrix(key))
    
if __name__ == "__main__":
    main()