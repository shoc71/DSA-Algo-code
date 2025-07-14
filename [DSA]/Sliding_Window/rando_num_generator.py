import random

list1 = []

for _ in range(20):
    r1 = random.random()
    r2 = random.randrange(1,10)

    list1.append(round(r1 * r2, 4))
    
    
list2 = [round(random.random() * random.randrange(10, 100),4) for _ in range(20)]    

# print(list1)
print(list2)

# print(random.choice([1,2,3,4]))