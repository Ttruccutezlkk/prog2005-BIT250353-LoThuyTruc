import numpy as np
from matplotlib import pyplot as plt

# Chuẩn bị dữ liệu
x = np.linspace(-5, 5, 100)  # Tạo mảng x từ -5 đến 5 với 100 điểm
y1 = x ** 2  # Tính y = x^2
y2 = x ** 3  # Tính y = x^3

# Vẽ biểu đồ
plt.figure(figsize=(8, 6))

# Vẽ hàm y = x^2
plt.plot(x, y1, color='blue', label='y = x²')  # Đường màu xanh
# Vẽ hàm y = x^3
plt.plot(x, y2, color='red', label='y = x³')  # Đường màu đỏ

# Thêm tiêu đề và nhãn cho các trục
plt.title('Biểu đồ của các hàm số y = x² và y = x³')
plt.xlabel('x')
plt.ylabel('y')

# Thêm chú thích
plt.legend()

# Hiển thị biểu đồ
plt.grid()  # Thêm lưới để dễ nhìn hơn
plt.show()