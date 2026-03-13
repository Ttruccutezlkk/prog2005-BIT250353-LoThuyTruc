def diem_trung_binh(ds):
    tong = sum(ds.values())
    so_sv = len(ds)
    return tong / so_sv

# Ví dụ
sinh_vien = {
    "An": 8,
    "Binh": 7,
    "Chi": 9
}

tb = diem_trung_binh(sinh_vien)

print("Điểm trung bình:", tb)