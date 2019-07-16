class Parent(Child):

    def func1(self):

        print("func1 function , This is a first function of the parent class.")

    def func2(self):
        print("func2 function , This is a second function of the parent class.")


class Child:

    def func3(self):
        print("func3 function , This is a first function of the  child class.")

    def func4(self):

        print("func4 function , This is a second function of the  child class.")


ch = Child()

par = Parent()

# Access only child class function when we are not inheriting parent class

'''print(ch.func3())

print(ch.func4())

print(ch.func1())

print(ch.func2())'''

print(par.func3())







