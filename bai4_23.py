sentence = input("Nhập một câu: ")
letters_count = 0
digits_count = 0
for char in sentence:
    if char.isalpha(): 
        letters_count += 1
    elif char.isdigit():  
        digits_count += 1
print("Số ký tự chữ cái:", letters_count)
print("Số ký tự số:", digits_count)
