strs = []
while True:
    chuoi = input("Nhập chuỗi: (nhập 'exit' để thoát) ")
    if chuoi == "exit":
        break
    else:
        strs.append(chuoi.upper())

print("Danh sách chuỗi đã nhập: ")
for s in strs:
    print(s)
