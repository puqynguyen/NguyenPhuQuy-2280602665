def xoa_phan_tu(dic, key):
    """
    Xóa phần tử trong dictionary theo key
    :param dic: dictionary
    :param key: key cần xóa
    :return: None
    """
    if key in dic:
        del dic[key]
    else:
        print(f"Key '{key}' không tồn tại trong dictionary.")
        
dic = {'a': 1, 'b': 2, 'c': 3}
xoa_phan_tu(dic, 'b')
print(dic)  # {'a': 1, 'c': 3}