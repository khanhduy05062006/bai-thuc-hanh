def read_full_file(filename):
    """
    Đọc và in toàn bộ nội dung của tệp văn bản.

    Args:
        filename (str): Tên của tệp văn bản cần đọc.
    """
    try:
        # Mở tệp ở chế độ đọc ('r')
        with open(filename, 'r', encoding='utf-8') as file:
            # Sử dụng phương thức read() để đọc toàn bộ nội dung
            full_content = file.read()
            
            print(f"--- Nội dung của tệp '{filename}' ---")
            print(full_content)
            print("-----------------------------------")
            
    except FileNotFoundError:
        print(f"❌ Lỗi: Tệp '{filename}' không được tìm thấy.")
    except Exception as e:
        print(f"❌ Đã xảy ra lỗi khi đọc tệp: {e}")

# --- Ví dụ sử dụng ---
file_name = 'sample_file_to_read.txt' 

# 1. Tạo một tệp mẫu để thử nghiệm (nếu tệp chưa tồn tại)
try:
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write("Đây là dòng đầu tiên.\n")
        f.write("Dòng thứ hai chứa một vài ký tự đặc biệt.\n")
        f.write("Đây là dòng cuối cùng, được đọc toàn bộ.")
except Exception as e:
    print(f"Không thể tạo tệp mẫu: {e}")

# 2. Thực hiện đọc toàn bộ tệp
read_full_file(file_name)
