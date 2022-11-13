# Calcul d'un PGCD par différences successives 

a=int(input("Valeur de a ?")) 
b=int(input("Valeur de b ?")) 
def pgcd(a,b):
    while a!=b: 
        d=abs(b-a) 
        b=a 
        a=d 
    # print("pgcd=",d)
    return d 
if(a>b):
    print("pgcd = "+str(pgcd(a-b,b)))
elif(b>a):
    print("pgcd = "+str(pgcd(a,b-a)))
else:
    print("pgcd = "+str(a))


    