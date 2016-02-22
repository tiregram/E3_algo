import random

from datetime import datetime

from fusion_sort import fusion_sort
from bubble_sort import bubble_sort
import exo1  as e

from matplotlib import pyplot as pl

def days_hours_minutes(td):
    return  td.microseconds


if __name__ == '__main__':
    val = 10
    inc = 10
    

    X_nb = []
    
    time_heap = []
    time_heap_i = []
    time_bubble = []
    time_fusion = []
    
    
    for a in range(1,5):

        copy1 = []
        h = e.Tas(100)
        h2 = e.Tas(100)
        
        for i in range(0,val):
            aaa = random.randint(0,val)
            copy1.append(aaa)
            h.insert(aaa)
            h2.insert(aaa)
        
        copy2 = copy1[:]

        X_nb.append(val)
       
        time = datetime.now()
        h2.heap_sort_s()
        time = datetime.now() - time
        time_heap_i.append(days_hours_minutes(time))        

        time = datetime.now()
        h.heap_sort()
        time = datetime.now() - time
        time_heap.append(days_hours_minutes(time))        

        time = datetime.now()
        bubble_sort(copy1)
        time = datetime.now() - time
        time_bubble.append(days_hours_minutes(time))
        
        time = datetime.now()
        fusion_sort(copy2)
        time = datetime.now() - time
        time_fusion.append(days_hours_minutes(time))

        val = val * inc;

    print(X_nb)
    print(time_heap)
    print(time_heap_i)
    print(time_fusion)
    print(time_bubble)
    
    pl.subplot(2,1,1)
    pl.plot(X_nb,time_heap   ,color='green', lw=1)
    pl.plot(X_nb,time_heap_i   ,color='orange', lw=1)
    pl.plot(X_nb,time_bubble ,color='blue', lw=1)
    pl.plot(X_nb,time_fusion ,color='red' , lw=1)
    
    pl.yscale('log')
    pl.xscale('log')
    pl.show()


