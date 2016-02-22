
def fusion_sort(liste):

    taille =len(liste)

    #si la taille est de 0 ou supérieur a 1 alors le sous tableaux est trier
    if taille == 0 or taille == 1 :
        return liste
    else:
        return fusion(fusion_sort(liste[0:taille//2]),fusion_sort(liste[taille//2:taille]))

def fusion(liste1,liste2):
    l = []
    
    if liste1 == None or len(liste1)==0:
        return liste2
    
    if liste2 == None or len(liste2)==0:
        return liste1

    a = liste1.pop(0)
    b = liste2.pop(0)
    
    while True:
        if b < a:
            l.append(b)
            if len(liste2) == 0:
                l = l + [a] +liste1
                break;
            else:
                b = liste2.pop(0)
        else:
            l.append(a)
            if len(liste1) == 0:
                l = l + [b] + liste2
                break;
            else:
                a = liste1.pop(0)


    return l

import random

if __name__ == '__main__':
    # creation du tableau
    element_non_order =[]
    for i in range(0,10000):
        element_non_order.append(random.randint(0,10000))



    element_order = fusion_sort(element_non_order)
    
    print(element_order)
