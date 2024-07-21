l = [9,3,2,1,10,5]

def tri_selection(liste):
    add = liste[0]
    newliste = []

    while len(liste) != 0:
        for x in liste:
            if add > x:
                add = x
        newliste.append(add)
        liste.remove(add)
        if len(liste) != 0:
            add = liste[0]
    return newliste

def tri_insertion(liste):
    check_1 = 0
    check_2 = 1
    print(liste)
    while check_2 != len(liste):
        if liste[check_2] < liste[check_1]:
            temp = liste[check_2]
            liste.remove(liste[check_2])
            liste.insert(check_1, temp)
            check_1 = 0
            check_2 = 1
        else:
            check_1 += 1
            check_2 += 1 
    return liste
print(tri_insertion(l))

