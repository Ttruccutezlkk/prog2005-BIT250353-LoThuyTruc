# Khởi tạo biến để lưu trữ mật khẩu
mat_khau = ""

# Sử dụng vòng lặp while để yêu cầu người dùng nhập mật khẩu
while mat_khau != "python123":
    mat_khau = input("Nhập mật khẩu: ")
    if mat_khau != "python123":
        print("Mật khẩu không đúng. Vui lòng thử lại.")

# Thông báo khi mật khẩu đúng
print("Mật khẩu đúng! Chào mừng bạn.")