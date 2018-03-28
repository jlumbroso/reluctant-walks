# -*- coding: latin-1 -*-

# @Date:   2018-03-21-21:26
# @Email:  lumbroso@cs.princeton.edu
# @Filename: reference.py
# @Last modified time: 2018-03-28-01:01

import copy as _copy

from reluctant_walks.plane import StepSet as _StepSet
from reluctant_walks.config import package_raise as _package_raise

# ==============================================================================

def make_step_set(set):
    obj = _StepSet()
    for (x,y) in set:
        obj.add_step(x,y)
    return obj

# ==============================================================================
# 79 NON-TRIVIAL STEPSETS
#
# Below are the 79 non-trivial models of quarter-plane walks using small steps
# (each step can move by 0 or 1 along either/both the x and y axes). These
# models are non-trivial (e.g.: a stepset that contains no negative steps can
# never exit the quarter-plane) and do not reduce to a half-plane model.
#
# These were inventoried in:
#
#    Bousquet-Mélou, Mireille, and Marni Mishna (2010).
#    "Walks with small steps in the quarter plane."
#    https://arxiv.org/abs/0810.4387
#
# This dictionary categorizes these models according to the number of steps in
# the stepset.

__nt_stepsets = {

    1 : [],

    2 : [],

    3 : [
            [(0, 1), (1, -1), (-1, -1)],
            [(1, 1), (0, -1), (-1, 0)],
            [(0, 1), (1, 0), (-1, -1)],
            [(0, 1), (1, -1), (-1, 0)],
            [(0, 1), (1, -1), (-1, 1)],
            [(1, 1), (1, -1), (-1, 0)],
            [(1, 1), (1, -1), (-1, 1)]
        ],

    4 : [
            [(0, 1), (1, 0), (0, -1), (-1, -1)],
            [(0, 1), (1, 0), (1, -1), (-1, -1)],
            [(0, 1), (1, 1), (1, 0), (-1, -1)],
            [(0, 1), (1, 1), (0, -1), (-1, 0)],
            [(0, 1), (1, 1), (1, -1), (-1, -1)],
            [(0, 1), (1, 0), (1, -1), (-1, 0)],
            [(0, 1), (1, 0), (0, -1), (-1, 0)],
            [(0, 1), (1, -1), (0, -1), (-1, 0)],
            [(0, 1), (1, -1), (0, -1), (-1, 1)],
            [(0, 1), (1, -1), (-1, -1), (-1, 0)],
            [(0, 1), (1, -1), (-1, -1), (-1, 1)],
            [(0, 1), (1, -1), (-1, 0), (-1, 1)],
            [(0, 1), (1, 0), (1, -1), (-1, 1)],
            [(0, 1), (1, -1), (0, -1), (-1, -1)],
            [(0, 1), (1, 1), (1, -1), (-1, 0)],
            [(0, 1), (1, 1), (1, -1), (-1, 1)],
            [(0, 1), (1, 1), (0, -1), (-1, 1)],
            [(0, 1), (1, 1), (0, -1), (-1, -1)],
            [(1, 1), (0, -1), (-1, -1), (-1, 0)],
            [(1, 1), (0, -1), (-1, -1), (-1, 1)],
            [(1, 1), (0, -1), (-1, 0), (-1, 1)],
            [(1, 1), (1, -1), (0, -1), (-1, 1)],
            [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        ],

    5 : [
            [(0, 1), (1, 1), (1, 0), (-1, -1), (-1, 1)],
            [(0, 1), (1, 1), (1, 0), (0, -1), (-1, 1)],
            [(0, 1), (1, 1), (1, 0), (1, -1), (-1, 1)],
            [(0, 1), (1, 0), (1, -1), (0, -1), (-1, 0)],
            [(0, 1), (1, 0), (1, -1), (-1, -1), (-1, 0)],
            [(0, 1), (1, 0), (0, -1), (-1, -1), (-1, 0)],
            [(0, 1), (1, 1), (1, 0), (-1, -1), (-1, 0)],
            [(0, 1), (1, 1), (0, -1), (-1, -1), (-1, 0)],
            [(0, 1), (1, 1), (0, -1), (-1, -1), (-1, 1)],
            [(0, 1), (1, 1), (0, -1), (-1, 0), (-1, 1)],
            [(0, 1), (1, 1), (1, -1), (0, -1), (-1, 0)],
            [(0, 1), (1, 1), (1, -1), (0, -1), (-1, 1)],
            [(0, 1), (1, 1), (1, -1), (-1, -1), (-1, 0)],
            [(0, 1), (1, 1), (1, -1), (-1, -1), (-1, 1)],
            [(0, 1), (1, 1), (1, -1), (-1, 0), (-1, 1)],
            [(0, 1), (1, 1), (1, -1), (0, -1), (-1, -1)],
            [(0, 1), (1, -1), (0, -1), (-1, -1), (-1, 0)],
            [(0, 1), (1, -1), (0, -1), (-1, -1), (-1, 1)],
            [(0, 1), (1, -1), (0, -1), (-1, 0), (-1, 1)],
            [(0, 1), (1, -1), (-1, -1), (-1, 0), (-1, 1)],
            [(0, 1), (1, 0), (1, -1), (0, -1), (-1, -1)],
            [(0, 1), (1, 1), (1, 0), (0, -1), (-1, 0)],
            [(0, 1), (1, 0), (1, -1), (0, -1), (-1, 1)],
            [(0, 1), (1, 0), (1, -1), (-1, -1), (-1, 1)],
            [(1, 1), (0, -1), (-1, -1), (-1, 0), (-1, 1)],
            [(1, 1), (1, -1), (0, -1), (-1, 0), (-1, 1)],
            [(1, 1), (1, -1), (-1, -1), (-1, 0), (-1, 1)]
        ],

    6 : [
            [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)],
            [(0, 1), (1, 1), (1, 0), (0, -1), (-1, -1), (-1, 0)],
            [(0, 1), (1, 1), (1, 0), (1, -1), (-1, -1), (-1, 0)],
            [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, 0)],
            [(0, 1), (1, 1), (1, 0), (1, -1), (-1, 0), (-1, 1)],
            [(0, 1), (1, 1), (1, 0), (1, -1), (-1, -1), (-1, 1)],
            [(0, 1), (1, 0), (0, -1), (-1, -1), (-1, 0), (-1, 1)],
            [(0, 1), (1, 0), (1, -1), (-1, -1), (-1, 0), (-1, 1)],
            [(0, 1), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)],
            [(0, 1), (1, 0), (1, -1), (0, -1), (-1, 0), (-1, 1)],
            [(0, 1), (1, 1), (0, -1), (-1, -1), (-1, 0), (-1, 1)],
            [(0, 1), (1, 1), (1, -1), (0, -1), (-1, -1), (-1, 0)],
            [(0, 1), (1, 1), (1, -1), (0, -1), (-1, 0), (-1, 1)],
            [(0, 1), (1, 1), (1, -1), (-1, -1), (-1, 0), (-1, 1)],
            [(0, 1), (1, 1), (1, -1), (0, -1), (-1, -1), (-1, 1)],
            [(1, 1), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
        ],

    7 : [
            [(0, 1), (1, 1), (1, 0), (0, -1), (-1, -1), (-1, 0), (-1, 1)],
            [(0, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)],
            [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, 0), (-1, 1)],
            [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 1)],
            [(0, 1), (1, 1), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
        ],

    8 : [
           [(0, 1), (1, 1), (1, 0), (1, -1),
                    (0, -1), (-1, -1), (-1, 0), (-1, 1)]
        ]
}

