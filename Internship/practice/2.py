class Employee:
    def _init_(self, id, name,email, age, password, salary):
        self.id = id
        self.name = name
        self.email=email
        self.age = age
        self.password = password
        self.salary = salary

    def display_employee(self):
        print(f"ID: {self.id}, Name: {self.name},Email : {self.email} ,Age: {self.age}, Salary: {self.salary}")

class EmployeeDatabase:
    def _init_(self):
        self.employee_list = []

    def add_employee(self, employee):
        self.employee_list.append(employee)

    

    def sort_by_salary(self):
        self.employee_list.sort(key=lambda x: x.salary)
    
    def sort_by_age(self):
        self.employee_list.sort(key=lambda a: a.age)

    def view_employee(self):
        for employee in self.employee_list:
            employee.view_employee()

if _name_ == '_main_':
    emp_db = EmployeeDatabase()

    num_employees = int(input("Enter the number of employees to add: "))
    for i in range(num_employees):
        id = int(input(f"Enter employee {i+1} ID: "))
        name = input(f"Enter employee {i+1} name: ")
        email=input(f"Enter employee {i+1} email:")        
        age = int(input(f"Enter employee {i+1} age: "))
        password = input(f"Enter employee {i+1} password: ")
        salary = int(input(f"Enter employee {i+1} salary: "))

        emp = Employee(id, name,email, age, password, salary)
        
    emp_db.add_employee(emp)

    emp_db.view_employee(emp)
    emp_db.sort_by_salary()

    emp_db.sort_by_age()

    emp_db.display_employees()