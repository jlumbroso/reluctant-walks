# -*- coding: latin-1 -*-

# @Date:   2018-03-21-21:26
# @Email:  lumbroso@cs.princeton.edu
# @Filename: reference.py
# @Last modified time: 2018-03-23-13:41

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
            0, 0, 0, None],
    7: [0, 1, 0, 0, (0, 1)],
    8: [0]
}

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

nt_stepsets_records = __build_nt_stepsets_records()
#def get_nontrivial_qw_model(by_drift=)
# ==============================================================================
