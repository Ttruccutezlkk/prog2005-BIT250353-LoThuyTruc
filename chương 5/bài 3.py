import matplotlib.pyplot as plt

labels = ['A', 'B', 'C', 'D', 'E']
sizes = [30, 25, 15, 20, 10]  # Phần trăm doanh số

plt.figure(figsize=(8, 6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)

plt.title('Phần trăm doanh số của các sản phẩm')

plt.axis('equal')  # Đảm bảo hình tròn
plt.show()