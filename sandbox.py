# @Date:     2018-03-21-21:21
# @Email:    lumbroso@cs.princeton.edu
# @Filename: sandbox.py
# @Last modified time: 2018-03-21-22:27


try:
    # Python 3
    from functools import reduce
except ImportError:
    pass

##############################
## 79 NON-TRIVIAL STEP SETS ##
##############################


nt_stepsets = {
    1 : [],

    2 : [],

    3 : [ [(0, 1), (1, -1), (-1, -1)],
                [(1, 1), (0, -1), (-1, 0)],
                [(0, 1), (1, 0), (-1, -1)],
                [(0, 1), (1, -1), (-1, 0)],
                [(0, 1), (1, -1), (-1, 1)],
                [(1, 1), (1, -1), (-1, 0)],
                [(1, 1), (1, -1), (-1, 1)]    ],

    4 : [ [(0, 1), (1, 0), (0, -1), (-1, -1)],
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
                [(1, 1), (1, -1), (-1, -1), (-1, 1)] ],

    5 : [ [(0, 1), (1, 1), (1, 0), (-1, -1), (-1, 1)],
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
                [(1, 1), (1, -1), (-1, -1), (-1, 0), (-1, 1)] ],

    6 : [ [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)],
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
                [(1, 1), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]],

    7 : [ [(0, 1), (1, 1), (1, 0), (0, -1), (-1, -1), (-1, 0), (-1, 1)],
                [(0, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)],
                [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, 0), (-1, 1)],
                [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 1)],
                [(0, 1), (1, 1), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)] ],

    8 : [[(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]]

}

