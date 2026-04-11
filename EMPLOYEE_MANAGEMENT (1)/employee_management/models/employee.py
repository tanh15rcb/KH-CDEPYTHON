from abc import ABC, abstractmethod
from datetime import datetime
from exceptions.employee_exceptions import InvalidAgeError, InvalidSalaryError, ProjectAllocationError

class Employee(ABC):
    _id_counter = 1

    def __init__(self, name, age, email, base_salary, position):
        self.validate_age(age)
        self.validate_salary(base_salary)
        Employee.validate_email(email)
        
        self.employee_id = self.generate_id()
        self.name = name
        self.age = age
        self.email = email
        self.base_salary = base_salary
        self.position = position
        self.projects = []
        self.performance_score = 0.0
        self.join_date = datetime.now()
        self.status = "active"  # active, terminated
        self.contract_end_date = None
        self.severance_pay = 0.0
        self.termination_reason = None

    @classmethod
    def generate_id(cls):
        emp_id = f"EMP{cls._id_counter:03d}"
        cls._id_counter += 1
        return emp_id

    @staticmethod
    def validate_age(age):
        if not (18 <= age <= 65):
            raise InvalidAgeError("Tuổi phải từ 18 đến 65")

    @staticmethod
    def validate_salary(salary):
        if salary <= 0:
            raise InvalidSalaryError("Lương phải lớn hơn 0")

    @staticmethod
    def validate_email(email):
        if '@' not in email:
            raise ValueError("Email phải chứa ký tự '@'")
        return email

    @abstractmethod
    def calculate_salary(self):
        """Tính lương theo chức vụ"""
        pass

    def assign_project(self, project_name):
        if len(self.projects) >= 5:
            raise ProjectAllocationError("Nhân viên đã có tối đa 5 dự án")
        if project_name not in self.projects:
            self.projects.append(project_name)

    def remove_project(self, project_name):
        if project_name in self.projects:
            self.projects.remove(project_name)

    def evaluate_performance(self, score):
        if not (0 <= score <= 10):
            raise ValueError("Điểm đánh giá phải từ 0 đến 10")
        self.performance_score = score

    def terminate(self, reason, severance_pay=0.0):
        """Cho nhân viên nghỉ việc"""
        self.status = "terminated"
        self.termination_reason = reason
        self.severance_pay = severance_pay
        self.contract_end_date = datetime.now()

    def reduce_salary(self, amount, reason):
        """Giảm lương nhân viên"""
        if amount <= 0:
            raise InvalidSalaryError("Số tiền giảm phải lớn hơn 0")
        if amount >= self.base_salary:
            raise InvalidSalaryError("Không thể giảm lương bằng hoặc lớn hơn lương hiện tại")
        self.base_salary -= amount
        # Có thể lưu lịch sử giảm lương nếu cần

    def __str__(self):
        status_str = f"Trạng thái: {self.status}"
        if self.status == "terminated":
            status_str += f", Lý do nghỉ: {self.termination_reason}, Đền bù: {self.severance_pay:,.0f} VND"
        return f"ID: {self.employee_id}, Tên: {self.name}, Tuổi: {self.age}, Email: {self.email}, Chức vụ: {self.position}, Lương cơ bản: {self.base_salary}, Dự án: {', '.join(self.projects) if self.projects else 'Không có'}, Điểm hiệu suất: {self.performance_score}, {status_str}"