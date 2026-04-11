class Project:
    def __init__(self, project_name, description="", start_date=None, end_date=None):
        self.project_name = project_name
        self.description = description
        self.start_date = start_date or datetime.now()
        self.end_date = end_date
        self.assigned_employees = []  # List of employee IDs

    def assign_employee(self, employee_id):
        if employee_id not in self.assigned_employees:
            self.assigned_employees.append(employee_id)

    def remove_employee(self, employee_id):
        if employee_id in self.assigned_employees:
            self.assigned_employees.remove(employee_id)

    def get_employee_count(self):
        return len(self.assigned_employees)

    def __str__(self):
        return f"Dự án: {self.project_name}, Mô tả: {self.description}, Số nhân viên: {self.get_employee_count()}"