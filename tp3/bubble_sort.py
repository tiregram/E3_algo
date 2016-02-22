


def bubble_sort(element_to_order):
    # on recup la taille
    taille = len(element_to_order)

    # on met la valeur par default
    is_over = False
    
    while is_over == False:
        # mise a False si il n'y a pas de changement alors exit
        is_over = True

        # compare les element cote a cote avec la fonction > 
        for i in range(0, taille-1):
            if element_to_order[i] > element_to_order[i+1]:
                is_over = False
                # python swap  /!\ xor can be do
                element_to_order[i],element_to_order[i+1] = element_to_order[i+1],element_to_order[i]
                
    return element_to_order


import random

if __name__ == '__main__':
    # creation du tableau
    element_non_order =[]
    for i in range(0,1000):
        element_non_order.append(random.randint(0,10000))

    #test trie
    element_order = bubble_sort(element_non_order)
    
