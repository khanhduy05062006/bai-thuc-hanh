
tong_tien = 0
print("Nhập nhật ký giao dịch (D/W + số tiền). Nhập trống để kết thúc:")
while True:
    dong = input()
    if dong == "":       
        break
    loai, so_tien = dong.split()
    so_tien = int(so_tien)
    if loai.upper() == 'D':
        tong_tien += so_tien
    elif loai.upper() == 'W':
        tong_tien -= so_tien
print("Số tiền còn lại là:", tong_tien)
