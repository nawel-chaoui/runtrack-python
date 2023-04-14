L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]

long = len(L)

x =  1

for y in range(long):
    if 25 <= L[y] <= 90:
        x = x*L[y]
        
print(x)