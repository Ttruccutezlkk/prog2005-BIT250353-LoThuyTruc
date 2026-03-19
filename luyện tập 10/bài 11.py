while True:
    print("\n--- MENU ---")
    print("1. Bài 1")
    print("2. Bài 2")
    print("3. Thoát")

    chon = input("Chọn: ")

    if chon == "1":
        path = input("Nhập đường dẫn: ")
        print(path.split("\\")[-1])

    elif chon == "2":
        s = input("Nhập chuỗi: ")
        k = input("Nhập ký tự: ")
        print(s.count(k))

    elif chon == "3":
        print("Thoát!")
        break

    else:
        print("Chọn sai!")