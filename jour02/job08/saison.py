def on_mange_quoi_quand(type, saison):
    if type == "fruits" and saison == "hiver" :
        return("orange, mandarine, kiwi")
    elif type == "fruits" and saison == "été" :
        return("poire, fraise, cassis")
    elif type == "légume" and saison == "hiver" :
        return("carotte, topinambour, endive")
    elif type == "légume" and saison == "été" :
        return("artichaut, aubergine, navet")
    else : 
        return("RIEN")

print(on_mange_quoi_quand("fruits", "été"))
print(on_mange_quoi_quand("légume", "été"))