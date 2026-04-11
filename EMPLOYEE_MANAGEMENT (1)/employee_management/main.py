import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from models.manager import Manager
from models.developer import Developer
from models.intern import Intern
from services.company import Company
from services.payroll import Payroll
from utils.validators import Validators
from utils.formatters import Formatters
from exceptions.employee_exceptions import (
    EmployeeNotFoundError,
    InvalidSalaryError,
    InvalidAgeError,
    ProjectAllocationError,
    DuplicateEmployeeError
)

def main():
    company = Company()
    
    while True:
        try:
            print(Formatters.format_menu())
            choice = input().strip()
            Validators.validate_choice(choice, [str(i) for i in range(1, 12)])
            
            if choice == '1':
                add_employee(company)
            elif choice == '2':
                remove_employee(company)
            elif choice == '3':
                find_employee(company)
            elif choice == '4':
                list_employees(company)
            elif choice == '5':
                assign_project(company)
            elif choice == '6':
                evaluate_performance(company)
            elif choice == '7':
                salary_report(company)
            elif choice == '8':
                statistics(company)
            elif choice == '9':
                project_management(company)
            elif choice == '10':
                hr_management(company)
            elif choice == '11':
                print("Cảm ơn đã sử dụng hệ thống!")
                break
                
        except ValueError as e:
            print(f"Lỗi: {e}. Vui lòng thử lại.")
        except Exception as e:
            print(f"Lỗi không mong muốn: {e}. Vui lòng thử lại.")

def add_employee(company):
    try:
        print("Chọn loại nhân viên:")
        print("1. Manager")
        print("2. Developer")
        print("3. Intern")
        emp_type = input("Nhập lựa chọn (1-3): ").strip()
        Validators.validate_choice(emp_type, ['1', '2', '3'])
        
        name = input("Nhập tên: ").strip()
        if not name:
            raise ValueError("Tên không được để trống")
        
        age_str = input("Nhập tuổi: ").strip()
        age = Validators.validate_age(age_str)
        
        email = input("Nhập email: ").strip()
        email = Validators.validate_email(email)
        
        salary_str = input("Nhập lương cơ bản: ").strip()
        salary = Validators.validate_salary(salary_str)
        
        if emp_type == '1':
            emp = Manager(name, age, email, salary)
        elif emp_type == '2':
            emp = Developer(name, age, email, salary)
        elif emp_type == '3':
            emp = Intern(name, age, email, salary)
        
        company.add_employee(emp)
        print(f"Đã thêm nhân viên: {emp.employee_id} - {emp.name}")
        
    except (InvalidAgeError, InvalidSalaryError, ValueError, DuplicateEmployeeError) as e:
        print(f"Lỗi: {e}")
    except Exception as e:
        print(f"Lỗi không mong muốn: {e}")

def remove_employee(company):
    try:
        emp_id = input("Nhập ID nhân viên cần xóa: ").strip().upper()
        company.remove_employee(emp_id)
        print(f"Đã xóa nhân viên có ID: {emp_id}")
    except EmployeeNotFoundError as e:
        print(f"Lỗi: {e}")
    except Exception as e:
        print(f"Lỗi không mong muốn: {e}")

def find_employee(company):
    try:
        emp_id = input("Nhập ID nhân viên: ").strip().upper()
        emp = company.find_employee(emp_id)
        print(Formatters.format_employee_list([emp]))
    except EmployeeNotFoundError as e:
        print(f"Lỗi: {e}")
    except Exception as e:
        print(f"Lỗi không mong muốn: {e}")

def list_employees(company):
    try:
        employees = company.list_employees()
        print(Formatters.format_employee_list(employees))
    except IndexError as e:
        print(f"Lỗi: {e}")
    except Exception as e:
        print(f"Lỗi không mong muốn: {e}")

