import tkinter as tk
from tkinter import ttk

# --- Hàm xử lý cho Phần b) ---
def show_radio_selection(selected_option):
    """
    Cập nhật Label để hiển thị thông tin Radio Button đang được chọn.
    """
    # Lấy giá trị hiện tại của Radio Button (là 1, 2, hoặc 3)
    selection = selected_option.get()
    
    # Cập nhật văn bản của Label
    result_label.config(text=f"Bạn đã chọn: Số {selection}")

# --- Xây dựng Cửa sổ Chính ---
root = tk.Tk()
root.title("Thông tin cá nhân & Radio Button")
root.geometry("450x450") # Thiết lập kích thước cửa sổ

# --- PHẦN a) Xây dựng Form Thông tin Cá nhân ---
info_frame = ttk.LabelFrame(root, text="Thông tin Cá nhân", padding="10")
info_frame.pack(padx=10, pady=10, fill="x")

# Dữ liệu mẫu (có thể thay thế bằng dữ liệu thực)
personal_info = {
    "Họ Tên": "Nguyễn Văn A",
    "Ngày Sinh": "01/01/2000",
    "MSSV": "B18DCATXXX",
    "Ngành Học": "Công nghệ Thông tin"
}

row_index = 0
for label_text, value in personal_info.items():
    # Label cho tên trường
    ttk.Label(info_frame, text=f"{label_text}:").grid(row=row_index, column=0, sticky="w", padx=5, pady=2)
    
    # Label cho giá trị
    ttk.Label(info_frame, text=value, foreground="blue").grid(row=row_index, column=1, sticky="w", padx=5, pady=2)
    
    row_index += 1

# --- PHẦN b) Xây dựng Form Radio Button ---
radio_frame = ttk.LabelFrame(root, text="Lựa chọn Radio Button", padding="10")
radio_frame.pack(padx=10, pady=10, fill="x")

# Biến Tkinter để lưu trữ lựa chọn Radio Button (IntVar vì giá trị là số 1, 2, 3)
# Khởi tạo giá trị mặc định là 1
radio_var = tk.IntVar(value=1)

# Tạo các Radio Button
ttk.Radiobutton(radio_frame, text="Lựa chọn 1", variable=radio_var, value=1).grid(row=0, column=0, sticky="w", padx=10, pady=5)
ttk.Radiobutton(radio_frame, text="Lựa chọn 2", variable=radio_var, value=2).grid(row=0, column=1, sticky="w", padx=10, pady=5)
ttk.Radiobutton(radio_frame, text="Lựa chọn 3", variable=radio_var, value=3).grid(row=0, column=2, sticky="w", padx=10, pady=5)

# Nút "Click Me"
# Khi nhấn, gọi hàm show_radio_selection với biến radio_var
click_button = ttk.Button(
    radio_frame, 
    text="Click Me", 
    command=lambda: show_radio_selection(radio_var)
)
click_button.grid(row=1, column=0, columnspan=3, pady=10)

# Label hiển thị kết quả lựa chọn
result_label = ttk.Label(radio_frame, text="Chưa có lựa chọn nào được xác nhận", foreground="red")
result_label.grid(row=2, column=0, columnspan=3, pady=5)


# --- Chạy vòng lặp sự kiện chính ---
root.mainloop()
