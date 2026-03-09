a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

print("Ba hệ số bạn vừa nhập là:")
print("a =", a)
print("b =", b)
print("c =", c)

# Tìm số lớn nhất và nhỏ nhất
max_num = max(a, b, c)
min_num = min(a, b, c)

# In kết quả
print("Số lớn nhất là:", max_num)
print("Số nhỏ nhất là:", min_num)