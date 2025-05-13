def dem_so_lan_xuat_hien(s):
    dem = {}
    str = s.split()
    for word in str:
        if word in dem:
            dem[word] += 1
        else:
            dem[word] = 1 
    return dem

str = input("Nhập chuỗi: ")
result = dem_so_lan_xuat_hien(str)
print(result)