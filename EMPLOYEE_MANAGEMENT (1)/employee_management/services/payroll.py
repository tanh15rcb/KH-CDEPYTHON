from .company import Company

class Payroll:
    @staticmethod
    def calculate_total_salary(company):
        return sum(emp.calculate_salary() for emp in company.employees)

    @staticmethod
    def calculate_average_salary(company):
        if not company.employees:
            return 0
        return Payroll.calculate_total_salary(company) / len(company.employees)

    @staticmethod
    def get_salary_report(company):
        if not company.employees:
            raise IndexError("Chưa có dữ liệu nhân viên")
        report = []
        for emp in company.employees:
            salary = emp.calculate_salary()
            total_compensation = salary
            if emp.status == "terminated":
                total_compensation += emp.severance_pay
            report.append({
                'id': emp.employee_id,
                'name': emp.name,
                'position': emp.position,
                'salary': salary,
                'severance_pay': emp.severance_pay if emp.status == "terminated" else 0,
                'total_compensation': total_compensation,
                'status': emp.status
            })
        return report

    @staticmethod
    def get_top_performers(company, top_n=5):
        if not company.employees:
            raise IndexError("Chưa có dữ liệu nhân viên")
        sorted_emps = sorted(company.employees, key=lambda x: x.performance_score, reverse=True)
        return sorted_emps[:top_n]