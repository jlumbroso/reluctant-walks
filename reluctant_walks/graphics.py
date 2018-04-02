# @Author: jlumbroso
# @Date:   2018-03-28-01:21
# @Email:  lumbroso@cs.princeton.edu
# @Filename: graphics.py
# @Last modified by:   jlumbroso
# @Last modified time: 2018-04-02-17:39

import matplotlib.pyplot as _plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes as _inset_axes
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes as _zoomed_inset_axes

def plot_walk(walk, color='red', alpha=0.04, fig=None, ax=None, figsize=None, dpi=None):
    """
    """
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

    if fig == None and ax == None:
        if figsize == None and dpi == None:
            fig = _plt.figure()
        elif figsize != None:
            fig = _plt.figure(figsize=figsize)
        elif dpi != None:
            fig = _plt.figure(dpi=dpi)
        else:
            fig = _plt.figure(figsize=figsize, dpi=dpi)

        ax = fig.add_axes([0,0,1,1])

    elif ax == None:
        ax = fig.add_axes([0,0,1,1])

    ax.plot(Xvec, Yvec, color=color, alpha=alpha)

    return (fig, ax)

def plot_walk_region(walks, fig=None, ax=None, figsize=None, inset_stepset=None,
                     inset=True, inset_loc=4, inset_size=0.5, inset_hide_grid=False,
                     tight_quarterplane=False, borders=(None, None, None, None), **args):
    """
    """
    # NOTE: Import should not be moved to top-level or will create cyclic
    # dependency.
    from reluctant_walks.reference import is_quarter_plane as _is_quarter_plane

    unrestricted_walks = walks
    restricted_walks = filter(_is_quarter_plane, unrestricted_walks)

    for walk in unrestricted_walks:
        (fig, ax) = plot_walk(walk, color='grey', alpha=0.04, fig=fig, ax=ax, figsize=figsize, **args)

    for walk in restricted_walks:
        (fig, ax) = plot_walk(walk, color='green', alpha=0.8, fig=fig, ax=ax, figsize=figsize, **args)

    ax.axhline(0, color='black')
    ax.axvline(0, color='black')

    if borders == None or len(borders) < 4:
        borders = (None, None, None, None)

    if tight_quarterplane:
        borders = (-1, -1, borders[2], borders[3])

    if borders[0] != None:
        ax.set_xlim(left=borders[0])
    if borders[1] != None:
        ax.set_ylim(bottom=borders[1])
    if borders[2] != None:
        ax.set_xlim(right=borders[2])
    if borders[3] != None:
        ax.set_ylim(top=borders[3])

    if inset and inset_stepset != None:
        axins = _inset_axes(ax,
                            width=inset_size*1.,
                            height=inset_size*1.,
                            loc=inset_loc)
        plot_stepset(inset_stepset, ax=axins, hide_grid=inset_hide_grid)

    return (fig, ax)

def plot_stepset(stepset, hide_grid=False, color='red', alpha=1.0, dpi=80, ax=None):
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
        fig = _plt.figure(figsize=(1, 1), dpi=dpi)
        ax = fig.add_axes([0,0,1,1])

    if not hide_grid:
        ax.grid(True)
    else:
        ax.xaxis.set_ticks([])
        ax.yaxis.set_ticks([])
        #ax.axis('off')

    ax.xaxis.set_ticklabels([])
    ax.yaxis.set_ticklabels([])
    ax.tick_params(which='both', size=0.0)

    ax.set_aspect('equal', 'datalim')
    ax.plot(Xvec, Yvec, color=color, alpha=alpha)

    return ax

def plot_stepsets(stepsets, side=None, dpi=80, **args):
    import math

    if side == None:
        side = int(math.ceil(math.sqrt(len(stepsets))))

    N=side
    M=int(math.ceil(len(stepsets)/float(N)))

    fig, ax = _plt.subplots(M, N, dpi=dpi)

    for i in range(len(stepsets)):
        x = i % N
        y = (i - x) / N
        if N > 1 and M > 1:
            plot_stepset(stepset=stepsets[i],
                        ax=ax[y][x],
                        dpi=dpi,
                        **args)
        else:
            ax[x].set_aspect('equal', 'datalim')
            plot_stepset(stepset=stepsets[i],
                        ax=ax[x],
                        dpi=dpi,
                        **args)

    for i in range(len(stepsets),N*M):
        x = i % N
        y = (i - x) / N
        ax[y][x].axis('off')

    return fig
