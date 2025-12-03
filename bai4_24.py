sentence = input("Nhập một câu: ")
uppercase_count = 0
lowercase_count = 0
for char in sentence:
    if char.isupper():  
        uppercase_count += 1
    elif char.islower():  
        lowercase_count += 1
print("Số chữ cái viết hoa:", uppercase_count)
print("Số chữ cái viết thường:", lowercase_count)
