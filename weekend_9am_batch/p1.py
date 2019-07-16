
'''def prime(*args):

    for a in  args:
        print(type(a))

        for i in a:
            print(type(i))

            if i > 2:
                for j in range(2, i):
                    if i % j == 0:
                        print(i, "number is not prime")
                        break
                else:

                    print(i, "number is prime")


prime([7, 2, 3, 4, 5, 6, 7, 8, 8])



def prime(a):

        for i in a:
            print(type(i))

            if i > 2:
                for j in range(2, i):
                    if i % j == 0:
                        print(i, "number is not prime")
                        break
                else:

                    print(i, "number is prime")


prime([7, 2, 3, 4, 5, 6, 7, 8, 8])
'''




noprme=[j for i in range(2,8) for j in range(i*2,50,i)]

prime=[x for x in range(2,50) if x not in noprme]

print(prime)

print(noprme)
