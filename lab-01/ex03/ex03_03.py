def tao_tuple(lst):
    return tuple(lst)

lst = input("Nhập vào danh sách các số nguyên cách nhau bởi dấu cách: ")
number = list(map(int, lst.split()))
tuple = tao_tuple(number)
print("Danh sách là:", number)
print("Tuple là:", tuple)