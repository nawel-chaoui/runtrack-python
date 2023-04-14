for nb in range(1000):
    if nb > 1:
        for x in range (2, nb):
             if (nb % x) == 0:
                break
        else:
            print(nb)
