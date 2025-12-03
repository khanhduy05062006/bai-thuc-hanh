
def pascal_row(n):
    row = [1]
    for k in range(1, n):
        next_number = row[k-1] * (n - k) // k
        row.append(next_number)
    return row
n = int(input("Nhập n (dòng thứ n của tam giác Pascal): "))
result = pascal_row(n)
print("Dòng thứ", n, "của tam giác Pascal là:")
print(result)
