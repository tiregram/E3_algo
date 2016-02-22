import math

class Tas:
    tab = []
    
    def __init__(self,first_element):
        "docstring"
        self.tab = []
        self.tab.append(first_element)

    def has_children(self,indice ):
        return self.has_children_right(indice) and self.has_children_left(indice)

    def has_children_right(self, indice):
        return 2 * indice + 1 < len( self.tab )  
        
    def has_children_left(self, indice):
        return 2 * indice + 2 < len( self.tab )
    
    def get_children_right_value(self,indice):
        return self.tab[self.get_children_right_indice(indice)] if self.has_children_right(indice) else None

    def get_children_left_value(self,indice):
        return self.tab[self.get_children_left_indice(indice)] if self.has_children_left(indice) else None

    def get_children_left_indice(self,indice):
        return 2*indice+1  
        
    def get_children_right_indice(self,indice):
        return 2*indice+2
        
    def get_children(self,indice):
        return (get_children_left(indice),get_children_right(indice))

    def down_heat(self,indice):
        # check des valeur de base pour evité les sortie de tableau
        if(not self.has_children(indice)):
            if self.has_children_left(indice):
                if self.get_children_left_value(indice) < self.get_value(indice):
                       
                    self.swap(indice , self.get_children_left_indice(indice))
                    
                else :
                    
                    return
            else:
                return


        value = self.get_value(indice)
        cr = self.get_children_right_value(indice)
        cl = self.get_children_left_value(indice)

        
        if( cr  <  value and cl < value ):
            return;

        if( cr < cl ):
            self.swap( indice , self.get_children_left_indice(indice))
            self.down_heat(self.get_children_left_indice(indice))
        else:
            self.swap( indice , self.get_children_right_indice(indice))
            self.down_heat(self.get_children_right_indice(indice))

        return



    def up_heat(self,indice):
        if(indice == 0 ):
            return

        if(self.get_parent_value(indice) < self.get_value(indice)):
            self.swap(indice,self.get_parent_indice(indice))
            self.up_heat(self.get_parent_indice(indice))
        else:
            return
        

    def get_parent_indice(self, indice):
        return (indice-1) // 2
            
        
        
    def get_parent_value(self, indice):
        return self.tab[self.get_parent_indice(indice)]
        
            
    def swap(self,indice_one ,indice_two ):
        # TODO: use the xor implementation to switch
        valswitch = self.get_value(indice_one)
        self.tab[indice_one] = self.get_value(indice_two)
        self.tab[indice_two] = valswitch;
        
        
            
    def get_value(self,indice ):
        return self.tab[indice] if len(self.tab)>  indice else None
    
    def get_level_at_this_indice(self, indice):
        return 0 # TODO: return the 

    def get_level_to_the_panel(self):
        return 0

    def insert(self,value):
        self.tab.append(value)
        self.up_heat(len(self.tab)-1)

    def delete(self,indice):
        ret = self.tab[indice]
        self.tab[indice] = self.tab.pop()
        self.down_heat(indice)
        return ret

    def __str__(self):
        return self.str_rec(0);
        
    def str_rec(self,indice,mess=""):
        #ret ="\t" * (math.floor(math.log(indice + 1 ,2)))+"\---->" +
#        deca = math.floor(math.log(indice + 1,2))
 #       textDecalage = "    " * deca  +"\-->"
        
        ret  = mess+ ("C:" if (indice == 0) else ("\->D:" if ((indice % 2) == 0 ) else "-->G:"))
        ret += str(self.get_value(indice))
        ret += "\n"
        
        ret += (self.str_rec(self.get_children_left_indice(indice),mess + "   |" )  if self.has_children_left(indice)  else "")
        ret += (self.str_rec(self.get_children_right_indice(indice), mess + "    ") if self.has_children_right(indice) else "")    
        return ret


#    def heap_sort():
        

    
if __name__ == '__main__':
    # test simple
    h = Tas(5)
    import random
    [h.insert(random.randint(0,1000)) for a in range(0,1000)]
    print(h)
    

    l=[]


   
    for a in range(0,len(h.tab)):
        h.swap(0,len(h.tab)-1)
        l.append(h.tab.pop())
        h.down_heat(0);
   
    print(l)

    

