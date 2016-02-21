class Deque:
    """ cette class implémante le concepete de liste chainé
    """
    first = None # first element de la liste
    last = None  # last element de la liste
    
    def __init__(self, firstElement = 0):
        "Ce constructeur crée une liste doublement chainé avec comme premier element firstElement ou 0"
        self.last = self.first = Contener()
        self.last.value = firstElement
                

    ### function pour metre un element au debut    
    def push_first(self,elem ):
        n = Contener()
        n.value = elem
        n.next = self.first
        self.first.prev = n
        self.first = n

    ### function pour metre un element a la fin
    def push_last(self,elem ):
        n = Contener()
        n.value = elem
        n.prev = self.last
        self.last.next = n
        self.last = n

    ### eléve un element au debut
    def pop_first():
        n = self.first
        self.first = self.first.next
        self.first.prev = None
        return n.value


    ### eleve un element a la fin
    def pop_last():
        n = self.last
        self.last = self.last.prev
        self.last.next = None
        return n.value
    
    ### check si les element sont egaux
    def is_palindrome(self, ):
        come_to_first = self.first
        come_to_last = self.last

        while(come_to_first != come_to_last):
            if come_to_last.value != come_to_first.value:
                return False
            come_to_last = come_to_last.prev
            come_to_last = come_to_first.next
            
        return True

    #rajoute tout les element d'un itérable. aussi bien les string que les liste python, dico , string....
    def addString(self,string_to_add ):
        for a in string_to_add:
            self.push_last(a)


    
    def __str__(self):
        str_to_return=''
        cur = self.first
        while cur != None:
            str_to_return += str(cur.value) + " <=> "
            cur = cur.next
        return str_to_return

    def remove(self,rmv_me):
        cur = self.first
        while cur != None:
            if cur.value == rmv_me:
                cur.prev.next = cur.next
                if cur.next != None:
                    cur.next.prev = cur.prev
            cur = cur.next

    # cette function aplique un lambda sur tout les elements
    def aply_a_lambda(self, lamb):
        cur = self.first
        while cur != None:
            cur.value = lamb(cur.value)
            cur = cur.next

    # ceci est un contener pour stoquer les element il ne doit pas etre disponible pour l'exterieur
class Contener:
    next = None
    prev = None
    value = None
    
if __name__ == '__main__':
    a = Deque('a')
    print(a.is_palindrome())
    a.addString(" baHH non")
    a.remove(" ")
    a.aply_a_lambda(lambda v : v.lower())
    print(a)





        


