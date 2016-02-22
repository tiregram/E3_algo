import random
from datetime import datetime
from fusion_sort import fusion_sort
from bubble_sort import bubble_sort
from matplotlib import pyplot as pl


def days_hours_minutes(td):
    return  td.microseconds


if __name__ == '__main__':
    val = 10
    inc = 10
    
    X_nb = []
    time_bubble = []
    time_fusion = []
    
    
    for a in range(1,6):
        copy1 = []

        for i in range(0,val):
            copy1.append(random.randint(0,val))
            
        
        copy2 = copy1[:]

        X_nb.append(val)
        
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
    print(time_fusion)
    print(time_bubble)
    
    pl.subplot(2,1,1)
    pl.plot(X_nb,time_bubble ,color='blue', lw=1)
    pl.plot(X_nb,time_fusion ,color='red' , lw=1)
    
    pl.yscale('log')
    pl.xscale('log')
    pl.show()


