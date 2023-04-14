L = [10,20,30,20,10,50,60,40,80,50,40]
L_sans_doublons = []

for x in L:
    z = False
    for y in L_sans_doublons:
        if x == y:
            z = True
    if not z :
        L_sans_doublons += [x]

print(L_sans_doublons)