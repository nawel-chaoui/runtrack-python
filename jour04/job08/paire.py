L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]

long = len(L)
som = 0 

for x in range(long):
    if L[x] % 2 == 0 :
        som = som + L[x]
        
print(som)