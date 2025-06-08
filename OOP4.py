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

#inherits all atributes and methods from Employee class, even if pass is put in it
#the Developer subclass will still be able to carry out emails, names, etc without any code needed
#but if you want to make it special, you must use special function and _init__ to add specific
#special operations that a Developer can Execute

class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        #passes first, last, and pay from the Employee function so that we don't 
        #need to rewrite it all, super is used when you have multiple inheritance classes

        #Employee.__init__(self,first, last, pay) - Would work same as super but super is
        #better in fuure because it cann inherit from multiple classes

        super().__init__(first,last,pay)
        self.prog_lang = prog_lang

# [] = list and if there are no emplyees it makes a list, but if there is
#it will set the employees = to the employee list
class Manager(Employee):
    raise_amt = 1.2
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

#If employee is not in employee list, the append function will add the employee
#into the list
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

#If employee is in self.employee, remove them (for instances if they get fired, etc.)
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

#prints employees in list with full name
    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'User', 60000, 'Java')


mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

#Tells us if an object is an instance of a class (is mgr_1 an instance of Manager)
print(isinstance(mgr_1, Manager))

#This otputs false bevcause although they both get instance from Employee,
#They are not part of eachothers inheretance because they don't inherit code from eachother
print(isinstance(mgr_1, Developer))

#Checks if Developer is a subclass of Employee
print(issubclass(Developer, Employee))

#Will output false because they are both subclasses of Employee, not of eachother
print(issubclass(Manager, Developer))


#mgr_1.add_emp(dev_2)
# mgr_1.remove_emp(dev_1)
# mgr_1.print_emps()


#print(dev_1.email)
# print(dev_1.prog_lang)


# print(dev_1.pay)
#Now uses Developer classes raise amount because we have a differemt raise amount
#in developer class function now
#dev_1.apply_raise()
# print(dev_1.pay)

#print(mgr_1.pay)
# mgr_1.apply_raise()
# print(mgr_1.pay)


#Checkes where data came from because at the moment the Developer class is empty
#but still had an output, and showed it got it from the Employee class
# print(help(Developer))