def assign_project(company):
    try:
        emp_id = input("Nhập ID nhân viên: ").strip().upper()
        emp = company.find_employee(emp_id)
        project = input("Nhập tên dự án: ").strip()
        if not project:
            raise ValueError("Tên dự án không được để trống")
        emp.assign_project(project)
        print(f"Đã phân công dự án '{project}' cho nhân viên {emp.name}")
    except (EmployeeNotFoundError, ProjectAllocationError, ValueError) as e:
        print(f"Lỗi: {e}")
    except Exception as e:
        print(f"Lỗi không mong muốn: {e}")

def evaluate_performance(company):
    try:
        emp_id = input("Nhập ID nhân viên: ").strip().upper()
        emp = company.find_employee(emp_id)
        score_str = input("Nhập điểm đánh giá (0-10): ").strip()
        score = Validators.validate_score(score_str)
        emp.evaluate_performance(score)
        print(f"Đã đánh giá nhân viên {emp.name} với điểm {score}")
    except (EmployeeNotFoundError, ValueError) as e:
        print(f"Lỗi: {e}")
    except Exception as e:
        print(f"Lỗi không mong muốn: {e}")

def salary_report(company):
    try:
        report = Payroll.get_salary_report(company)
        print(Formatters.format_salary_report(report))
    except IndexError as e:
        print(f"Lỗi: {e}")
    except Exception as e:
        print(f"Lỗi không mong muốn: {e}")

def statistics(company):
    try:
        employees = company.list_employees()
        total_salary = Payroll.calculate_total_salary(company)
        avg_salary = Payroll.calculate_average_salary(company)
        top_performers = Payroll.get_top_performers(company, 3)
        
        print("THỐNG KÊ HỆ THỐNG")
        print(f"Tổng số nhân viên: {len(employees)}")
        print(f"Tổng lương: {total_salary:,.0f} VND")
        print(f"Lương trung bình: {avg_salary:,.0f} VND")
        print("\nTop 3 nhân viên có hiệu suất cao nhất:")
        for emp in top_performers:
            print(f"- {emp.name} ({emp.employee_id}): {emp.performance_score} điểm")
            
        # Thống kê theo chức vụ
        managers = company.get_employee_by_position("Manager")
        developers = company.get_employee_by_position("Developer")
        interns = company.get_employee_by_position("Intern")
        
        print(f"\nSố Manager: {len(managers)}")
        print(f"Số Developer: {len(developers)}")
        print(f"Số Intern: {len(interns)}")
        
    except IndexError as e:
        print(f"Lỗi: {e}")
    except Exception as e:
        print(f"Lỗi không mong muốn: {e}")
def project_management(company):
    while True:
        print("\nQUẢN LÝ DỰ ÁN")
        print("1. Thêm dự án mới")
        print("2. Hiển thị danh sách dự án")
        print("3. Phân công nhân viên vào dự án")
        print("4. Xóa nhân viên khỏi dự án")
        print("5. Danh sách nhân viên theo dự án")
        print("6. Sắp xếp nhân viên theo số dự án")
        print("7. Quay lại menu chính")
        
        try:
            choice = input("Chọn chức năng (1-7): ").strip()
            Validators.validate_choice(choice, [str(i) for i in range(1, 8)])
            
            if choice == '1':
                add_project(company)
            elif choice == '2':
                list_projects(company)
            elif choice == '3':
                assign_employee_to_project(company)
            elif choice == '4':
                remove_employee_from_project(company)
            elif choice == '5':
                list_employees_by_project(company)
            elif choice == '6':
                sort_employees_by_projects(company)
            elif choice == '7':
                break
                
        except ValueError as e:
            print(f"Lỗi: {e}. Vui lòng thử lại.")
        except Exception as e:
            print(f"Lỗi không mong muốn: {e}")

def hr_management(company):
    while True:
        print("\nQUẢN LÝ NHÂN SỰ")
        print("1. Cho nhân viên nghỉ việc")
        print("2. Giảm lương nhân viên")
        print("3. Quay lại menu chính")
        
        try:
            choice = input("Chọn chức năng (1-3): ").strip()
            Validators.validate_choice(choice, [str(i) for i in range(1, 4)])
            
            if choice == '1':
                terminate_employee(company)
            elif choice == '2':
                reduce_employee_salary(company)
            elif choice == '3':
                break
                
        except ValueError as e:
            print(f"Lỗi: {e}. Vui lòng thử lại.")
        except Exception as e:
            print(f"Lỗi không mong muốn: {e}")

