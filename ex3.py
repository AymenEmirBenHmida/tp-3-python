heure = int(input(" nombre d'heure "))
prix = float(input(" donner prix unitaire "))

def percent50(prix,heurSupp):
    prixN = prix+prix*0.5
    return prixN*heurSupp
def percent70(prix,heurSupp):
    prixN = prix+prix*0.75
    return prixN*heurSupp
def percent100(prix,heurSupp):
    prixN = prix+prix
    return prixN*heurSupp


while(prix<0):
    prix = int(input(" donner prix unitaire "))

prixT = 0

heureS = heure -39
if(heureS<=0):
    prixT = heure * prix
    print(" le salaire est "+str(prixT))
elif(heureS <=5):
    print(str(heureS))
    print("salaire = "+str(percent50(prix,heureS)))
elif(heureS <=10):
    print(str(heureS-4))
    prixT = percent50(prix,5)+percent70(prix,heureS-5)
    print("salaire = "+ str(prixT))
else:
   
    prixT = percent50(prix,5)+percent70(prix,5)+percent100(prix,heureS-10)
    print("salaire = "+ str(prixT))


