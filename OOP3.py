class Employee:
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last= last
        self.pay= pay
        self.email = first + "." + last + "@company.com"

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

#cls is the class variable name because if you used class it is actually 
#a key word in Python that creates a class, so cls is used as the variable, 
#similar to self for as instance variable, cls is the class variable

# the @classmethod function can change attributes within the class such 
#as if originally species = 'Canine' the @classmethod function could do this:

# class Dog:
#     species = "Canine"

#      @classmethod
#     def change_species(cls, new_species):
#         cls.species = new_species

# Dog.change_species("Wolf")

# print(Dog.species) aand this would change the species from Canine to
#Wolf as output


    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

#Creates new Employee for any new employee rather than needing to change 
#code for specific employees to make new ones
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first,last, pay)

#Static methods dont take cls or self and you can just driectly put in 
#the variable needed. It doesn't have access to class or self methods. 
#It is a basic function within a class.

# The days of the week start with 0 as monday and go to 6 as saturday 
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

# imports datime module, makes new date, and checks if date is weekday, 
# if is will result in true, if not with false
import datetime
my_date = datetime.date(2025, 6, 9)
print(Employee.is_workday(my_date))


# emp_str_1 = 'John-Doe-700000'
# emp_str_2 = 'Steve-Smith-36000'
# emp_str_3 = 'Jane-Doe-900000'

#calls on classmethod to make employee
# new_emp_1 = Employee.from_string(emp_str_1)


#this takes the employee string 1 (emp_str_1) and deletes the '-' marks
#to get the first name, last name, and pay. It then creates a new emplyee
# with the new_emp_1 = Employee(first, last, pay) 

# first, last, pay = emp_str_1.split('-')

# new_emp_1 = Employee(first,last, pay)

# print(new_emp_1.email)
# print(new_emp_1.pay)






#Changes all raise amounts as explained before changes class amount from 
# what was previously established

#Employee.set_raise_amt(1.05)

# print(Employee.raise_amt)
# print(emp_1.raise_amt)
# print(emp_2.raise_amt)
