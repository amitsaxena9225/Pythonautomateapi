

class parent:

    def func(self):

        print("12345")

    def func1(self):

        print("abcd")

    def ovr(self):

        print("Amit")


class child(parent):


    def func2(self):

        print("XXXXXXX")

    def func3(self):

        print("!@#$$^^&*")




ch = child()

ch.func1()