import sqlite3

# Kết nối database
def ket_noi():
    return sqlite3.connect("nhansu.db")

# Tạo bảng
def tao_bang():
    conn = ket_noi()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS nhan_su (
        cccd TEXT PRIMARY KEY,
        ho_ten TEXT NOT NULL,
        ngay_sinh TEXT,
        gioi_tinh TEXT,
        dia_chi TEXT
    )
    """)

    conn.commit()
    conn.close()


# ================== CRUD ==================

# 1. Thêm nhân sự
def them_nhan_su(cccd, ho_ten, ngay_sinh, gioi_tinh, dia_chi):
    try:
        conn = ket_noi()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO nhan_su VALUES (?, ?, ?, ?, ?)
        """, (cccd, ho_ten, ngay_sinh, gioi_tinh, dia_chi))

        conn.commit()
        print("Thêm thành công!")

    except sqlite3.IntegrityError:
        print("Lỗi: CCCD đã tồn tại!")

    finally:
        conn.close()


# 2. Hiển thị danh sách
def hien_thi():
    conn = ket_noi()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM nhan_su")
    data = cursor.fetchall()

    for row in data:
        print(row)

    conn.close()


# 3. Sửa nhân sự
def sua_nhan_su(cccd, ho_ten, ngay_sinh, gioi_tinh, dia_chi):
    conn = ket_noi()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE nhan_su
    SET ho_ten=?, ngay_sinh=?, gioi_tinh=?, dia_chi=?
    WHERE cccd=?
    """, (ho_ten, ngay_sinh, gioi_tinh, dia_chi, cccd))

    conn.commit()

    if cursor.rowcount > 0:
        print("Cập nhật thành công!")
    else:
        print("Không tìm thấy CCCD!")

    conn.close()


# 4. Xóa nhân sự
def xoa_nhan_su(cccd):
    conn = ket_noi()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM nhan_su WHERE cccd=?", (cccd,))
    conn.commit()

    if cursor.rowcount > 0:
        print("Xóa thành công!")
    else:
        print("Không tìm thấy CCCD!")

    conn.close()


# 5. Tìm kiếm
def tim_kiem(tu_khoa):
    conn = ket_noi()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM nhan_su
    WHERE cccd LIKE ? OR ho_ten LIKE ? OR dia_chi LIKE ?
    """, (f"%{tu_khoa}%", f"%{tu_khoa}%", f"%{tu_khoa}%"))

    data = cursor.fetchall()

    if data:
        for row in data:
            print(row)
    else:
        print("Không tìm thấy!")

    conn.close()


# ================== TEST ==================
if __name__ == "__main__":
    tao_bang()

    while True:
        print("\n===== MENU =====")
        print("1. Thêm nhân sự")
        print("2. Hiển thị")
        print("3. Sửa")
        print("4. Xóa")
        print("5. Tìm kiếm")
        print("0. Thoát")

        chon = input("Chọn: ")

        if chon == "1":
            cccd = input("CCCD: ")
            ho_ten = input("Họ tên: ")
            ngay_sinh = input("Ngày sinh: ")
            gioi_tinh = input("Giới tính: ")
            dia_chi = input("Địa chỉ: ")
            them_nhan_su(cccd, ho_ten, ngay_sinh, gioi_tinh, dia_chi)

        elif chon == "2":
            hien_thi()

        elif chon == "3":
            cccd = input("Nhập CCCD cần sửa: ")
            ho_ten = input("Họ tên mới: ")
            ngay_sinh = input("Ngày sinh: ")
            gioi_tinh = input("Giới tính: ")
            dia_chi = input("Địa chỉ: ")
            sua_nhan_su(cccd, ho_ten, ngay_sinh, gioi_tinh, dia_chi)

        elif chon == "4":
            cccd = input("Nhập CCCD cần xóa: ")
            xoa_nhan_su(cccd)

        elif chon == "5":
            tu_khoa = input("Nhập từ khóa: ")
            tim_kiem(tu_khoa)

        elif chon == "0":
            break

        else:
            print("Chọn sai!")