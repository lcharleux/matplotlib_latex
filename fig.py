# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------
# FIGURE CONFIGURATION
import matplotlib as mpl
from rcparams import RCPARAMS
mpl.use("pgf")
mpl.rcParams.update(RCPARAMS)
width = 6.69        # fig width in inches
heigth = width /2.5 # fig heigth in inches
#-------------------------------------------------------------------------------


import matplotlib.pyplot as plt
import numpy as np 
x = np.linspace(0., 10., 1000)   
y1 = np.sin(np.pi/2. * x**2) * x**1.3
y2 = np.cos(np.pi * x /5.) * y1


fig = plt.figure(figsize = (width, heigth))
plt.plot(x, y1, "r-",label = r"$y_1$")
plt.plot(x, y2, "b-", label = r"$y_2$")
plt.fill_between(x, y1, y2, where = y1 >= y2, 
                 label = "$y_1 \geq y_2$", 
                 alpha = .5, 
                 facecolor = "magenta")
plt.fill_between(x, y1, y2, where = y1 < y2, 
                 label = "$y_1 < y_2$", 
                 alpha = .5, 
                 facecolor = "green")
plt.grid()
plt.xlim(0., 10.)
plt.legend(loc = "best")
plt.xlabel("Time, $t$")
plt.ylabel("Amplitude, $y(t)$")
plt.title(r"Some useless maths: $\zeta = \kappa$")
plt.tight_layout() 
plt.savefig("fig.pdf", bbox_inches='tight')
