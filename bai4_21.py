def is_divisible_by_5(binary_str):
    decimal = int(binary_str, 2)
    return decimal % 5 == 0
input_str = input("Nhập chuỗi các số nhị phân 4 chữ số, cách nhau bằng dấu phẩy: ")
binary_numbers = input_str.split(',')
divisible_by_5 = [num for num in binary_numbers if is_divisible_by_5(num)]
print("Các số nhị phân chia hết cho 5 là:")
print(','.join(divisible_by_5))
