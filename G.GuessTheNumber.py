import random

a=random.randint(1,100)
#print(a)
print("I am thinking of a number bw 1 to 100")
print("guess what is that number ?")
print("I would tell you that the number you said is higher or lower in  comparison to my number")

while True:
    i=int(input("Enter the number"))
    if a<i:
        print("Higher")
    elif a>i:
        print("Lower")
    elif a==i:
        print("You did it!")
        break

