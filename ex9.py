num = int(input('donner un nombre '))
while(num<0):
    num = int(input('donner un nombre '))
num0 = num//2
i=0
c=0
while(i<=num0):
    i=i+1
    if(num % i == 0 ):
        c=c+i
if(num == c):
    print("le nombre est parfait")
else:
    print("le nombre n'est pas parfait")

