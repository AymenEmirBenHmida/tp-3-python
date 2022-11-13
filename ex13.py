num = int(input('donner entier max '))
# print(str(10%5))
while(num<0):
    num = int(input('donner entier max '))
sum = 0
sumInv = 0
prod = 1
for x in range(1,num+1):
    if( x%5!= 0):
        sum = sum + x
        sumInv = sumInv + (1/x)
        prod = prod * x

print("la somme des nombres est = "+str(sum)+" , la somme des inverses = "+ "{:.2f}".format(sumInv)+" , le produit des nombres = "+str(prod))
