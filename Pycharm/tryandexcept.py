
try:

    a =open("/Users/apple/PycharmProjects/Pycharm/conditonal_statement.txt",'o')

    a.write("pravin")


except Exception as e:
    print e

except:

    print "something went wrong"

