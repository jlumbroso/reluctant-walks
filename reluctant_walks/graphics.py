# @Author: jlumbroso
# @Date:   2018-03-28-01:21
# @Email:  lumbroso@cs.princeton.edu
# @Filename: graphics.py
# @Last modified by:   jlumbroso
# @Last modified time: 2018-03-29-20:48

import matplotlib as _plt
#from matplotlib.lines import Line2D as _Lines2D

def plot_walk(walk, color='red', alpha=0.04):
    # FIXME: make this function take and return an axis
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

def plot_stepset(stepset, color='red', alpha=1.0, dpi=80, ax=None):
    Xvec = []
    Yvec = []
    for step in stepset:
        Xvec.append(0)
        Yvec.append(0)
        Xvec.append(step.x)
        Yvec.append(step.y)
    Xvec.append(0)
    Yvec.append(0)

    Xvec.reverse()
    Yvec.reverse()

    if ax == None:
        fig = plt.figure(figsize=(1, 1), dpi=dpi)
        ax = fig.add_axes([0,0,1,1])

    ax.grid(True)
    ax.xaxis.set_ticklabels([])
    ax.yaxis.set_ticklabels([])
    ax.set_aspect('equal', 'datalim')
    ax.plot(Xvec, Yvec, color=color, alpha=alpha)

    return ax

def plot_stepsets(stepsets, side=None, **args):
    import math

    if side == None:
        side = int(math.ceil(math.sqrt(len(stepsets))))

    N=side
    M=int(math.ceil(len(stepsets)/float(N)))

    fig, ax = plt.subplots(M, N, dpi=40)

    for i in range(len(stepsets)):
        x = i % N
        y = (i - x) / N
        plot_stepset(stepset=stepsets[i],
                     ax=ax[y][x],
                     **args)

    for i in range(len(stepsets),N*M):
        x = i % N
        y = (i - x) / N
        ax[y][x].axis('off')

    return fig
