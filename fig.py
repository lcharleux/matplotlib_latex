# -*- coding: utf-8 -*-

import matplotlib as mpl
mpl.use("pgf")
params = {
  "pgf.texsystem": "xelatex",
  "font.family": "serif", # use serif/main font for text elements
  "text.usetex": True,    # use inline math for ticks
  "pgf.rcfonts": False,   # don't setup fonts from rc parameters
  "pgf.preamble": [
       r"\usepackage{fontspec}",
       r"\usepackage{amsmath}",
       r"\setmainfont{XCharter}", # Charter BT
       ],
  "font.size"       : 10,
  "xtick.labelsize" : 10,
  "ytick.labelsize" : 10,
  "axes.labelsize"  : 10,
  "axes.titlesize"  : "large",  # fontsize of the axes title
  "axes.labelsize"  : "medium",  # fontsize of the x any y labels
  "axes.labelpad"   : 4.0,     # space between label and axis
  "axes.labelweight": "normal",  # weight of the x and y labels
  "axes.labelcolor" : "black",

  }
mpl.rcParams.update(params)

import matplotlib.pyplot as plt
import numpy as np 

def fonction(x, tau, omega):
  """
  Une fonction à tracer.
  
  fonction(1,2,3) =  0.051915149703173388

  """
  return np.exp(-x / tau)*np.sin(omega * x)
  
# Tracé de la fonction
x = np.linspace(0., 10., 1000)   
y1 = fonction(x, tau = 10., omega = .5* np.pi)
y2 = fonction(x, tau = 3., omega = 2.* np.pi)

width = 6.69 # Largeur de la figure
heigth = width /2.5 # Hauteur de la figure

fig = plt.figure(figsize = (width, heigth))
plt.plot(x, y1, "r-",label = r"$\tau = 10, \omega = \pi/2 $")
plt.plot(x, y2, "b-", label = r"$\tau = 3, \omega = 2\pi $")
plt.fill_between(x, y1, y2, where = y1 >= y2, label = "$y_1 \geq y_2$", alpha = .5, facecolor = "magenta")
plt.fill_between(x, y1, y2, where = y1 < y2, label = "$y_1 < y_2$", alpha = .5, facecolor = "green")
plt.grid()
plt.legend(loc = "best")
plt.xlabel("Temps, $t$")
plt.ylabel("Amplitude, $y(t)$")
plt.title(r"Oscillateur amorti: $y(t) = \exp(-t/\tau)\sin(\omega t)$")
plt.tight_layout() 
plt.savefig("fig.pdf", bbox_inches='tight')
