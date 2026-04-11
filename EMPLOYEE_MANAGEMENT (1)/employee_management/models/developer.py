from .employee import Employee

class Developer(Employee):
    def __init__(self, name, age, email, base_salary):
        super().__init__(name, age, email, base_salary, "Developer")

    def calculate_salary(self):
        bonus = self.performance_score * 150
        return self.base_salary * 1.2 + bonus