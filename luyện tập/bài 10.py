class SinhVien:
    count = 0  # Biến lớp để đếm số sinh viên

    def __init__(self, name, score):
        self.name = name  # Tên sinh viên
        self.score = score  # Điểm của sinh viên
        SinhVien.count += 1  # Tăng biến đếm khi một đối tượng được tạo ra

    @classmethod
    def get_count(cls):
        """Phương thức lớp để lấy số lượng sinh viên."""
        return cls.count

    def __str__(self):
        """Trả về chuỗi mô tả sinh viên."""
        return f"Sinh viên: {self.name}, Điểm: {self.score}"

# Ví dụ sử dụng
sinh_vien_1 = SinhVien("Nam", 8.5)
sinh_vien_2 = SinhVien("Lan", 9.0)
sinh_vien_3 = SinhVien("Hao", 7.5)

# In ra số lượng sinh viên đã được tạo ra
print("Số lượng sinh viên được tạo ra:", SinhVien.get_count())