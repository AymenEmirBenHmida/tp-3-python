num = int(input('donner un nombre '))
while(num<0):
    num = int(input('donner un nombre '))
i = 0
sum = 1
while(i < num):
    i = i+1
    sum = sum*i

print(i)
print("resultat en utilisant while = "+str(sum))

sum2 = 1
for x in range(1,num+1):
    sum2  = sum2 * x

print("resultat en utilisant for = "+str(sum2))