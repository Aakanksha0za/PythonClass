base_salary = "30000"
base_salary = int(base_salary)

def calculate_salary():
    bonus = 5000
    tax = 3000
    net_salary = base_salary + bonus - tax
    print("Net Salary:", net_salary)

calculate_salary()