from .employee import Employee

class Manager(Employee):
    def __init__(self, name, age, email, base_salary):
        super().__init__(name, age, email, base_salary, "Manager")

    def calculate_salary(self):
        bonus = self.performance_score * 200
        return self.base_salary * 1.5 + bonus