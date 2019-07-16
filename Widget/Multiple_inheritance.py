class Father:

    def func1(self):

        print("func1 function , This is a first function of the Fathert class.")

    def func2(self):
        print("func2 function , This is a second function of the Father class.")


class Mother:

    def func3(self):
        print("func3 function , This is a first function of the  Mother class.")

    def func4(self):

        print("func4 function , This is a second function of the  Mother class.")


class Child(Father, Mother):

    def func5(self):
        print("func5 function , This is a first function of the  child class.")

    def func6(self):

        print("func5 function , This is a second function of the  child class.")


ch = Child()

ch.func1()

ch.func3()

ch.func5()

