for x in range(2000, 3600):
    if x % 7 == 0 and x % 5 != 0:
        print(str(x) + ",", end="")