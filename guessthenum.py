import random as rd
comp=rd.randint(1,20)
#print(comp)

chance=10
win=False
while(chance>=1):
    guess=int(input("guess between 1-20:"))
    if guess== comp:
        win=True
        break
    elif guess> comp:
        print("too high")
    else:
        print("too low")
    chance-=1
if win ==True:
    print("you won")
else:
    print("you loss number is",comp)

