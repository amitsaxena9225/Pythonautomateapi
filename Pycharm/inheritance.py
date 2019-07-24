

class Parent:

    def func(self):

        print ("this is parent class func")

class mother(Parent):

    def func2(self):

        print ("this is mother class func")


class Child(mother):

    def func1(self):

        print ("this is child class func")


p = Parent()

p.func()

c = Child()

c.func1()

c.func()

