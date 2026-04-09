from phanso import PhanSo

def main():
    print("=== CHƯƠNG TRÌNH PHÂN SỐ ===")

    # Nhập phân số 1
    tu1 = int(input("Nhập tử số 1: "))
    mau1 = int(input("Nhập mẫu số 1: "))
    ps1 = PhanSo(tu1, mau1)

    # Nhập phân số 2
    tu2 = int(input("Nhập tử số 2: "))
    mau2 = int(input("Nhập mẫu số 2: "))
    ps2 = PhanSo(tu2, mau2)

    print("\n--- KẾT QUẢ ---")
    print("Phân số 1:", ps1)
    print("Phân số 2:", ps2)

    print("Tổng:", ps1.cong(ps2))
    print("Hiệu:", ps1.tru(ps2))
    print("Nhân:", ps1.nhan(ps2))
    print("Chia:", ps1.chia(ps2))


if __name__ == "__main__":
    main()