def add_project(company):
    try:
        name = input("Nhập tên dự án: ").strip()
        if not name:
            raise ValueError("Tên dự án không được để trống")
        description = input("Nhập mô tả dự án: ").strip()
        
        from models.project import Project
        proj = Project(name, description)
        company.add_project(proj)
        print(f"Đã thêm dự án: {name}")
    except ValueError as e:
        print(f"Lỗi: {e}")
    except Exception as e:
        print(f"Lỗi không mong muốn: {e}")

def list_projects(company):
    try:
        print(Formatters.format_project_list(company.projects))
    except Exception as e:
        print(f"Lỗi không mong muốn: {e}")

def assign_employee_to_project(company):
    try:
        emp_id = input("Nhập ID nhân viên: ").strip().upper()
        proj_name = input("Nhập tên dự án: ").strip()
        company.assign_employee_to_project(emp_id, proj_name)
        print(f"Đã phân công nhân viên {emp_id} vào dự án {proj_name}")
    except (EmployeeNotFoundError, ValueError) as e:
        print(f"Lỗi: {e}")
    except Exception as e:
        print(f"Lỗi không mong muốn: {e}")

def remove_employee_from_project(company):
    try:
        emp_id = input("Nhập ID nhân viên: ").strip().upper()
        proj_name = input("Nhập tên dự án: ").strip()
        company.remove_employee_from_project(emp_id, proj_name)
        print(f"Đã xóa nhân viên {emp_id} khỏi dự án {proj_name}")
    except (EmployeeNotFoundError, ValueError) as e:
        print(f"Lỗi: {e}")
    except Exception as e:
        print(f"Lỗi không mong muốn: {e}")

def list_employees_by_project(company):
    try:
        proj_name = input("Nhập tên dự án: ").strip()
        employees = company.get_employees_by_project(proj_name)
        print(Formatters.format_employees_by_project(employees, proj_name))
    except ValueError as e:
        print(f"Lỗi: {e}")
    except Exception as e:
        print(f"Lỗi không mong muốn: {e}")

def sort_employees_by_projects(company):
    try:
        employees = company.get_employees_sorted_by_projects()
        print(Formatters.format_employees_sorted_by_projects(employees))
    except IndexError as e:
        print(f"Lỗi: {e}")
    except Exception as e:
        print(f"Lỗi không mong muốn: {e}")

def terminate_employee(company):
    try:
        emp_id = input("Nhập ID nhân viên: ").strip().upper()
        reason = input("Nhập lý do nghỉ việc: ").strip()
        severance_str = input("Nhập số tiền đền bù (0 nếu không có): ").strip()
        severance = Validators.validate_salary(severance_str) if severance_str else 0.0
        company.terminate_employee(emp_id, reason, severance)
        print(f"Đã cho nhân viên {emp_id} nghỉ việc")
    except (EmployeeNotFoundError, InvalidSalaryError, ValueError) as e:
        print(f"Lỗi: {e}")
    except Exception as e:
        print(f"Lỗi không mong muốn: {e}")

def reduce_employee_salary(company):
    try:
        emp_id = input("Nhập ID nhân viên: ").strip().upper()
        amount_str = input("Nhập số tiền giảm lương: ").strip()
        amount = Validators.validate_salary(amount_str)
        reason = input("Nhập lý do giảm lương: ").strip()
        company.reduce_employee_salary(emp_id, amount, reason)
        print(f"Đã giảm lương nhân viên {emp_id} số tiền {amount:,.0f} VND")
    except (EmployeeNotFoundError, InvalidSalaryError, ValueError) as e:
        print(f"Lỗi: {e}")
    except Exception as e:
        print(f"Lỗi không mong muốn: {e}")
if __name__ == "__main__":
    main()