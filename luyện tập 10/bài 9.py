class Nguoi:
    def __init__(self, ten, tuoi):
        if tuoi < 0:
            raise ValueError("Tuổi không hợp lệ")
        self._ten = ten
        self._tuoi = tuoi

    def get_ten(self):
        return self._ten

    def set_ten(self, ten):
        self._ten = ten

    def __str__(self):
        return f"Tên: {self._ten}, Tuổi: {self._tuoi}"

    def noi(self):
        return "Xin chào!"

    @classmethod
    def loai(cls):
        return "Đây là class Nguoi"

    @staticmethod
    def thong_tin():
        return "Static method"

    def __eq__(self, other):
        return self._ten == other._ten and self._tuoi == other._tuoi


class SinhVien(Nguoi):
    def __init__(self, ten, tuoi, diem):
        super().__init__(ten, tuoi)
        if diem < 0 or diem > 10:
            raise ValueError("Điểm không hợp lệ")
        self._diem = diem

    def __str__(self):
        return f"{super().__str__()}, Điểm: {self._diem}"


# test
sv1 = SinhVien("Trúc", 18, 9)
sv2 = SinhVien("Trúc", 18, 9)

print(sv1)
print(sv1.noi())
print(SinhVien.loai())
print(SinhVien.thong_tin())
print("So sánh:", sv1 == sv2)