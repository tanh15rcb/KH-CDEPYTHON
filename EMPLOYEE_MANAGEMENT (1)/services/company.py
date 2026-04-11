class Company:
    def __init__(self):
        self.employees = []

    def add(self, emp):
        self.employees.append(emp)

    def show_all(self):
        for e in self.employees:
            print(e.show())

    def find_by_id(self, id):
        for e in self.employees:
            if e.id == id:
                return e
        return None

    def total_salary(self):
        return sum(e.salary for e in self.employees)

    def max_salary(self):
        return max(self.employees, key=lambda e: e.salary)

    def excellent(self):
        return [e for e in self.employees if e.performance > 8]

    def need_improve(self):
        return [e for e in self.employees if e.performance < 5]