nt_stepsets_slope = {
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

if not ('nt_stepsets_slope' in vars() or 'nt_stepsets_slope' in globals()):
    def get_best_slope(x):
        try:
            return StepSet(x).get_best_slope()
        except KeyboardInterrupt:
            raise
        except:
            return None
    nt_stepsets_slope = {}
    for key in nt_stepsets:
        nt_stepsets_slope[key] = map(get_best_slope, nt_stepsets[key])





step_set1 = [ (-1,0), (1,1), (1,-1) ]
step_set2 = [ (0,1), (-1,-1), (0,-1), (1,-1) ]



def is_quarter_plane(walk):
    x, y = 0, 0
    i = 0
    for step in walk:
        x += step.x
        y += step.y
        i += 1
        if x < 0 or y < 0:
            return i
    return i

def make_step_set(set):
    obj = StepSet()
    for (x,y) in set:
        obj.add_step(x,y)
    return obj

def how_many_until_quarter(stepset, size):
    n = 0
    walk = []
    while n < 100:
        walk = random_generate(stepset, size)
        n += 1
        if is_quarter_plane(walk):
            break
    return (n, walk)


def flattendict(d):
    l = []
    for i in d:
        l += d[i]
    return l


#walksteptest1 = make_step_set([(-1,0), (1,1), (1,-1)])
#how_many_until_quarter(walksteptest1, 100) # returns something like 3
#how_many_until_quarter(walksteptest1, 1000) # returns something like 6


def drift(step_set):
    return reduce(lambda x,y: x+y, map(lambda (x,y): x+y, step_set))

def tdrift(step_set):
    return sum(step_set)


def negdrift(sset):
    return filter(lambda x: drift(x) < 0, sset)

def testslopes():
    ntl = flattendict(nt_stepsets)
    for i in ntl:
        print i
        print StepSet(i).get_best_slope()

def tt():
        x, y = var("x y", domain = "real")
        step_set = step_set1
        # p: inventory polynomial
        p = sum(map(lambda (a,b):x**a*y**b, step_set))
        ks_zero = (
            p(x=1).coefficient(y**(0)) +
            2*sqrt(p(x=1).coefficient(y**(-1)) * p(x=1).coefficient(y**(-1))))
        ks_max = (
            p(y=1).coefficient(x**(0)) +
            2*sqrt(p(y=1).coefficient(x**(-1)) * p(y=1).coefficient(x**(-1))))
        return (ks_zero, ks_max)

def gen():
    ssl3 = [(0, 1), (1, 0), (1, -1), (-1, -1), (-1, 0), (-1, 1)]
    ss3 = StepSet(ssl3)
    grgsw_no_slope = GenRGenSWalkCompiler(ss3)
    grgsw_no_slope.generate(100, 100)
    ss3.slope = ss3.get_best_slope()
    grgsw_with_slope = GenRGenSWalkCompiler(ss3)
    grgsw_with_slope.generate(100, 100)
    return (grgsw_no_slope, grgsw_with_slope)

def draw_walk(walk):
    import turtle
    turtle.reset()
    turtle.speed("fastest")
    turtle.pu()
    turtle.setpos(-300, -300)
    turtle.pd()
    turtle.pencolor(1.0, 0.0, 0.0)
    turtle.forward(1000)
    turtle.setpos(-300, -300)
    turtle.left(90)
    turtle.forward(1000)
    turtle.setpos(-300, -300)
    turtle.pencolor(0.0, 0.0, 0.0)
    for step in walk:
        turtle.goto(turtle.xcor() + 10*step.x,turtle.ycor() + 10*step.y)

def draw_walks(walks):
    for walk in walks:
        print is_quarter_plane(walk)
        draw_walk(walk)
        sleep(1)

def gen2():
    s4 = StepSet([(0, 1), (1, 1), (0, -1), (-1, -1), (-1, 0), (-1, 1)])
    s4.slope = (-1, 0)
    return GenRGenSWalkCompiler(s4).generate(100,100)

def gen3():
    s4 = StepSet([(0, 1), (1, 1), (0, -1), (-1, -1), (-1, 0), (-1, 1)])
    s4.slope = (0, 1)
    return GenRGenSWalkCompiler(s4).generate(100,100)

def gen4():
    s4 = StepSet([(0, 1), (1, 1), (0, -1), (-1, -1), (-1, 0), (-1, 1)])
    s4.slope = (-1, 0)
    return GenRGenSWalkCompiler(s4).generate(100000,10)

def sum_pairs(p1, p2):
    return (p1[0] + p2[0], p1[1] + p2[1])


def tabulate_endpoints(walks):
    endpoints = {}
    for walk in walks:
        x, y = 0, 0
        i = 0
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

def tabulate_endpoints2(walks, side=10):
    endpoints = np.array([[0]*side]*side)
    for walk in walks:
        x, y = 0, 0
        i = 0
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

############## Random generation Rec. (Yann) ###############
import random
def quarterplane(x,y):
    return (x>=0) and (y>=0)

def end_anywhere_quarterplane(x,y):
    return quarterplane(x,y)

def precompute_naive_random_generation(steps,length,test_function = quarterplane, end_position = end_anywhere_quarterplane):
    max_north = max([s.y for s in steps])
    max_south = min([s.y for s in steps])
    max_east = max([s.x for s in steps])
    max_west = min([s.x for s in steps])
    tab = {(x,y,0):1 for x in range(max_west*length,1+max_east*length) for y in range(max_south*length,1+max_north*length) if test_function(x,y) and end_position(x,y)}

    for i in range(1,length+1):
        for x in range(max_west*length,1+max_east*length):
            for y in range(max_south*length,1+max_north*length):
                acc = 0
                if test_function(x,y):
                    for s in steps:
                        (nx,ny) = (x+s.x,y+s.y)
                        if test_function(nx,ny) and (nx,ny,i-1) in tab:
                            acc += tab[(nx,ny,i-1)]
                    tab[(x,y,i)] = acc
    return tab

def naive_random_generation(steps,length,num_walks,test_function = quarterplane,end_position = end_anywhere_quarterplane):
    walks = []
    tab = precompute_naive_random_generation(steps,length,test_function,end_position)
    for w in range(num_walks):
        x,y = 0,0
        curr_walk = []
        for i in range(length,0,-1):
            r = random.random()*tab[(x,y,i)]
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
############################################################


#def tabulate_endpoints(step_set, side=10):
#    tab = [[0] * side]*side


steve_walk1 = StepSet([(0,1), (1,0), (-1,0), (0,-1)])
steve_walk2 = StepSet([(1,-1), (-1,1), (1,1)])

def gen_rej(ss, n):
    while True:
        walks = GenRGenSWalkCompiler(ss).generate(100, n)
        for w in walks:
            if is_quarter_plane(w) == n:
                return w

import numpy as np

def push_steps(tab, ss, x, y, val=0):
    for s in ss:
        nx = x + s.x
        ny = y + s.y
        if (nx >= 0 and nx < len(tab) and
                ny >= 0 and ny < len(tab[0])):
            tab[nx,ny] += val

def tabulate_all_walks(ss, side=10,stepcount=10):
    blank = np.array([[0]*side]*side)
    curr = blank.copy()
    curr[0,0] = 1
    for step in range(stepcount):
        prev = curr
        curr = blank.copy()
        for i in range(min(step+1, side)):
            for j in range(min(step+1, side)):
                push_steps(curr, ss, i, j, prev[i,j])
    return curr

def print_matrix(mat, prec=2):
    fstring = "%%6.0%df" % prec
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print fstring % mat[len(mat[0])-i-1,j],
        print ""

steve_walk1.slope = (-1,1)

def reset():
    import turtle
    turtle.reset()
    turtle.speed("fastest")

def draw_walk_noreset(walk):
    import turtle
    turtle.pu()
    turtle.setpos(-200, -200)
    turtle.pd()
    turtle.pencolor(1.0, 0.0, 0.0)
    turtle.forward(500)
    turtle.setpos(-200, -200)
    turtle.left(90)
    turtle.forward(500)
    turtle.setpos(-200, -200)
    turtle.pencolor(0.0, 0.0, 0.0)
    for step in walk:
        turtle.goto(turtle.xcor() + 10*step.x,turtle.ycor() + 10*step.y)


def draw_walks_noreset(walks):
    reset()
    for walk in walks:
        print is_quarter_plane(walk)
        if is_quarter_plane(walk) == len(walk):
            draw_walk_noreset(walk)
            sleep(1)

TERM_NEUTRAL=     "TERM_NEUTRAL"#1
TERM_ATOM=            "TERM_ATOM" #2
EPSILON=                "EPSILON" #16
PRODUCT=                "PROD" #4
UNION=                    "UNION" #8
SYMBOL=                 "SYMBOL" #32

def make_union(lst):
    if len(lst) == 0:
        return []
    return [UNION] + lst

def build_system(stepset):
    system = {}

    # Z(i)s
    for step in stepset:
        system[step.symbol] = [TERM_ATOM]

    max_k = min(stepset.max_up, stepset.min_down)

    # DD -> d_eqs
    d_eq = [ UNION ]
    d_eq += [ [ EPSILON ] ]
    d_eq += map(lambda s: [PRODUCT, s.symbol, "DD"], stepset.select(0))
    d_eq += [ [PRODUCT, "L%d"%k, "R%d"%k] for k in range(1, max_k + 1) ]
    system["DD"] = d_eq

    # PP ->
    p_eq = [ UNION ]
    p_eq += [ [ EPSILON ] ]
    p_eq += map(lambda s: [PRODUCT, s.symbol, "PP"], stepset.select(0))
    p_eq += [ [PRODUCT, "L%d"%k, "PP"] for k in range(1, stepset.max_up + 1) ]
    system["PP"] = p_eq

    # Li = Z(i)s D + { Lk R(k-i), k = i+1..a }
    for i in range(1, stepset.max_up + 1):
        li_eq = []
        li_eq += map(lambda s: [PRODUCT, s.symbol, "DD" ], stepset.select(i))

        max_k = min(stepset.max_up, i + stepset.min_down)
        li_eq +=    [ [ PRODUCT, "L%d"%k, "R%d"%(k-i) ]
                                for k in range(i+1, max_k+1) ]
        if len(li_eq) > 0:
            system["L%d"%i] = make_union(li_eq)

    # Rj
    for j in range(1, stepset.min_down + 1):
        rj_eq = []
        rj_eq += map(lambda s: [PRODUCT, s.symbol, "DD" ], stepset.select(-j))
        max_k = min(j+stepset.max_up, stepset.min_down)
        rj_eq += [ [ PRODUCT, "L%d"%(k-j), "R%d"%k ]
                             for k in range(j+1, max_k+1) ]
        if len(rj_eq) > 0:
            system["R%d"%j] = make_union(rj_eq)

    return system

import operator

def using_symbols(rule):
    if rule[0] == TERM_ATOM:
        return []
    elif rule[0] == PRODUCT:
        return reduce(operator.add, map(using_symbols, rule[1:]), [])
    elif rule[0] == EPSILON:
        return []
    elif rule[0] == UNION:
        return reduce(operator.add, map(using_symbols, rule[1:]), [])
    else:
        return [rule]

def clean_system(system):
    for symbol in system:
        pass

import itertools

def rule_genr(rule):
    if rule[0] == TERM_ATOM:
        return None
    elif rule[0] == PRODUCT:
        return " ".join(map(rule_genr, rule[1:]))
    elif rule[0] == EPSILON:
        return ""
    elif rule[0] == UNION:
        return map(rule_genr, rule[1:])
    else:
        return rule

def sys_genrs(system):
    rules = []
    for symbol in system:
        rule = rule_genr(system[symbol])
        if rule == None:
            continue
        elif type(rule) == list:
            rules += map(lambda x: "%s -> %s" % (symbol, x), rule)
        elif type(rule) == str:
            rules += [ "%s -> %s" % (symbol, rule) ]
        else:
            print rule
    # Assembly
    return ";\n".join(rules)



def precompute(N,steps,meanders=True):
        if meanders:
                tab = {(h,0):1 for h in range(0,1+max(steps)*N)}
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



walk_6s = nt_stepsets[6][6]

def test(times=100, size=100, rat_approx=100):
    ss2_ = StepSet(nt_stepsets[6][7])
    if rat_approx > 0:
        ss2_.slope = ss2_.get_best_slope(rat_approx)
    walks = GenRGenSWalkCompiler(ss2_).generate(times, size)
    qpwcount = len(filter(lambda x: x==size, map(is_quarter_plane, walks)))
    return (float(times)/float(qpwcount), ss2_.slope)

def test2(times=100, size=100, rat_approx=100):
    ss2_ = StepSet(nt_stepsets[6][7])
    if rat_approx > 0:
        ss2_.slope = ss2_.get_best_slope(rat_approx)
    walks = GenRGenSWalkCompiler(ss2_).generate(times, size)
    qpwcount = len(filter(lambda x: x==size, map(is_quarter_plane, walks)))
    return (float(sum(map(is_quarter_plane, walks)))/float(qpwcount), ss2_.slope)

def test3(times=100, size=100, rat_approx=100):
    ss2_ = StepSet(nt_stepsets[6][7])
    if rat_approx > 0:
        ss2_.slope = ss2_.get_best_slope(rat_approx)
    walks = GenRGenSWalkCompiler(ss2_).generate(times, size)
    qpwcount = len(filter(lambda x: x==size, map(is_quarter_plane, walks)))
    return (times, size, qpwcount, ss2_.slope)




import cPickle
import os.path
import os
import sys

seed_path = "./generated-walks/"

def save_walk(walk, dirname, nt_size, nt_pos, size, ident, mark= ""):
    filename = "%d_steps_w%d_size_%d_%sid%d" % (nt_size, nt_pos, size, mark, ident)
    with open(os.path.join(dirname, filename), "w") as f:
        cPickle.dump(walk, f)
        f.flush()
        f.close()

def save_walks(walklist, dirname, nt_size, nt_pos, size, mark=""):
    for i in range(len(walklist)):
        save_walk(walklist[i], dirname, nt_size, nt_pos, size, i, mark)


def load_walk_by_filename(filename):
    with open(os.path.join(dirname, filename), "r") as f:
        return cPickle.load


sizes = [ 100, 1000, 10000 ]
times = [ 1000, 1000, 100 ]

nt_min = 3
nt_max = 8

reboot = False

size_pos = 0
sset_size = nt_min
sset_pos = 0


def save_state():
    global size_pos, sset_size, sset_pos
    with open(os.path.join(seed_path, "state.txt"), "w") as f:
        cPickle.dump((size_pos, sset_size, sset_pos), f)
        f.flush()
        f.close()

def load_state():
    global size_pos, sset_size, sset_pos, reboot
    reboot = True
    if os.path.exists(os.path.join(seed_path, "state.txt")):
        try:
            with open(os.path.join(seed_path, "state.txt"), "r") as f:
                (size_pos, sset_size, sset_pos) = cPickle.load(f)
            print "Resuming at size: ", size_pos, "step set size: ", sset_size, "walk: ", sset_pos
            return
        except EOFError:
            print "Resuming did not work, restarting from beginning"
    size_pos = 0
    sset_size = nt_min
    sset_pos = 0



def bulk_walk_generation():
    if not os.path.exists(seed_path):
            os.makedirs(seed_path)

    load_state()

    try:
        while size_pos < len(sizes):
            if not reboot:
                sset_size = nt_min
            while sset_size <= nt_max:
                if not reboot:
                    sset_pos = 0
                while sset_pos < len(nt_stepsets[sset_size]):
                    reboot = False
                    save_state()
                    print "size: ", size_pos, "step set size: ", sset_size, "walk: ", sset_pos
                    # <== DO STUFF ==>
                    ss_list = nt_stepsets[sset_size][sset_pos]
                    ss_best_slope = nt_stepsets_slope[sset_size][sset_pos]
                    ss = StepSet(ss_list)
                    # generate a bunch with the normal slope
                    if ss_best_slope != 0:
                        w1 = GenRGenSWalkCompiler(ss).generate(times[size_pos], sizes[size_pos])
                        save_walks(w1, seed_path, sset_size, sset_pos, sizes[size_pos])
                    # generate a bunch with the "best" slope if not normal
                    if ss_best_slope == None:
                        sset_pos += 1
                        continue
                    ss.slope = ss_best_slope
                    w2 = GenRGenSWalkCompiler(ss).generate(times[size_pos], sizes[size_pos])
                    save_walks(w2, seed_path, sset_size, sset_pos, sizes[size_pos], "b_")
                    # <== END DO STUFF ==>
                    sset_pos += 1
                sset_size += 1
            size_pos += 1
    except KeyboardInterrupt:
        print "Stopped by keyboard, saving state..."
        save_state()
        sys.exit(0)



#if __name__ == "__main__":
#    bulk_walk_generation()



sizes = [ 1000, 10000 ]
times = [ 10000, 10000 ]

irr_slopes = [(4, 1), (3, 1), (7, 2), (24, 7), (31, 9), (86, 25), (375, 109), (461, 134)]
irr_stepset = [(0, 1), (1, 0), (1, -1), (-1, -1), (-1, 0), (-1, 1)]


reboot = False

size_pos = 0
slope_pos = 0


def save_state():
    global size_pos, sset_size, sset_pos
    with open(os.path.join(seed_path, "state-2.txt"), "w") as f:
        cPickle.dump((size_pos, slope_pos), f)
        f.flush()
        f.close()

def load_state():
    global size_pos, slope_pos, reboot
    reboot = True
    if os.path.exists(os.path.join(seed_path, "state-2.txt")):
        try:
            with open(os.path.join(seed_path, "state-2.txt"), "r") as f:
                (size_pos, slope_pos) = cPickle.load(f)
            print "Resuming at size: ", size_pos, "slope pos: ", slope_pos
            return
        except EOFError:
            print "Resuming did not work, restarting from beginning"
    size_pos = 0
    slope_pos = 0

seed_path = "./generated-walks-irr/"

def push_info(path, line):
    fn = os.path.join(seed_path, "info.txt")
    if os.path.exists(fn):
        if not os.path.isfile(fn):
            raise Exception
    with open(fn, "a") as f:
        print line
        f.write(line)
        f.write("\n")
        f.flush()
        f.close()


def irrational_slope_precision():
    global sizes, times, irr_slopes, irr_stepset, size_pos, slope_pos, reboot, seed_path
    if not os.path.exists(seed_path):
            os.makedirs(seed_path)

    load_state()

    ss = StepSet(irr_stepset)

    try:
        while size_pos < len(sizes):
            if not reboot:
                slope_pos = 0
            while slope_pos < len(irr_slopes):
                reboot = False
                save_state()
                print "size: ", size_pos, "slope pos: ", slope_pos
                # <== DO STUFF ==>
                ss.slope = irr_slopes[slope_pos]
                genr = GenRGenSWalkCompiler(ss)
                num_rules = genr.compile_equations().count('\n')
                push_info(seed_path, "===========")
                push_info(seed_path, "Slope: %s" % (irr_slopes[slope_pos],))
                push_info(seed_path, "Num rules: %s" % num_rules)
                push_info(seed_path, "Walk size: %d" % sizes[size_pos])
                walks = genr.generate(times[size_pos], sizes[size_pos])
                save_walks(walks, seed_path,
                                     len(irr_stepset), slope_pos, sizes[size_pos])
                # write info
                walk_sizes = map(is_quarter_plane, walks)
                qpw_count = len(filter(lambda size: size == sizes[size_pos], walk_sizes))
                push_info(seed_path, "Walk lengths: %s" % walk_sizes)
                push_info(seed_path, "QPW count: %d" % qpw_count)
                push_info(seed_path, "**")
                push_info(seed_path, "%s %d %d" % (irr_slopes[slope_pos], sizes[size_pos], qpw_count))
                # <== END DO STUFF ==>
                slope_pos += 1
            size_pos += 1
    except KeyboardInterrupt:
        print "Stopped by keyboard, saving state..."
        save_state()
        sys.exit(0)


#if __name__ == "__main__":
#    irrational_slope_precision()




# WORK SESSION #
################

ss_sym = StepSet([(1,0), (0,1), (1,-1), (-1,-1), (-1,0)])

nt67 = StepSet(nt_stepsets[6][7])
nt67.slope = nt_stepsets_slope[6][7]
nt67.slope = nt67.get_best_slope(1000)

mrs = StepSet([(1,0), (0,1), (-1, 0), (1, -1), (-1, -1), (-2, -1)])
mrs2 = StepSet([(1,0), (0,1), (-1, 0), (0, -1),
                                (-1, -1), (-2, -1), (-1, -2)])


mrs = StepSet([(1,0), (0,1), (-1, 0), (1, -1), (-1, -1), (-2, -1)])
mrs2 = StepSet([(1,0), (0,1), (-1, 0), (0, -1),
                                (-1, -1), (-2, -1), (-1, -2)])

chinese = StepSet([(1,0), (0,1), (1,-1), (0,-1), (-1,-1), (-1,0)])
