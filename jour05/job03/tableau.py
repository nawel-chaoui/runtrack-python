# Écrire une fonction qui, recevant une taille n en paramètre, affiche un tapis de n+1 lignes/n+1 colonnes traversé par une diagonale.

def tapis(n): 
	print("+" + "-" * (n+1) + "+") 

	for i in range(n+1): 
		print("|" + "#" * (n-i) + " " + "#" * i + "|") 
  
	print("+" + "-" * (n+1) + "+") 
  
tapis(int(input("Taille: ")))