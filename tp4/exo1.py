import fifo
import random
import time


def insertion_sort(elemToTry):

    tab = []


    for a in elemToTry:
        tab.append(a);
        
        place(tab , len(tab)-1)

    return tab
        
    
def invertPlace(tableau,indiceOne,indiceTwo):
    tableau[indiceTwo], tableau[indiceOne] = tableau[indiceOne],tableau[indiceTwo]


def place(tableau,indice):


    while tableau[indice] < tableau[indice-1]:
        if(indice-1 < 0 ):
            return

        invertPlace(tableau,indice-1,indice)
        indice = indice - 1
    
    
    
    
#############################################################

def bucketSort(table, index =  lambda a : a>>6):

    tab = [None]

    for a in table:
        

        
        if len(tab)-1 < index(a):

            tab = tab + [None] * (index(a) - len(tab)+1)
            

            
        if tab[index(a)] ==  None:
            tab[index(a)] = fifo.Deque(a)
        else:
            tab[index(a)].push_last(a)
        
    tabret = []
    for a in tab:
        tabret = tabret + insertion_sort(a)

    return tabret

