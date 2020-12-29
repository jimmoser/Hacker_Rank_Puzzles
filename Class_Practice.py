class Employee:
    num_of_emps = 0
    raise_amt = 1.05

    def __init__(self, first, last, pay, role):
        self.first = first
        self.last = last
        self.pay = pay
        self.role = role

        Employee.num_of_emps += 1

    def full_name(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(Employee.raise_amt * self.pay)

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay, role = emp_str.split('-')
        return cls(first, last, pay, role)

emp1 = Employee('Jim', 'Moser', 10000, 'Math Teacher')
emp2 = Employee('Jeff', 'Bomber', 20000, 'Programmer')
str1 = "Sam-Wolfe-20000-Teacher"
str2 = "Peter-Piper-90000-Flutist"
str3 = "Jack-Johnson-1000-Singer"

emp3 = Employee.from_string(str1)
emp4 = Employee.from_string(str2)
emp5 = Employee.from_string(str3)

emp1.apply_raise()
print(emp1.pay)
print(emp1.first)
print(emp2.full_name())
print(Employee.num_of_emps)
print(emp3.pay)
print(emp4.last)
print(emp5.role)
