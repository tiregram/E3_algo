
def tri_fusion(liste):

    taille =len(liste)

    #si la taille est de 0 ou supérieur a 1 alors le sous tableaux est trier
    if taille == 0 or taille == 1 :
        return liste
    else:
        return fusion(tri_fusion(liste[0:taille//2]),tri_fusion(liste[taille//2:taille]))

def fusion(liste1,liste2):
    # si la liste 1 est vide on retourne liste 2
    if liste1==[]:
        return liste2
    elif liste2==[]: # inversement 
        return liste1
    else: # on refusione la liste en insérant  un element de la liste2
        return fusion(liste1[1:len(liste1)],insere(liste1[0],liste2))

def insere(x,liste):
    if liste==[]:
        return [x]
    elif x<=liste[0]: 
        return [x] + liste
    else:# si la liste est sup on recomence avec les element suivant de la liste
        return [liste[0]] + insere(x,liste[1:len(liste)])

