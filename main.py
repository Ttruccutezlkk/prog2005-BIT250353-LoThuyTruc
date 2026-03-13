def tinh_toan(t):
    tong = sum(t)
    lon_nhat = max(t)
    nho_nhat = min(t)
    return tong, lon_nhat, nho_nhat

# Ví dụ
t = (3, 7, 1, 9, 5)

tong, lon_nhat, nho_nhat = tinh_toan(t)

print("Tổng:", tong)
print("Giá trị lớn nhất:", lon_nhat)
print("Giá trị nhỏ nhất:", nho_nhat)

