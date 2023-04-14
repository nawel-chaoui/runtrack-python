# Un gardien de phare va aux toilettes cinq fois par jour. Or les WC sont au rez-de-chaussée…
# Écrire une fonction qui reçoit en paramètres, le nombre de marches du phare et la hauteur de chaque marche (en cm), 
# cette fonction doit calculer combien de mètre le gardien effectué par semaine pour aller aux toilettes. 
# La sortie du code doit être : Pour x marches de y cm, le gardien parcours z.zz m par semaine.

# On n'oubliera pas : 
#                    qu'une semaine comporte 7 jours ; 
#                    qu'une fois en bas, le gardien doit remonter ; 
#                    que le résultat est à exprimer en m.
 
def distance_parcourue(nb, h) :  
    print(f"Pour {nb} marches de {h}cm, il parcourt {nb*h*2*5*7/100.0:.2f}m par semaine.") 
  
nbMarches = int(input("Combien de marches ?"))  
hauteurMarche = int(input("Hauteur d'une marche (cm) ?"))  
  
distance_parcourue(nbMarches, hauteurMarche)
