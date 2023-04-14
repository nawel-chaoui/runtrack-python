def ma_list():
    x = ["pomme", "cerise" ,"orange", "melon"]
    x.insert(2, "mangue")
    return(','.join(x))

print(ma_list())