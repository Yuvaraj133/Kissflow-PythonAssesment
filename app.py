import json
with open('employee_data.json', 'r') as file:
    data = json.load(file)
department_salary = {}
department_count = {}

for employee in data:
    dept = employee['department']
    salary = employee['salary']
    if dept not in department_salary:
        department_salary[dept] = 0
        department_count[dept] = 0
    department_salary[dept] += salary
    department_count[dept] += 1

salary_summary={}
for dept in department_salary:
    average_salary = department_salary[dept] // department_count[dept]
    salary_summary[dept] = average_salary

with open('salary_summary.json', 'w') as file:
    json.dump(salary_summary, file, indent=4)
highest_salary_employee = max(data, key=lambda x: x['salary'])

print("Employee with the Highest Salary:")
print(f"Name: {highest_salary_employee['name']}")
print(f"Department: {highest_salary_employee['department']}")
print(f"Salary: {highest_salary_employee['salary']}")
