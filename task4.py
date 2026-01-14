class Employee:
    def __init__(self, n, s):
        self.name = n
        self._salary = s

    def get_salary(self):
        return self._salary

    def get_role(self):
        return "Employee"

class Manager(Employee):
    def __init__(self, n, s, b):
        super().__init__(n, s)
        self.bonus = b

    def get_role(self):
        return "Manager"

    def get_bonus(self):
        return self.bonus

def print_employee_details(emp_list):
    print("Name           | Role       | Salary    ")
    print("----------------------------------------")
    for e in emp_list:
        print(e.name + "          | " + e.get_role() + "   | $" + str(e.get_salary()))

if __name__ == "__main__":
    e1 = Employee("Alice", 50000)
    e2 = Employee("Bob", 55000)
    m1 = Manager("Charlie", 80000, 10000)

    l = [e1, e2, m1]

    print_employee_details(l)

    print("\nManager " + m1.name + " bonus: $" + str(m1.get_bonus()))
