class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last= last
        self.pay= pay
        self.email = first + "." + last + "@company.com"


    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

#used for debugging and logging for developers. What you want Python (developers)
#to see - a detailed, unambigous description. Would print Employee('Corey', 'Schafer', 50000)
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)
    
#more readable representation of object for user to see - nice, readable description
#Prints Corey Schafer - Corey.Schafer@company.com
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)
    
#allows us to tell code how we want to add both employees together, in this case
#we are adding my pay
    def __add__(self, other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullname())

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

#All __XXX__ functions are called dundr XXX functions 


# We get how many characters are in emp_1 name using __len__ function
# print(len(emp_1))

#Shows we must create __len__ 
# print(len('test'))
# print('test'.__len__())

#Add being used
# print(emp_1 + emp_2)

#Shows we must create __str__ and __repr__
# print(repr(emp_1))
# print(str(emp_1))
# print(emp_1.__repr__()) - same as print(repr(emp_1))
# print(emp_1.__str__()) - same as print(str(emp_1))

#Shows we must create __add__
#print(1+2)
# print(int.__add__(1,2))
# print('a'+'b')
# print(str.__add__('a', 'b'))
