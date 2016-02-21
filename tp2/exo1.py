import re

class Exo1:
    def question_a(self,file_url):
        print (len(open(file_url).read()));

    def question_b(self,file_url):
        text = open(file_url).read()
        text = re.sub(',|;|/|-|_','',text)
        text = re.sub(' +[a-zA-Z]*1+ ',' ',text)
        text = re.sub('^[a-zA-Z]*1+ ','',text)
        text = re.sub(' +[a-zA-Z]*1$','',text)
        text = re.sub('^[a-zA-Z]*1$','',text)
       # print(text)
        return text
    
    def question_c(self,text ):
        text = re.sub('\n',' ',text)
        text = re.sub('\t',' ',text)
        words= text.split(' ');
        dico = dict()
        for  word in words :
            if word in dico: 
                dico[word] = dico[word ]+1
            else:
                dico[word]=1

        better = [[0,''],
                  [0,''],
                  [0,''],
                  [0,''],
                  [0,''],
                  [0,''],
                  [0,''],
                  [0,''],
                  [0,''],
                  [0,'']
        ]

        for a in dico:
            for b in better:
                if dico[a] > b[0]:
                    b[0]=dico[a]
                    b[1]=a
                    break
        
        return better


    def question_d(self,file_url ):

        f=open(file_url)
        text = f.read()
        f.close()
#        print(text)
        results = re.findall(" +[a-zA-Z.]+@+[a-zA-Z.]+ ",text)
        out = dict()
        for result in results:
            if result not in out:
                out[result] = 1;

        file_out = open("contactstp2.csv","w")
        for clef in out:
            print(clef)
            file_out.write(re.sub(' ','',clef)+";");

        file_out.close();
        
        
        
    
if __name__ == '__main__':
    a = Exo1()
    a.question_a("mbox_short.txt")
    text  = a.question_b("mbox_short.txt")
    print( a.question_c(text))
    a.question_d("mbox_short.txt")
    
    
