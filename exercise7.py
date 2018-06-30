from numpy import arange
import math
import matplotlib.pyplot as plot

def f(x):
    if scale == "C":
        return(source_temp * (9.0/5.0)) + 32.0

scale = "C"
source_temp = 40
xs = list(range(-5, 5))
ys = [] 

for x in xs: 
     ys.append(f(x)) 

plot.plot(xs, ys) 
plot.show()