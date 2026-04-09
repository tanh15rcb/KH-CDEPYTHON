1. Giới thiệu

Bài tập xây dựng lớp PhanSo trong Python nhằm mô phỏng các phép toán cơ bản trên phân số.

Chương trình cho phép:

Khởi tạo phân số
Cộng, trừ, nhân, chia hai phân số
Tối giản phân số
Kiểm tra lỗi (mẫu số = 0)
2. Công nghệ sử dụng
Ngôn ngữ: Python 3
Thư viện: math (sử dụng hàm gcd)
3. Cấu trúc thư mục
PhanSoProject/
│
├── phanso.py      # Định nghĩa class PhanSo
└── main.py        # Chương trình chính (test)
4. Mô tả class PhanSo
🔹 Thuộc tính
tu_so: Tử số
mau_so: Mẫu số (mặc định = 1)
🔹 Các hàm chính
cong(): Cộng 2 phân số
tru(): Trừ 2 phân số
nhan(): Nhân 2 phân số
chia(): Chia 2 phân số
toi_gian(): Rút gọn phân số
5. Công thức sử dụng
Cộng / Trừ:
(a/b) ± (c/d) = (ad ± bc) / (b*d)
Nhân:
(a/b) * (c/d) = (ac) / (bd)
Chia:
(a/b) ÷ (c/d) = (ad) / (bc)
6. Cách chạy chương trình
Bước 1: Mở terminal tại thư mục project
Bước 2: Chạy lệnh
python main.py