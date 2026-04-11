from models.manager import Manager
from models.developer import Developer
from models.intern import Intern
from services.company import Company
from services.payroll import increase_salary

company = Company()

def menu():
    print("\n===== MENU =====")
    print("1. Thêm nhân viên")
    print("2. Hiển thị danh sách")
    print("3. Tìm theo ID")
    print("4. Tính tổng lương")
    print("5. Lương cao nhất")
    print("6. Đánh giá hiệu suất")
    print("0. Thoát")

while True:
    menu()
    choice = input("Chọn: ")

    if choice == "1":
        t = input("Loại (m/d/i): ")
        id = input("ID: ")
        name = input("Tên: ")
        salary = float(input("Lương: "))

        if t == "m":
            emp = Manager(id, name, salary)
        elif t == "d":
            lang = input("Ngôn ngữ: ")
            emp = Developer(id, name, salary, lang)
        else:
            emp = Intern(id, name, salary)

        company.add(emp)

    elif choice == "2":
        company.show_all()

    elif choice == "3":
        id = input("Nhập ID: ")
        emp = company.find_by_id(id)
        print(emp.show() if emp else "Không tìm thấy")

    elif choice == "4":
        print("Tổng lương:", company.total_salary())

    elif choice == "5":
        print("Cao nhất:", company.max_salary().show())

    elif choice == "6":
        id = input("ID: ")
        emp = company.find_by_id(id)
        if emp:
            emp.performance = float(input("Điểm: "))
        print("Xuất sắc:")
        for e in company.excellent():
            print(e.show())

    elif choice == "0":
        break