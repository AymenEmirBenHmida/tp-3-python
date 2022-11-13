sexe = input('donner sexe M/F ').upper()

while(sexe not in["F","M"] ):
    sexe = input('donner sexe M/F ')
taille = int(input('donner la taille (cm)'))
poids = int(input('donner le poids (kg)'))
indice = (poids/(taille*taille))
print( indice)
if((indice >= 25 and sexe =="M")or(indice == 23 and sexe =="F")):
    print("vous devriez surveiller votre alimentation")
elif((indice >= 19 and sexe =="M")or(indice == 18 and sexe =="F")):
    print("Vous devriez prendre des forces ")
else:
    print("Vous êtes à votre poids de forme")
