class GrandFather:

    def func1(self):

        print("func1 function , This is a first function of the GrandFather class.")

    def func2(self):
        print("func2 function , This is a second function of the GrandFather class.")


class Father:

    def func3(self):
        print("func3 function , This is a first function of the  Father class.")

    def func4(self):

        print("func4 function , This is a second function of the  Father class.")


class Child(Father):

    def func5(self):
        print("func5 function , This is a first function of the  child class.")

    def func6(self):

        print("func5 function , This is a second function of the  child class.")

    def func2(self):
        print("func2 function , This is a second function of the child class.")


class GrandChild(Child, GrandFather):

    def func7(self):
        print("func5 function , This is a first function of the  GrandChild class.")

    def func8(self):

        print("func5 function , This is a second function of the  GrandChild class.")


grch = GrandChild()

grch.func2()
