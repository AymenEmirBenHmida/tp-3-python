num = int(input('donner un nombre '))
while(num<0):
    num = int(input('donner un nombre '))

num0 = num//2
print(str(num0))
i=0
c=0
test = False
while(i<num0 and test==False ):
    i=i+1
    print(" i = "+str(i))
    if(i!=1):
        if(num % i == 0 ):
            test = True
if(test == False):
    print("le nombre est premier")
else:
    print("le nombre n'est pas premier")

