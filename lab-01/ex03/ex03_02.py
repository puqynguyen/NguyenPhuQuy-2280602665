def dao_nguoc_list(lst):
    return lst[::-1]
lst = input("Nhập vào danh sách các số nguyên cách nhau bởi dấu cách: ")
lst = list(map(str, lst.split()))
print("Danh sách sau khi đảo ngược là:", ", ".join(dao_nguoc_list(lst)))