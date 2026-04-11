class Formatters:
    @staticmethod
    def format_employee_list(employees):
        if not employees:
            return "Không có nhân viên nào."
        lines = ["Danh sách nhân viên:"]
        lines.append("-" * 80)
        for emp in employees:
            lines.append(f"ID: {emp.employee_id}")
            lines.append(f"Tên: {emp.name}")
            lines.append(f"Tuổi: {emp.age}")
            lines.append(f"Email: {emp.email}")
            lines.append(f"Chức vụ: {emp.position}")
            lines.append(f"Lương cơ bản: {emp.base_salary:,.0f} VND")
            lines.append(f"Dự án: {', '.join(emp.projects) if emp.projects else 'Không có'}")
            lines.append(f"Điểm hiệu suất: {emp.performance_score}")
            lines.append("-" * 80)
        return "\n".join(lines)

    @staticmethod
    def format_salary_report(report):
        if not report:
            return "Không có dữ liệu lương."
        lines = ["Báo cáo lương:"]
        lines.append("-" * 90)
        lines.append(f"{'ID':<10} {'Tên':<20} {'Chức vụ':<15} {'Lương':>15} {'Đền bù':>15} {'Tổng':>15} {'Trạng thái':<10}")
        lines.append("-" * 90)
        for item in report:
            lines.append(f"{item['id']:<10} {item['name']:<20} {item['position']:<15} {item['salary']:>15,.0f} {item['severance_pay']:>15,.0f} {item['total_compensation']:>15,.0f} {item['status']:<10}")
        total = sum(item['total_compensation'] for item in report)
        lines.append("-" * 90)
        lines.append(f"{'Tổng chi phí:':<75} {total:>15,.0f} VND")
        return "\n".join(lines)

    @staticmethod
    def format_project_list(projects):
        if not projects:
            return "Không có dự án nào."
        lines = ["Danh sách dự án:"]
        lines.append("-" * 60)
        for proj in projects:
            lines.append(f"Tên: {proj.project_name}")
            lines.append(f"Mô tả: {proj.description}")
            lines.append(f"Số nhân viên: {proj.get_employee_count()}")
            lines.append("-" * 60)
        return "\n".join(lines)

    @staticmethod
    def format_employees_by_project(employees, project_name):
        if not employees:
            return f"Không có nhân viên nào tham gia dự án '{project_name}'."
        lines = [f"Danh sách nhân viên tham gia dự án '{project_name}':"]
        lines.append("-" * 80)
        for emp in employees:
            lines.append(f"ID: {emp.employee_id}, Tên: {emp.name}, Chức vụ: {emp.position}")
        lines.append("-" * 80)
        return "\n".join(lines)

    @staticmethod
    def format_employees_sorted_by_projects(employees):
        if not employees:
            return "Không có nhân viên nào."
        lines = ["Nhân viên sắp xếp theo số lượng dự án (từ nhiều nhất):"]
        lines.append("-" * 80)
        for emp in employees:
            lines.append(f"ID: {emp.employee_id}, Tên: {emp.name}, Số dự án: {len(emp.projects)}, Dự án: {', '.join(emp.projects) if emp.projects else 'Không có'}")
        lines.append("-" * 80)
        return "\n".join(lines)

    @staticmethod
    def format_menu():
        menu = """
HỆ THỐNG QUẢN LÝ NHÂN VIÊN

1. Thêm nhân viên mới
2. Xóa nhân viên
3. Tìm nhân viên theo ID
4. Hiển thị danh sách nhân viên
5. Phân công dự án
6. Đánh giá hiệu suất
7. Tính lương và báo cáo
8. Thống kê
9. Quản lý dự án
10. Quản lý nhân sự
11. Thoát

Chọn chức năng (1-11):
"""
        return menu