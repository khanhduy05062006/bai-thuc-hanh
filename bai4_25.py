
s = input("Nhập danh sách số, cách nhau bởi dấu phẩy: ")
numbers = [int(x) for x in s.split(",")]
odd_numbers = [x for x in numbers if x % 2 != 0]
print("Các số lẻ là:", odd_numbers)
