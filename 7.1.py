def count_lines(filename):
    """
    Đếm số dòng trong tệp văn bản được chỉ định.

    Args:
        filename (str): Tên của tệp văn bản.

    Returns:
        int: Số dòng trong tệp, hoặc -1 nếu có lỗi xảy ra.
    """
    try:
        # Mở tệp ở chế độ đọc ('r')
        with open(filename, 'r', encoding='utf-8') as file:
            line_count = 0
            # Lặp qua từng dòng trong tệp và tăng bộ đếm
            for line in file:
                line_count += 1
        
        return line_count
    
    except FileNotFoundError:
        # Xử lý trường hợp tệp không tồn tại
        print(f"Lỗi: Tệp '{filename}' không được tìm thấy.")
        return -1
    except Exception as e:
        # Xử lý các lỗi khác
        print(f"Đã xảy ra lỗi: {e}")
        return -1

# --- Ví dụ sử dụng ---
file_to_count = 'sample_text_file.txt' # Đổi thành tên tệp của bạn

# Ghi một tệp mẫu để thử nghiệm (nếu tệp chưa tồn tại)
try:
    with open(file_to_count, 'w', encoding='utf-8') as f:
        f.write("Đây là dòng 1.\n")
        f.write("Dòng thứ hai.\n")
        f.write("Và đây là dòng cuối cùng, dòng 3.\n")
except Exception as e:
    print(f"Không thể tạo tệp mẫu: {e}")

# Thực hiện đếm
num_lines = count_lines(file_to_count)

if num_lines != -1:
    print(f"Tệp '{file_to_count}' có {num_lines} dòng.")
