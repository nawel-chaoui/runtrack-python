L = [12, 15, 78, 18, 96, 74]

def exchange(L):
    change = L[-1]
    L[-1] = L[0]
    L[0] = change
    return L

print(exchange(L))