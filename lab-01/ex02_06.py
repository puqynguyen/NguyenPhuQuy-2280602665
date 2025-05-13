x = int(input("Enter the number of rows: "))
y = int(input("Enter the number of columns: "))
row = [int(i) for i in range(x)]
col = [int(i) for i in range(y)]
table = [[0 for _ in range(y)] for _ in range(x)]
for i in range(x):
    for j in range(y):
        table[i][j] = i * j
        
print("Multiplication table:", table)