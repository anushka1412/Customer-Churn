# List of employees
employees = [
    {'id': 101, 'name': 'Avi', 'age': 30, 'salary': 50000, 'department': 'HR', 'post': 'Manager'},
    {'id': 102, 'name': 'Dev', 'age': 25, 'salary': 45000, 'department': 'IT', 'post': 'Developer'},
    {'id': 103, 'name': 'Akhil', 'age': 28, 'salary': 48000, 'department': 'Finance', 'post': 'Analyst'},
    {'id': 104, 'name': 'Abhishek', 'age': 35, 'salary': 52000, 'department': 'IT', 'post': 'Team Lead'},
    {'id': 105, 'name': 'Gonda', 'age': 32, 'salary': 47000, 'department': 'HR', 'post': 'Recruiter'}
]

# Function 1: Display all employees
def display_all_employees():
    print("\nAll Employees:")
    print(f"{'ID':<5}{'Name':<12}{'Age':<6}{'Salary':<10}{'Department':<12}{'Post'}")
    print("-" * 60)
    for emp in employees:
        print(f"{emp['id']:<5}{emp['name']:<12}{emp['age']:<6}{emp['salary']:<10}{emp['department']:<12}{emp['post']}")

# Function 2: Search employee by name
def search_by_name(name):
    print(f"\nSearching for employee with name: {name}")
    found = False
    for emp in employees:
        if emp["name"].lower() == name.lower():
            print("Employee Found:")
            print(f"{'ID':<5}{'Name':<12}{'Age':<6}{'Salary':<10}{'Department':<12}{'Post'}")
            print(f"{emp['id']:<5}{emp['name']:<12}{emp['age']:<6}{emp['salary']:<10}{emp['department']:<12}{emp['post']}")
            found = True
            break
    if not found:
        print("Employee not found.")

# Function 3: Display employees by department
def employees_by_department(dept):
    print(f"\nEmployees in Department: {dept}")
    found = False
    for emp in employees:
        if emp["department"].lower() == dept.lower():
            if not found:
                print(f"{'ID':<5}{'Name':<12}{'Age':<6}{'Salary':<10}{'Department':<12}{'Post'}")
                print("-" * 60)
                found = True
            print(f"{emp['id']:<5}{emp['name']:<12}{emp['age']:<6}{emp['salary']:<10}{emp['department']:<12}{emp['post']}")
    if not found:
        print("No employees found in this department.")

# Function 4: Give a raise to a specific employee
def give_raise(name, amount):
    for emp in employees:
        if emp["name"].lower() == name.lower():
            emp["salary"] += amount
            print(f"\nSalary updated for {name}: New salary is {emp['salary']}")
            return
    print("\nEmployee not found.")

# Example usage:
display_all_employees()
search_by_name("Akhil")
employees_by_department("IT")
give_raise("Dev", 3000)
