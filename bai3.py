
def kiem_tra_key(d, key):
    if key in d:
        print("Key tồn tại trong dictionary")
    else:
        print("Key không tồn tại")

# Ví dụ
d = {
    "An": 8,
    "Binh": 7,
    "Chi": 9
}

kiem_tra_key(d, "An")
kiem_tra_key(d, "Dung")