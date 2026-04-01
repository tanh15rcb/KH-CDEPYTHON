n = int(input("Nhập n: "))
i = 2
la_nguyen_to = True

if n < 2:
    la_nguyen_to = False
else:
    while i <= n // 2:
        if n % i == 0:
            la_nguyen_to = False
            break
        i += 1

if la_nguyen_to:
    print("Đây là số nguyên tố")
else:
    print("Không phải số nguyên tố")