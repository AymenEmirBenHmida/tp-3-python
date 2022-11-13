num2 = int(input('donner nombre2 '))
num1 = int(input('donner nombre '))
if(num1<0 and num2<0):
    print("le produit de deux nombre est positive")
elif(num1<0 and num2>0):
    print("le produit de deux nombre est negative")
elif(num1>0 and num2<0):
    print("le produit de deux nombre est negative")
else:
    print("le produits de deux nombre est positive")