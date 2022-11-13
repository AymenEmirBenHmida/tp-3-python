from random import randint
a=randint(0,100)

guess = int(input('donner un guess '))
while(guess!= a):
    if(guess>a):
        print("votre numero est trop grand")
    elif(guess<a):
        print("votre numero est trop petit")
    guess = int(input('donner un guess '))

print("votre numero est vrai \n yay")
