class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"{self.name} {self.salary} ({self.age})"

class EmployeeManager:
    def __init__(self):
        self.employees = []

    def add_employee(self):
        print('\nEnter employee data:')
        name = input('Enter name: ')
        age = int(input('Enter age: '))
        salary = int(input('Enter salary: '))
        self.employees.append(Employee(name, age, salary))

    def list_employees(self):
        if len(self.employees) == 0:
            print('\nNo employees')
            return
        print('\n')
        for emp in self.employees:
            print(emp)

    def delete_employees_with_age(self, age_from, age_to):
        for idx in range(len(self.employees) - 1, -1, -1):
            emp = self.employees[idx]
            if age_from <= emp.age <= age_to:
                print(f'\tDeleting {emp.name}')
                self.employees.pop(idx)

    def find_employee_by_name(self, name):
        for emp in self.employees:
            if emp.name == name:
                return emp
        return None

    def update_salary_by_name(self, name, salary):
        emp = self.find_employee_by_name(name)
        if emp is None:
            print('Error: No employee with such a name')
        else:
            emp.salary = salary

class FrontendManager:
    def __init__(self):
        self.employee_manager = EmployeeManager()

    def print_menu(self):
        print('\nProgram Options:')
        messages = [
            '1) Add a new employee',
            '2) List all employees',
            '3) Delete by age range',
            '4) Update salary given a name',
            '5) End the program'
        ]
        print('\n'.join(messages))
        msg = f'Enter your choice (from 1 to {len(messages)}): '
        return self.input_valid_int(msg, 1, len(messages))

    def input_valid_int(self, prompt, min_value=float('-inf'), max_value=float('inf')):
        while True:
            try:
                value = int(input(prompt))
                if min_value <= value <= max_value:
                    return value
                else:
                    print(f"Please enter a value between {min_value} and {max_value}.")
            except ValueError:
                print("Invalid input. Please enter an integer.")

    def run(self):
        while True:
            choice = self.print_menu()

            if choice == 1:
                self.employee_manager.add_employee()
            elif choice == 2:
                self.employee_manager.list_employees()
            elif choice == 3:
                age_from = self.input_valid_int('Enter age from: ', 0)
                age_to = self.input_valid_int('Enter age to: ', age_from)
                self.employee_manager.delete_employees_with_age(age_from, age_to)
            elif choice == 4:
                name = input('Enter name: ')
                salary = self.input_valid_int('Enter new salary: ', 0)
                self.employee_manager.update_salary_by_name(name, salary)
            else:
                break

if __name__ == '__main__':
    app = FrontendManager()
    app.run()