import re

class Validators:
    @staticmethod
    def validate_age(age_str):
        try:
            age = int(age_str)
            if not (18 <= age <= 65):
                raise ValueError("Tuổi phải từ 18 đến 65")
            return age
        except ValueError:
            raise ValueError("Tuổi phải là số nguyên")

    @staticmethod
    def validate_salary(salary_str):
        try:
            salary = float(salary_str)
            if salary <= 0:
                raise ValueError("Lương phải lớn hơn 0")
            return salary
        except ValueError:
            raise ValueError("Lương phải là số dương")

    @staticmethod
    def validate_email(email):
        if '@' not in email:
            raise ValueError("Email phải chứa ký tự '@'")
        # Simple regex for email
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, email):
            raise ValueError("Email không đúng định dạng")
        return email

    @staticmethod
    def validate_score(score_str):
        try:
            score = float(score_str)
            if not (0 <= score <= 10):
                raise ValueError("Điểm phải từ 0 đến 10")
            return score
        except ValueError:
            raise ValueError("Điểm phải là số từ 0 đến 10")

    @staticmethod
    def validate_choice(choice_str, options):
        if choice_str not in options:
            raise ValueError(f"Lựa chọn phải là một trong: {', '.join(options)}")
        return choice_str