from .employee import Employee

class Intern(Employee):
    def __init__(self, name, age, email, base_salary):
        super().__init__(name, age, email, base_salary, "Intern")

    def calculate_salary(self):
        bonus = self.performance_score * 50
        return self.base_salary * 0.8 + bonus