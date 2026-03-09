n = int(input("Nhập n: "))

# Hình 1
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

#Hình 2
for i in range(1, n+1):
    for j in range(1, 2*n):
        if i == n and j % 2 != 0:   # dòng đáy
            print("*", end="")
        elif j == n-i+1 or j == n+i-1:   # hai cạnh bên
            print("*", end="")
        else:
            print(" ", end="")
    print()
