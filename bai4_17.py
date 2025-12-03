chuoi = input("Nhập chuỗi các số, cách nhau bằng dấu phẩy: ")
ds_chuoi = chuoi.split(',')
ds_duong = [int(x.strip()) for x in ds_chuoi if int(x.strip()) > 0]
print("Danh sách các số nguyên dương là:")
print(ds_duong)
