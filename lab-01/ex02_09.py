def so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

x = int(input("Nhập số nguyên dương: "))
if so_nguyen_to(x):
    print(f"{x} là số nguyên tố")
else:
    print(f"{x} không phải là số nguyên tố")