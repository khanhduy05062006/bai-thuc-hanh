import numpy as np

# --- 1. Tạo Mảng ban đầu (từ 12 đến 38) ---

start_value = 12
end_value = 38

# np.arange(start, stop) tạo ra các giá trị từ 'start' đến 'stop - 1'.
# Ta cần 39 để bao gồm giá trị 38.
original_array = np.arange(start_value, end_value + 1)

print("📝 Mảng Ban đầu (12 đến 38):")
print(original_array)

# --- 2. Đảo ngược Mảng ---

# Có nhiều cách để đảo ngược mảng trong NumPy, nhưng cách dùng 
# slicing (lát cắt) là ngắn gọn và phổ biến nhất: [::-1]
reversed_array = original_array[::-1]

print("\n🔁 Mảng Đã đảo ngược:")
print(reversed_array)

# --- Kiểm tra ---
print("\n🔍 Kiểm tra:")
print(f"Phần tử đầu tiên của mảng gốc: {original_array[0]}")
print(f"Phần tử cuối cùng của mảng đảo ngược: {reversed_array[-1]}")
print("-" * 40)
print(f"Phần tử cuối cùng của mảng gốc: {original_array[-1]}")
print(f"Phần tử đầu tiên của mảng đảo ngược: {reversed_array[0]}")
