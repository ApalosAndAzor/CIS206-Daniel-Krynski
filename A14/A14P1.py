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

# Manager Class
class Manager(Employee):
    def __init__(self, first_name="N/A", last_name="N/A", job_level=1, annual_salary=0):
        super().__init__(first_name, last_name, job_level, annual_salary)
        self.auto = "N/A"

    def Auto(self, automobile):
        self.auto = automobile

    def long_term_bonus(self):
        if self.job_level == 1:
            return 0.50 * self.annual_salary
        elif self.job_level == 2:
            return 0.40 * self.annual_salary
        elif self.job_level == 3:
            return 0.35 * self.annual_salary

# Start for Manager
manager = Manager(first_name="Alice", last_name="Smith", job_level=1, annual_salary=70000)
manager.Auto("Tesla Model S")

# Display for Manager
print(f"First Name: {manager.first_name}")
print(f"Last Name: {manager.last_name}")
print(f"Job Level: {manager.job_level}")
print(f"Annual Salary: {manager.annual_salary}")
print(f"Short Term Bonus: {manager.short_term_bonus}")
print(f"Long Term Bonus: {manager.long_term_bonus}")
print(f"Auto: {manager.auto}")