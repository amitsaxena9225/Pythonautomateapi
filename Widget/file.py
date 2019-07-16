




with open("/Users/apple/PycharmProjects/Widget/chnadrika.txt",'w') as filename:

    a1='''
    kvbvbdvbdvbdvbvbvbvbvb
        nejnfenfejfnenfefej
        fejfeefneffnef
        flkefnefnekfefmef
        fenfkelfm;elfenfe
        fnejfnefmefe
        fefnefekfefnelfnebfebfkejf
        febnfelkfe
        eebfekfke;fe
      '''
    a ="amit saxena ,jbbvbebvvbkbkebve"
    #filename.write("AMit Saxena","he is great man")
    filename.write(a)
    filename.writelines(a1)
    print(filename.tell())
    print(filename.seekable())
    print(filename.seek(20))


