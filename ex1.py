bornI = int(input('donner borne inf '))

bornS = int(input('donner borne sup '))
while(bornS<=bornI):
    bornS = int(input('donner borne sup '))
num = int(input('donner nombre'))
if(num<= bornS and num>= bornI):
    print("votre nombre est dans l'intervale")
else:
    print("votre nombre n'est dans l'intervale")