def tong_chan(lst):
    tong = 0
    for i in lst:
        if i % 2 == 0:
            tong += i
    return tong

lst = input("Nhập vào danh sách các số nguyên cách nhau bởi dấu cách: ")
lst = list(map(int, lst.split()))
print("Tổng các số chẵn trong danh sách là:", tong_chan(lst))