# The cached 'best slopes' for the 79 non-trivial quarter-plane walk models
# with small steps. These were precomputed for convenience, but can be fully
# regenerated with the method __compute_nt_stepsets_slope() below.

__nt_stepsets_slope_ratprecision = 10
__nt_stepsets_slope = {
    1: [],
    2: [],
    3: [0, 0, 0, 0, 0, 0, 0],
    4: [(0, 1), 0, 0, 0, 0, 0, 0, (1, 2), 0, (8, 7), (3, 1), 0, 0,
            0, 0, 0, 0, 0, 1, (0, 1), 0, 0, 0],
    5: [0, 0, 0, 0, 0, 1, 0, (0, 1), 0, 0, 0, 0, 0, 0, 0, 0, (7, 8),
            (3, 2), (2, 1), (19, 7), (0, 1), 0, 0, 0, (1, 0), 0, (1, 0)],
    6: [0, 0, 0, 0, 0, 0, (1, 0), (31, 9), (7, 4), 0, (1, 0), (0, 1),
            0, 0, 0, 1], # FIXME: double check that 1
    7: [0, 1, 0, 0, (0, 1)],
    8: [0]
}

# FIXME: This function is deprecated by the one below which essentially
# does the same thing (better, and in one pass).
def __compute_nt_stepsets_slope(rat_precision=10, force=False):
    """
    Recomputes the best slopes of the 79 non-trivial quarter-plane walk models
    with small steps.
    """
    global __nt_stepsets_slope

    if (not '__nt_stepsets_slope' in globals()) or force:

        def get_best_slope(x):
            try:
                return StepSet(x).get_best_slope(rat_precision=rat_precision)
            except KeyboardInterrupt:
                raise
            except:
                return None

        nt_stepsets_slope = {}
        for key in __nt_stepsets:
            nt_stepsets_slope[key] = map(get_best_slope,
                                         __nt_stepsets[key])
        __nt_stepsets_slope = nt_stepsets_slope
        __nt_stepsets_slope_ratprecision = rat_precision

