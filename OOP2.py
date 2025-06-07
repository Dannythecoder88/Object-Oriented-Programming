class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last= last
        self.pay= pay
        self.email = first + "." + last + "@company.com"

#Wouldn't use self in this particular case because it isn't logical to want to have
#different values of employees in specific situations
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

# # of employees will be 0 here because we haven't established employees yet, 
#However on the second there will be, because we've added 2 employees.
print(Employee.num_of_emps)


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(Employee.num_of_emps)

















#.__dict__ shows all data values stored within the given variable. Emp_1 contains
# The name, pay, etc. but not the raise amount, whereas Employee does because
# It is the class variable
# print(Employee.__dict__)
# print(emp_1.__dict__)

#raises the raise amount from 1.04 to 1.05 for all employees
#Employee.raise_amount = 1.05

#Changes only emp_1's raise amount to 1.05
# emp_1.raise_amount = 1.05

#Now when you do .__dict__ emp_1 does have raise_amount as a variable because it was directly
#Assigned to it
# print(emp_1.__dict__)


# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# emp_1.apply_raise()
# print(emp_1.pay)

# emp_1.raise_amount
# Employee.raise_amount
