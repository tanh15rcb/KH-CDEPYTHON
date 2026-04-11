from .employee import Employee

class Manager(Employee):
    def __init__(self, id, name, salary):
        super().__init__(id, name, salary)