# Class
class Employee:
    def __init__(self, first_name="N/A", last_name="N/A", job_level=1, annual_salary=0):
        self.first_name = first_name
        self.last_name = last_name
        self.job_level = job_level
        self.annual_salary = annual_salary
        if self.job_level == 1:
            self.short_term_bonus = 0.25 * self.annual_salary
        elif self.job_level == 2:
            self.short_term_bonus = 0.20 * self.annual_salary
        elif self.job_level == 3:
            self.short_term_bonus = 0.10 * self.annual_salary
        self.long_term_bonus = 0.10 * self.annual_salary

# Start
emp = Employee(first_name="John", last_name="Doe", job_level=2, annual_salary=50000)

# Display
print(f"First Name: {emp.first_name}")
print(f"Last Name: {emp.last_name}")
print(f"Job Level: {emp.job_level}")
print(f"Annual Salary: {emp.annual_salary}")
print(f"Short Term Bonus: {emp.short_term_bonus}")
print(f"Long Term Bonus: {emp.long_term_bonus}")