chuoi = input("Nhập một chuỗi: ")

chuoi_dao_nguoc = ""

for i in range(len(chuoi) - 1, -1, -1):
    chuoi_dao_nguoc += chuoi[i]  # Thêm ký tự vào chuỗi đảo ngược

print("Chuỗi đảo ngược là:", chuoi_dao_nguoc)