# @Author: jlumbroso
# @Date:   2018-03-28-01:21
# @Email:  lumbroso@cs.princeton.edu
# @Filename: graphics.py
# @Last modified by:   jlumbroso
# @Last modified time: 2018-03-28-01:22

import matplotlib as _plt
from matplotlib.lines import Line2D as _Lines2D

def plot_walk(walk, color='red', alpha=0.04):
    Xcur = 0
    Ycur = 0
    Xvec = []
    Yvec = []
    for i in range(len(walk)):
        step = walk[i]
        Xnex = Xcur + step.x
        Ynex = Ycur + step.y
        Xvec.append(Xcur)
        Yvec.append(Ycur)
        Xcur = Xnex
        Ycur = Ynex
    Xvec.reverse()
    Yvec.reverse()
    #line = Line2D(Xvec,Yvec)
    return _plt.plot(Xvec, Yvec, color=color, alpha=alpha)
