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

y = Employee("Manu", "Saxena", "1007")

print (x.Name())
print (y.GetEmployee())

print (y.Name())
print (x.GetEmployee())

'''

#Overloading and Overriding
Instead of using the methods "Name" and "GetEmployee" in our previous example, it might have been better to put this functionality into the "__str__" method.


class Person:

    def __init__(self, first, last, age):
        self.firstname = first
        self.lastname = last
        self.age = age

    def __str__(self):
        return self.firstname + " " + self.lastname + ", " + str(self.age)

class Employee(Person):

    def __init__(self, first, last, age, staffnum):
        super().__init__(first, last, age)
        self.staffnumber = staffnum

    #We have overridden the method __str__ from Person in Employee. By the way, we have overridden __init__ also
    def __str__(self):
        return super().__str__() + ", " +  self.staffnumber


x = Person("Marge", "Simpson", 36)
y = Employee("Homer", "Simpson", 28, "1007")

print(x)
print(y)'''
