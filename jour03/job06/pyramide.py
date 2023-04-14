import string
pièces = (string.ascii_lowercase)*10   

x = 1
while x<=len(pièces):
        print(pièces[:x])
        pièces=pièces[x:]
        x+=1