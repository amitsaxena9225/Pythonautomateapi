# Overriding concept

class Person:
    # constructor
    def __init__(self, first, last):

        self.firstname = first
        self.lastname = last

    def Name(self):
        return self.firstname + " " + self.lastname


class Employee(Person):

    def __init__(self, first, last, staffnum):
        # inheriting __init__ function from base(parent)class
        Person.__init__(self, first,
                        last)  # calling from class Name/we can use Super also.super().__init__(first,last).Please note that we used super()) without arguments. This is only possible in Python3. We could have written "super(Employee, self).__init__(first, last, age)" which still works in Python3 and is compatible with Python2.

        self.staffnumber = staffnum

    def GetEmployee(self):
        return self.Name() + ", " + self.staffnumber


x = Person("Amit", "Saxena")

y = Employee("Sumit", "Saxena", "100")

print(x.firstname)

print(y.GetEmployee())