class Employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary
        self.performance = 0

    def show(self):
        return f"{self.id} - {self.name} - {self.salary} - {self.performance}"