moy = int(input('donner moyenne '))
while(moy>20 or moy<0):
    moy = int(input('donner moyenne '))

if(moy>=16):
    print("mention : « très bien ")
elif(moy<16 and moy >=14):
    print("mention « bien »")
elif(moy>=12 and moy<14):
    print("mention Assez bien")
elif(moy<=10 and moy<12):
    print("mention passable")