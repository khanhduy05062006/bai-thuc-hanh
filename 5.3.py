import numpy as np

# Giới hạn dưới (bao gồm)
start_value = 12

# Giới hạn trên (bao gồm)
end_value = 38

# Hàm np.arange(start, stop) tạo ra các giá trị từ 'start' 
# đến 'stop - 1'. Do đó, ta phải đặt 'stop' là 38 + 1 = 39 
# để đảm bảo giá trị 38 được bao gồm.
my_array = np.arange(start_value, end_value + 1)

# In mảng đã tạo
print(f"Khoảng giá trị yêu cầu: Từ {start_value} đến {end_value} (bao gồm)")
print("-" * 40)
print("Mảng NumPy đã tạo:")
print(my_array)
print("-" * 40)
print(f"Kích thước mảng: {my_array.shape}")
print(f"Loại dữ liệu: {my_array.dtype}")
