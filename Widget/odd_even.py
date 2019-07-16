class Even_odd:

    def __init__(self,lst):

        self.lst = [1, 2, 3, 4, 5, 6, 7, 9, 11]

    def even(self):

        for i in self.lst:

            if i % 2 == 0:

                print(i, "even")

    def odd(self):

        for i in self.lst:

            if i % 2 != 0:
                print(i, "odd")


ob = Even_odd([1, 2, 3, 4, 5, 6, 7])


(ob.even())

(ob.odd())

