import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import fifo
import random
import exo1
import time

class grap_time:
    
    def get_the_time_function(func,data):
        start_time = time.time()
        func(**data)
        return time.time() - start_time

    def get_data(value_min,value_max,quantity):
        elem = fifo.Deque(1)
        for a in range(0,quantity):
            elem.push_last(random.randint(value_min,value_max))
        return elem
        
    def data_gen(t=0):
        cnt = 1
        while cnt < 4000:
            data = dict()
            cnt += 1000
            data["elemToTry"] = grap_time.get_data(0,100000,cnt)
            print(cnt)
            yield cnt , grap_time.get_the_time_function(exo1.insertion_sort,data) 
            
            
    def init():
        ax.set_ylim(0, 10)
        ax.set_xlim(90, 1000)
        
        del xdata[:]
        del ydata[:]

        line.set_data(xdata,
                      ydata)
        return line,



    def run(data):
        # update the data
        t, y = data
        xdata.append(t)
        ydata.append(y)
        xmin, xmax = ax.get_xlim()
        
        if t >= xmax:
            ax.set_xlim(xmin, 2*xmax)
            ax.figure.canvas.draw()
            line.set_data(xdata,ydata)
            
        return line,

    
fig, ax = plt.subplots()
xdata, ydata = [], []
line, = ax.plot([], [], lw=2)

def draw():
    
    ax.grid()
    
    ani = animation.FuncAnimation(
        fig,
        grap_time.run,
        grap_time.data_gen,
        blit=False,
        interval=1,
        repeat=False,
        init_func=grap_time.init)
        
    plt.show()
    

draw();
