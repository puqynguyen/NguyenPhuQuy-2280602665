def dao_nguoc(x):
    if x < 0:
        raise ValueError("x phải là số nguyên dương")
    
    # Chuyển đổi số thành chuỗi, đảo ngược và chuyển lại thành số nguyên
    return int(str(x)[::-1])

x = int(input("Nhập số nguyên dương: "))
print(f"Số đảo ngược của {x} là {dao_nguoc(x)}")