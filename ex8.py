def carree(num):
  return num*num

a = int(input('donner un nombre a'))
while(a<0):
    a = int(input('donner un nombre a'))
b = int(input('donner un nombre b'))

while(b<0):
    b = int(input('donner un nombre b'))

c = int(input('donner un nombre c'))
while(c<0):
    c = int(input('donner un nombre c'))
largest = 0

# if a > b and a > c :
#     largest = a
#     a=c
#     c=largest
# elif b > c :
#     largest = b
#     b = c
#     c = largest
# else :
#     largest = c

if (a >= b) and (a >= c):
   largest = a
   a=c
   c=largest
elif (b >= a) and (b >= c):
   largest = b
   b = c
   c = largest
   
else:
   largest = c
if(a+b>= c):
    print("les longueurs correspondent à un triangle")
if(carree(a)+carree(b)==carree(c) ):
    print("le triangle est rectangle")
elif(carree(a)+carree(b)==carree(c) and a==b):
    print("le triangle est isocèle et rectangle")
elif(a==b==c):
    print("le triangle est equilateral")