__nt_stepsets_records = None

def __build_nt_stepsets_records():
    from reluctant_walks.plane import StepSet

    objs = []
    current_id = 0
    for key in __nt_stepsets:
        for i in range(len(__nt_stepsets[key])):
            walk_coord = (key, i)
            walk_id = current_id
            walk_steps = __nt_stepsets[key][i]
            walk_cached_bestslope = __nt_stepsets_slope[key][i]
            walk_obj = StepSet(
                init_set=walk_steps,
                cached_bestslope=walk_cached_bestslope,
                cached_bestslope_ratprecision= \
                    __nt_stepsets_slope_ratprecision)
            record = {
                'id': walk_id,
                'coord': walk_coord,
                'size': len(walk_steps),
                'steps': walk_steps,
                'stepset': walk_obj,
                'drift': walk_obj.drift,
                'best_slope': walk_cached_bestslope
            }
            objs.append(record)
            current_id += 1

    return objs

__nt_stepsets_records = __build_nt_stepsets_records()

# consts
POSSIBLE_NT_DRIFTS=set(map(lambda r: r['drift'], __nt_stepsets_records))
POSSIBLE_NT_SLOPES=set(filter(lambda x: x != None,
                           map(lambda r: r['best_slope'],
                               __nt_stepsets_records)))
POSSIBLE_NT_SIZES=set(map(lambda r: r['size'], __nt_stepsets_records))

def get_nontrivial_qw_model(by_drift=POSSIBLE_NT_DRIFTS,
                            by_best_slope=POSSIBLE_NT_SLOPES,
                            by_size=POSSIBLE_NT_SIZES):

    global __nt_stepsets_records

    if not "__nt_stepsets_records" in globals():
        __nt_stepsets_records = __build_nt_stepsets_records()

    def filter_function(record):
        if type(record) != dict:
            return False
        fields = record.keys()
        if "drift" in fields and not record['drift'] in by_drift:
            return False
        if "size" in fields and not record['size'] in by_size:
            return False
        if "best_slope" in fields and not record['best_slope'] in by_best_slope:
            return False
        # If we made it this far...
        return True

    return filter(filter_function, _copy.deepcopy(__nt_stepsets_records))

# ==============================================================================

def walk_exit_step(walk):
    """
    Determines the step at which a walk exits the upper quarterplane.
    """
    x, y = 0, 0
    i = 0
    for step in walk:
        x += step.x
        y += step.y
        i += 1
        if x < 0 or y < 0:
            return i
    return i

def is_quarter_plane(walk):
    """
    Determines whether a given walk exit the upper quarterplane.
    """
    return walk_exit_step(walk) == len(walk)


# ==============================================================================

def tabulate_endpoints_sparse(walks):
    """
    Compute the endpoint of each walk that is provided and return a dictionary
    that maps to each possible endpoint the number of walks (1 or more) that
    end in this endpoint. This implementation uses a Python `dict`.
    """
    endpoints = {}

    for walk in walks:
        x, y = 0, 0
        i = 0
        # FIXME: not dogfooding our own `is_quarter_plane` because we need
        # the endpoint; perhaps this means the method should be changed to
        # be more useful.
        quarter_plane = True
        for step in walk:
            x += step.x
            y += step.y
            i += 1
            if x < 0 or y < 0:
                quarter_plane = False
                break
        if quarter_plane:
            if not (x,y) in endpoints:
                endpoints[(x,y)] = 0
            endpoints[(x,y)] += 1

    return endpoints

