import re

class Exo1:
    def question_a(self,file_url):
        print (len(open(file_url).read()));

    def question_b(self,file_url):
        file_to_read = open(file_url)
        text = file_to_read.read()
        file_to_read.close();

        text = re.sub('[0-9]*','',text)
        text = re.sub(',|;|/|-|:|\.|\)','',text)
        text = re.sub('\[|\]','',text)
        text = re.sub(' +[a-zA-Z]*1+ ','',text)
        text = re.sub('^[a-zA-Z]*1+ ','',text)
        text = re.sub(' +[a-zA-Z]*1$','',text)
        text = re.sub('^[a-zA-Z]*1$','',text)
        
        text = re.sub('\n',' ',text)
        text = re.sub('\t',' ',text)        
        return text
    
    def question_c(self,text):



                
        words= text.split(' ');
        dico = dict()
        for  word in words :
            if word not in dico: 
                dico[word] = 0
            dico[word] = dico[word]+1

        
        dico[''] = 0;
        

        import operator
        better = sorted(dico.items(),
                        key=operator.itemgetter(1),
                        reverse=True)[0:10]
        return better



    def question_d(self,file_url,adi):

        f=open(file_url)
        text = f.read()
        f.close()
#        print(text)
        results = re.findall(" +[a-zA-Z.0-9]+@+[a-zA-Z.]+ ",text)
        out = dict()
        for result in results:
            if result not in out:
                out[result] = 1;

        file_out = open("contactstp2"+adi+".csv","w")
        for clef in out:
            print(clef)
            file_out.write(re.sub(' ','',clef)+";");

        file_out.close();
        
        
        
    
if __name__ == '__main__':
    a = Exo1()
    a.question_a("mbox_short.txt")
    text  = a.question_b("mbox_short.txt")


    text = a.question_c(text)
    print(text)


    a.question_d("mbox_short.txt","short")
    a.question_d("mbox.txt","")
    
