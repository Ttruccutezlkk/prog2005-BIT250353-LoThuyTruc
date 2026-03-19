import os

def trich_xuat_ten_tap_nhac(duong_dan):
    """Trích xuất tên tệp nhạc, bao gồm đuôi tệp."""
    return os.path.basename(duong_dan)

def trich_xuat_ten_bai_hat(duong_dan):
    """Trích xuất tên bài hát mà không có đuôi tệp."""
    ten_tap = os.path.basename(duong_dan)  # Lấy tên tệp
    return os.path.splitext(ten_tap)[0]    # Tách tên và đuôi tệp

# Ví dụ sử dụng
duong_dan = "d:\\music\\muabui.mp3"
ten_tap_nhac = trich_xuat_ten_tap_nhac(duong_dan)
ten_bai_hat = trich_xuat_ten_bai_hat(duong_dan)

print("Tên tệp nhạc:", ten_tap_nhac)    # Kết quả: muabui.mp3
print("Tên bài hát:", ten_bai_hat)        # Kết quả: muabui