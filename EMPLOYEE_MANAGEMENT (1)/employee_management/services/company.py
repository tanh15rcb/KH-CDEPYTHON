from models.manager import Manager
from models.developer import Developer
from models.intern import Intern
from models.project import Project
from exceptions.employee_exceptions import EmployeeNotFoundError, DuplicateEmployeeError

class Company:
    def __init__(self):
        self.employees = []
        self.projects = []

    def add_employee(self, employee):
        # Check for duplicate ID
        for emp in self.employees:
            if emp.employee_id == employee.employee_id:
                raise DuplicateEmployeeError(f"Nhân viên với ID {employee.employee_id} đã tồn tại")
        self.employees.append(employee)

    def remove_employee(self, employee_id):
        for emp in self.employees:
            if emp.employee_id == employee_id:
                self.employees.remove(emp)
                return
        raise EmployeeNotFoundError(employee_id)

    def find_employee(self, employee_id):
        for emp in self.employees:
            if emp.employee_id == employee_id:
                return emp
        raise EmployeeNotFoundError(employee_id)

    def list_employees(self):
        if not self.employees:
            raise IndexError("Chưa có dữ liệu nhân viên")
        return self.employees

    def get_employee_by_position(self, position):
        return [emp for emp in self.employees if emp.position == position]

    # Project management methods
    def add_project(self, project):
        # Check for duplicate project name
        for proj in self.projects:
            if proj.project_name == project.project_name:
                raise ValueError(f"Dự án '{project.project_name}' đã tồn tại")
        self.projects.append(project)

    def find_project(self, project_name):
        for proj in self.projects:
            if proj.project_name == project_name:
                return proj
        raise ValueError(f"Không tìm thấy dự án '{project_name}'")

    def assign_employee_to_project(self, employee_id, project_name):
        emp = self.find_employee(employee_id)
        proj = self.find_project(project_name)
        emp.assign_project(project_name)
        proj.assign_employee(employee_id)

    def remove_employee_from_project(self, employee_id, project_name):
        emp = self.find_employee(employee_id)
        proj = self.find_project(project_name)
        emp.remove_project(project_name)
        proj.remove_employee(employee_id)

    def get_employees_by_project(self, project_name):
        proj = self.find_project(project_name)
        employees = []
        for emp_id in proj.assigned_employees:
            try:
                emp = self.find_employee(emp_id)
                employees.append(emp)
            except EmployeeNotFoundError:
                continue  # Skip if employee not found
        return employees

    def get_employees_sorted_by_projects(self):
        """Sắp xếp nhân viên theo số lượng dự án từ nhiều nhất đến ít nhất"""
        if not self.employees:
            raise IndexError("Chưa có dữ liệu nhân viên")
        return sorted(self.employees, key=lambda x: len(x.projects), reverse=True)

    # HR management methods
    def terminate_employee(self, employee_id, reason, severance_pay=0.0):
        emp = self.find_employee(employee_id)
        emp.terminate(reason, severance_pay)
        # Có thể remove from projects
        for proj in self.projects:
            if employee_id in proj.assigned_employees:
                proj.remove_employee(employee_id)

    def reduce_employee_salary(self, employee_id, amount, reason):
        emp = self.find_employee(employee_id)
        emp.reduce_salary(amount, reason)