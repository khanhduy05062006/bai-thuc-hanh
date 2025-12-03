# main_program.py

# Import module đã tạo
from list_utils import find_max, find_min, bubble_sort

def get_list_input():
    """
    Nhận số lượng và các giá trị của danh sách từ bàn phím.
    """
    while True:
        try:
            # Nhận số lượng phần tử
            n = int(input("Nhập số lượng phần tử (N) của danh sách: "))
            if n <= 0:
                print("Số lượng phần tử phải là số nguyên dương.")
                continue
            break
        except ValueError:
            print("Đầu vào không hợp lệ. Vui lòng nhập một số nguyên.")
            
    my_list = []
    print(f"Vui lòng nhập {n} giá trị số nguyên:")
    
    for i in range(n):
        while True:
            try:
                # Nhận giá trị từng phần tử
                value = int(input(f"Nhập phần tử thứ {i + 1}: "))
                my_list.append(value)
                break
            except ValueError:
                print("Đầu vào không hợp lệ. Vui lòng nhập một số nguyên.")
                
    return my_list

# --- Thực hiện chương trình ---

if __name__ == "__main__":
    
    print("--- Chương trình tìm Max/Min và Sắp xếp Danh sách ---")
    
    # 1. Nhận danh sách từ người dùng
    input_list = get_list_input()
    
    if not input_list:
        print("Danh sách rỗng. Không thể xử lý.")
    else:
        print(f"\nDanh sách đã nhập: {input_list}")
        
        # 2. Sử dụng hàm từ module để tìm phần tử lớn nhất
        max_val = find_max(input_list)
        print(f"Phần tử lớn nhất (từ module find_max): {max_val}")
        
        # 3. Sử dụng hàm từ module để tìm phần tử nhỏ nhất
        min_val = find_min(input_list)
        print(f"Phần tử nhỏ nhất (từ module find_min): {min_val}")
        
        # 4. Sử dụng hàm từ module để sắp xếp
        sorted_list = bubble_sort(input_list.copy()) # Dùng .copy() để không thay đổi danh sách gốc
        print(f"Danh sách đã sắp xếp (từ module bubble_sort): {sorted_list}")
