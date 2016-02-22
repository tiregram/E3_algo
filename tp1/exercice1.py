
#
class Fraction:
    nume = 0
    deno = 0
   

    def __init__(self, n,d):
        self.demo = d
        self.nume = n
        
    
    def PGCD(self ):
        
      a,b = (self.demo,self.nume) if self.demo > self.nume else (self.nume, self.demo)
     
      reste = 1

      while(True):
          reste = a%b;
          if(reste != 0):
              a = b
              b = reste
              continue;
          else:
              return b

    def PGCDrecursif(self):
        a,b = (self.demo,self.nume) if self.demo > self.nume else (self.nume, self.demo)
        reste = 1

        reste = a % b 

        if(reste == 0):
            return b
        else:
            return Fraction(b,reste).PGCDrecursif();
        
    def addition(self,frac):
        return Fraction(self.num * frac.demo + frac.num * self.demo,
                        self.demo*frac.demo)
        
    def soustraction(self,frac):
        return Fraction(self.num * frac.demo - frac.num * self.demo,
                        self.demo*frac.demo)

    def multiplication(self,frac):
        return Fraction(self.num * frac.num,
                        self.demo * frac.demo)
    def divition(self,frac):
        return self * Fraction(frac.deno,frac.nume)

    def reduce(self):
        pgcd =self.PGCD()
        self.demo /= pgcd
        self.nume /= pgcd

    def __str__(self):
        self.reduce()
        return str(self.nume) + "/" + str(self.demo);
            

    
if __name__ == '__main__':
    f1 = Fraction(100,85)
    print(f1.PGCD())
    print(f1.PGCDrecursif())
    f1.reduce()
    print(f1)
    
    f2 = Fraction(18,3) 
    print(f2.PGCD())
    print(f2.PGCDrecursif())
    f2.reduce()
    print(f2)
    

    f3 = Fraction(19231300,4324250) 
    print(f3.PGCD())
    print(f3.PGCDrecursif())
    f3.reduce()
    print(f3)
    
