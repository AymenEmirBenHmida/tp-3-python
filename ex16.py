num = int(input('donner entier max '))

for x in range(1,num+1):
    for z in range(1,num+1):
        print("*",end ="")
        if(z == num):
            print("")

for x in range(1,num+1):
    y = x
    for z in range(1,x+1):
        print("*",end ="")
    print("")


for x in range(1,num+1):
    y = x
    for z in range(1,num+1):
        if(z==1 or z== num):
            print("*",end ="")
        else:
            print(" ",end ="")
    print("")


for x in range(1,num+1):
    y = x
    if(x== num):
        for c in range(1,num+1):
            print("*",end ="")
    else:

        for z in range(1,num+1):
            if(z==1 or z== y):
                print("*",end ="")
            else:
                print(" ",end ="")
        print("")