def tabulate_endpoints_dense(walks, side=10):
    """
    Compute the endpoint of each walk that is provided and return a dictionary
    that maps to each possible endpoint the number of walks (1 or more) that
    end in this endpoint. This implementation uses a `numpy` array (and requires
    the `numpy` package).
    """
    try:
        import numpy as np
    except ImportError:
        _package_raise("numpy")

    endpoints = np.array([[0]*side]*side)
    for walk in walks:
        x, y = 0, 0
        i = 0
        # FIXME: same remark as above.
        quarter_plane = True
        for step in walk:
            x += step.x
            y += step.y
            i += 1
            if x < 0 or y < 0:
                quarter_plane = False
                break
        if quarter_plane:
            if x < side and y < side:
                endpoints[x,y] += 1

    return endpoints

# ==============================================================================

def _push_steps(tab, stepset, x, y, val=0):
    for s in stepset:
        nx = x + s.x
        ny = y + s.y
        if (nx >= 0 and nx < len(tab) and
                ny >= 0 and ny < len(tab[0])):
            tab[nx,ny] += val

def tabulate_all_walks(stepset, side=10, N=10):
    """
    Tabulates all possible walks of size `N`. This implementation uses
    a `numpy` array (and requires the `numpy` package).
    """
    try:
        import numpy as np
    except ImportError:
        _package_raise("numpy")
    import numpy as np

    blank = np.array([[0]*side]*side)

    curr = blank.copy()
    curr[0,0] = 1

    for step in range(N):
        prev = curr
        curr = blank.copy()
        for i in range(min(step+1, side)):
            for j in range(min(step+1, side)):
                _push_steps(curr, stepset, i, j, prev[i,j])

    return curr

def print_matrix(mat, prec=2):
    fstring = "%%6.0%df" % prec
    for i in range(len(mat)):
        s = ""
        for j in range(len(mat[0])):
            s += (fstring % mat[len(mat[0])-i-1,j])
        print(s)

# ==============================================================================

# FIXME: x- and y-axis interverted

def tabulate_halfplane_walks(steps, N=10, meanders=True):

    if meanders:
        tab = {(h,0):1 for h in range(0, 1+max(steps)*N)}
    else:
        tab = {(0,0):1}

    for i in range(1,N+1):
        for h in range(0,1+max(steps)*(N)):
            acc = 0
            for s in steps:
                if (h+s,i-1) in tab:
                    acc += tab[(h+s,i-1)]
            tab[(h,i)] = acc

    return tab

# ==============================================================================
############## Random generation Rec. (Yann) ###############
import random as _random

def in_quarter_plane(x,y):
    return (x>=0) and (y>=0)

def end_anywhere_quarterplane(x,y):
    return quarterplane(x,y)

def naive_random_generation_precompute(steps, length,
                                       test_function=in_quarter_plane,
                                       end_position=end_anywhere_quarterplane):
    """
    """
    max_north = max([s.y for s in steps])
    max_south = min([s.y for s in steps])
    max_east = max([s.x for s in steps])
    max_west = min([s.x for s in steps])
    tab = {
        (x, y, 0) : 1
                for x in range(max_west*length,1+max_east*length)
                for y in range(max_south*length,1+max_north*length)
                if test_function(x,y) and end_position(x,y)
                }

    for i in range(1, length+1):
        for x in range(max_west*length, 1+max_east*length):
            for y in range(max_south*length, 1+max_north*length):
                acc = 0
                if test_function(x, y):
                    for s in steps:
                        (nx,ny) = (x+s.x,y+s.y)
                        if test_function(nx,ny) and (nx,ny,i-1) in tab:
                            acc += tab[(nx,ny,i-1)]
                    tab[(x,y,i)] = acc
    return tab

def naive_random_generation(steps,length,num_walks,
                            test_function=in_quarter_plane,
                            end_position=end_anywhere_quarterplane):
    walks = []
    tab = naive_random_generation_precompute(steps,length,test_function,end_position)
    for w in range(num_walks):
        x,y = 0,0
        curr_walk = []
        for i in range(length,0,-1):
            r = _random.random() * tab[(x,y,i)]
            found = False
            for s in steps:
                if not found:
                    (nx,ny) = (x+s.x,y+s.y)
                    if test_function(nx,ny) and (nx,ny,i-1) in tab:
                        r -= tab[(nx,ny,i-1)]
                        if r<0:
                            curr_walk.append(s)
                            found = True
                            x,y = nx,ny
        walks.append(curr_walk)
    return walks

# ==============================================================================
