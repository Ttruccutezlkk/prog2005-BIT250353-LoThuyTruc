# Yêu cầu 1: In số lẻ từ 17 đến 111 theo thứ tự giảm dần
print("Các số lẻ từ 17 đến 111 (giảm dần):")
for i in range(111, 16, -1):
    if i % 2 != 0:
        print(i, end=" ")

print("\n")

# Yêu cầu 2: In các số nguyên tố từ 17 đến 111
print("Các số nguyên tố từ 17 đến 111:")

for n in range(17, 112):
    if n > 1:
        la_nguyen_to = True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                la_nguyen_to = False
                break
        if la_nguyen_to:
            print(n, end=" ")
