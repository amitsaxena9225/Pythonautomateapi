
class Example:

    raiise = 1.05   # class variable

    def __init__(self, first, last, pay):

        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@' + 'company.com'

    def fullname(self):
        return self.first + self.last

    def hike(self):

        #self.pay = self.pay * 1.04        # hardcoded
        #self.pay = self.pay * self.raiise  # using instance variable
        self.pay =self.pay * Example.raiise # using class variable

        return self.pay


class Developer(Example):

    def __init__(self, first, last, pay, lang):
        #super.__init__(self, first, last, pay)
        #super(Developer,self).__init__( first, last, pay)
        Example.__init__(self, first, last, pay)
        self.lang = lang

    def domain(self):

        return self.lang


class Manager(Example):

    def __init__(self, first, last, pay, emp=None):

        #super(Manager, self).__init__(first, last, pay)
        Example.__init__(self, first, last, pay)

        if emp is None:
            self.emp = []

        else:
            self.emp = emp

    def add_emp(self, emps):

        if emps not in self.emp:
            self.emp.append(emps)

    def remove_emp(self,emps):

        if emps in self.emp:
            self.emp.remove(emps)

    def print_emp(self):

        for i in self.emp:
            print(i.fullname())

de = Developer('Ami', "Saxen", 200000000000, 'python')

de1 = Developer('Am', "Saxe", 2000000000000000, 'JAVA')

mn = Manager('Manish','Kothari',5000000000)


ex = Example('Amit', 'Saxena', 2000000)
'''
print(ex.fullname())
print(ex.last)
print(ex.first)
print(ex.pay)
print(ex.hike())

print(de.fullname())
print(de.first)
print(de.pay)
print(de.hike())
print(de1.domain())

print(mn.fullname())
print(mn.emp)
#print(mn.domain())
'''
print(mn.add_emp("amit saxena"))
print(mn.print_emp())

