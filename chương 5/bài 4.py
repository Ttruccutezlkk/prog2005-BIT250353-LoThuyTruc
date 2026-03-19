import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu (bạn thay tên file cho đúng)
df = pd.read_csv("california_cities.csv")

# Sắp xếp theo diện tích giảm dần
df_sorted = df.sort_values(by="area_total_km2", ascending=False)

# Lấy top 10 thành phố lớn nhất
top10 = df_sorted.head(10)

# Vẽ biểu đồ cột ngang
plt.figure(figsize=(10, 6))
plt.barh(top10["city"], top10["area_total_km2"])

# Đảo ngược trục y để thành phố lớn nhất ở trên
plt.gca().invert_yaxis()

# Thêm tiêu đề và nhãn
plt.title("Top 10 thành phố lớn nhất California theo diện tích")
plt.xlabel("Diện tích (km²)")
plt.ylabel("Thành phố")

# Hiển thị
plt.show()