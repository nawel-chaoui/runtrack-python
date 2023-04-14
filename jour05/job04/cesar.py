# Jules César, général et stratège romain, a été le premier militaire officiel à chiffrer ses messages. Sa méthode était assez simple : 
# il décalait les lettres de 3 rangs dans l'alphabet.

# Créer une fonction à laquelle on donne un message et un décalage, et la fonction
# renvoie alors le message décalé dans l'alphabet. Il faudra gérer le dépassement ('z' décalé vers la droite revient sur 'a', 
# et 'a' décalé vers la gauche revient sur 'z').
 
def cesar(msg="", clef=0): 
	alphabet="abcdefghijklmnopqrstuvwxyz" 
	chiffre="" 
  
	for l in msg.lower(): 
		pos=alphabet.find(l) 
  
		if pos != -1: 
			chiffre+=alphabet[(pos+clef) % len(alphabet)] 
		else: 
			chiffre+=l 
	 
	return chiffre  
  
message= input("Message à chiffrer :")
chiffre=cesar(message, 3) 
dechiffre=cesar(chiffre, -3) 
print(chiffre, "=>", dechiffre)