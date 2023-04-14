L = [8,24,48,2,16]

nb = len(L)
multiples = 0 

for x in range(nb):
    if L[x] % 3 == 0:
        multiples = multiples+1
        
print(multiples)
