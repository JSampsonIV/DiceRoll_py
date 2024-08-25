import random

total = 0
count = 0
maxd4 = 0
maxd4 = 0
maxd6 = 0
maxd8 = 0
maxd10 = 0
maxd12 = 0
maxd20 = 0
print("Rolling until all dice roll their maximum value")
while (total!=60):
    d4 = random.randint(1,4)
    if (d4==4):
        maxd4+=1
    d6 = random.randint(1, 6)
    if (d6==6):
        maxd6+=1
    d8 = random.randint(1, 8)
    if (d8==8):
        maxd8+=1
    d10 = random.randint(1, 10)
    if (d10==10):
        maxd10+=1
    d12 = random.randint(1, 12)
    if (d12==12):
        maxd12+=1
    d20 = random.randint(1, 20)
    if (d20==20):
        maxd20+=1
    total = d4 + d6 + d8 + d10 + d12 + d20
    print("Total: "+str(total))
    count+=1

print(f"Rolled all maximum values after {count:.2e} rolls, with {maxd4:.2e} max d4 rolls, {maxd6:.2e} max d6 rolls, {maxd8:.2e} max d8 rolls, {maxd10:.2e} max d10 rolls, {maxd12:.2e} max d12 rolls, and {maxd20:.2e} max d20 rolls")