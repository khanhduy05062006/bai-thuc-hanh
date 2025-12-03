import math

class Circle:
    """
    Class đại diện cho một hình tròn, được định nghĩa bởi bán kính (radius).
    Cung cấp các phương thức để tính diện tích và chu vi.
    """
    
    def __init__(self, radius):
        """
        Phương thức khởi tạo (constructor).
        Kiểm tra và thiết lập bán kính.
        
        Args:
            radius (float/int): Bán kính của hình tròn.
        """
        # Đảm bảo bán kính là số dương
        if radius <= 0:
            raise ValueError("Bán kính phải là một số dương.")
        self.radius = radius
        print(f"✅ Đã tạo hình tròn với bán kính R = {self.radius}")

    def tinh_dien_tich(self):
        """
        Tính diện tích của hình tròn theo công thức: A = π * R^2
        
        Returns:
            float: Diện tích của hình tròn.
        """
        dien_tich = math.pi * (self.radius ** 2)
        return dien_tich

    def tinh_chu_vi(self):
        """
        Tính chu vi của hình tròn theo công thức: C = 2 * π * R
        
        Returns:
            float: Chu vi của hình tròn.
        """
        chu_vi = 2 * math.pi * self.radius
        return chu_vi

# --- Ví dụ sử dụng Class Circle ---

# 1. Tạo một đối tượng Circle
try:
    # Khởi tạo hình tròn với bán kính R = 5
    hinh_tron_a = Circle(5)
    
    # 2. Tính toán và hiển thị kết quả
    dien_tich_a = hinh_tron_a.tinh_dien_tich()
    chu_vi_a = hinh_tron_a.tinh_chu_vi()
    
    print("\n--- Kết quả tính toán ---")
    print(f"Bán kính (R): {hinh_tron_a.radius}")
    print(f"Diện tích (A): {dien_tich_a:.4f} (π * R²) {math.pi:.4f} * 5²")
    print(f"Chu vi (C): {chu_vi_a:.4f} (2 * π * R) 2 * {math.pi:.4f} * 5")
    print("------------------------")

    # 3. Thử nghiệm với bán kính khác
    hinh_tron_b = Circle(12.5)
    print(f"Diện tích mới: {hinh_tron_b.tinh_dien_tich():.2f}")
    
except ValueError as e:
    print(f"Lỗi khởi tạo: {e}")
