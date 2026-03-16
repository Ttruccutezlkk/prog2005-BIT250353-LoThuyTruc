class SinhVien:
    def __init__(self, name, score):
        self.name = name  # Tên sinh viên
        self.score = score  # Điểm của sinh viên

    def __eq__(self, other):
        """Nạp chồng toán tử == để so sánh điểm của hai sinh viên."""
        if isinstance(other, SinhVien):
            return self.score == other.score
        return NotImplemented  # Trả về NotImplemented nếu không so sánh được

    def __str__(self):
        """Trả về chuỗi mô tả sinh viên."""
        return f"Sinh viên: {self.name}, Điểm: {self.score}"

# Ví dụ sử dụng
sinh_vien_1 = SinhVien("Nam", 8.5)
sinh_vien_2 = SinhVien("Lan", 8.5)
sinh_vien_3 = SinhVien("Hao", 9.0)

# So sánh các sinh viên
print(sinh_vien_1 == sinh_vien_2)  # Kết quả sẽ là True
print(sinh_vien_1 == sinh_vien_3)  # Kết quả sẽ là False

# In ra thông tin về sinh viên
print(sinh_vien_1)  # In thông tin sinh viên 1
print(sinh_vien_2)  # In thông tin sinh viên 2
print(sinh_vien_3)  # In thông tin sinh viên 3