import random

table = {'AClean':"Right",'ADirty':"Suck",'BClean':"Left",'BDirty':"Suck"}
for i in range(0,6):
    location = random.choice(["A","B"])
    condition = random.choice(["Clean","Dirty"])
    action = table[location + condition]
    print("["+location+", "+condition+"] : "+action)