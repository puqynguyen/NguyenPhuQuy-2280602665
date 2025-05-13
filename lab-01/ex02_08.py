def chia_het_5(x):
    thanh_phan = int(x, 2)
    if thanh_phan % 5 == 0:
        return True
    else:
        return False
    
chuoi = input("Nhập chuỗi nhị phân (cách nhau bằng ','): ")
chuoi = chuoi.replace(" ", "").split(",")
chuoi = [x for x in chuoi if chia_het_5(x)]
print("Các chuỗi nhị phân chia hết cho 5 là: ", ",".join(chuoi))