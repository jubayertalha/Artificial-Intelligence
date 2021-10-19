import random

for i in range(5):
    location = random.choice(["A", "B"])
    condition = random.choice(["Clean", "Dirty"])
    print("["+location+", "+condition+"] : ",end='')
    if condition=="Dirty":
        print("Suck")
    elif location=="A":
        print("Right")
    elif location=="B":
        print("Left")