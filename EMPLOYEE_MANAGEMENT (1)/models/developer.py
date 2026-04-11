from .employee import Employee

class Developer(Employee):
    def __init__(self, id, name, salary, language):
        super().__init__(id, name, salary)
        self.language = language