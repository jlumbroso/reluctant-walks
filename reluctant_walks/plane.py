# @Date:   2018-03-21-19:49
# @Email:  lumbroso@cs.princeton.edu
# @Filename: plane.py
# @Last modified time: 2018-03-29-22:51

try:
    # Python 3
    from functools import reduce
except ImportError:
    pass
# Utility function to transform a float to a rationales
from reluctant_walks.config import farey_rat_approx as _farey_rat_approx
from reluctant_walks.config import package_ensure as _package_ensure
import reluctant_walks.graphics as _graphics

class Step(object):
    __kind = 'plane'
    COUNT = 0

    def __init__(self, x_delta, y_delta, slope_p = 0, slope_q = 1):
        """Defines the coordinates of the step."""
        self.__x_delta = x_delta
        self.__y_delta = y_delta
        self.__slope_p = slope_p
        self.__slope_q = slope_q
        self.__id = Step.COUNT
        self.__name = "Z{}".format(self.__id)
        Step.COUNT += 1

    def __sign(self, value):
        if value > 0:
            return "+"
        elif value < 0:
            return "-"
        else:
            return " "

    def __repr__(self):
        return "Step({}, {}, {})".format(
            self.__name, self.__x_delta, self.__y_delta)

    def __str__(self):
        return "{}: ({}{}, {}{}) weight: {}".format(
            self.__name,
            self.__sign(self.__x_delta),
            abs(self.__x_delta),
            self.__sign(self.__y_delta),
            abs(self.__y_delta),
            self.weight)

    @property
    def symbol(self):
        return self.__name

    @property
    def symbol_id(self):
        return self.__id

    @property
    def x(self):
        return self.__x_delta

    @x.setter
    def x(self, value):
        self.__x_delta = value

    @property
    def y(self):
        return self.__y_delta

    @y.setter
    def y(self, value):
        self.__y_delta = value

    # FIXME: determine if/where this is used (my hunch is that it is used
    # nowhere); determine if this makes (mathematical) sense.
    @property
    def slope(self):
        return (self.__slope_p, self.__slope_q)

    @slope.setter
    def slope(self, value):
        if type(value) is tuple and len(value) == 2:
            (self.__slope_p, self.__slope_q) = value
        else:
            self.__slope_p = value
            self.__slope_q = 1

    @property
    def weight(self):
        return (self.__slope_q * self.__y_delta)+self.__slope_p *self.__x_delta




class StepSet(object):
    __kind = 'plane'

    def __init__(self, init_set = [], slope_p = 0, slope_q = 1,
                 cached_bestslope=None, cached_bestslope_ratprecision=10):
        self.__set = []
        self.__slope_p = slope_p
        self.__slope_q = slope_q
        for step in init_set:
            self.add(Step(step[0],step[1]))

        # caching system for 'best slopes' (so this can be useful without Sage)
        self.__cached_bestslope = cached_bestslope
        self.__cached_bestslope_ratprecision = cached_bestslope_ratprecision

    def add(self, step):
        if not step.symbol in map(lambda s: s.symbol, self.__set):
            step.slope = (self.__slope_p, self.__slope_q)
            self.__set += [step]

    def add_step(self, x_delta, y_delta):
        self.__set += [Step(x_delta, y_delta)]

    def __iter__(self):
        for s in self.__set:
            yield s

    def get(self, symbol):
        for s in self.__set:
            if s.symbol == symbol or s.symbol == "Z" + symbol:
                return s

    def select(self, weight):
        for s in self.__set:
            if s.weight == weight:
                yield s

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        s = "StepSet\n"
        for step in self:
            s += "    {}\n".format(step.__str__())
        return s

    @property
    def figure(self):
        return _graphics.plot_stepset(self.__set)

    @property
    def max_up(self):
        return reduce(max, map(lambda s: s.weight, self.__set), 0)

    @property
    def min_down(self):
        return (-reduce(min, map(lambda s: s.weight, self.__set), 0))

    @property
    def drift(self):
        drift = 0
        for step in self.__set:
            drift += step.x
            drift += step.y
        return drift

    def __is_positive_real(self, v):
        try:
            float(v)
            return float(v) >= 0
        except KeyboardInterrupt:
            raise
        except:
            return False

    def solve_inventory_equation(self):
        # NOTE: This computation currently requires Sage.
        _package_ensure("sage")
        from sage.all import var, maxima, diff

        # ==================================================================
        # FIXME: document where this math comes from.

        # Computation
        x, y = var("x y", domain = "real")
        step_set = map(lambda ss: (ss.x, ss.y), self.__set)
        # p: inventory polynomial
        p = sum(map(lambda q:x**q[0] * y**q[1], step_set))
        # solve diff(p, x) == 0 && diff(p, y) == 0
        solutions = maxima([diff(p, x) == 0, diff(p, y) == 0]).solve([x,y]).sage()
        #solutions = solve([diff(p, x) == 0, diff(p, y) == 0], x, y)
        try:
            # just keep real solutions
            real_solutions = filter(lambda l: reduce(lambda a,b: a and b,
                map(lambda eq: self.__is_positive_real(eq.rhs()), l)),
                                                            solutions)
        except KeyboardInterrupt:
            raise
        except:
            return (p, [])

        # FIXME: circumventing a kink in solve
        if len(real_solutions) > 1:
            real_solutions = filter(lambda l:
                                    not (l[0].rhs().n() == 0 and l[1].rhs().n() == 0),
                                    real_solutions)

        # ==================================================================
        return (p, real_solutions)

    def get_best_slope(self, rat_precision=10, force=False):
        if self.drift >= 0:
            return 0

        # ======================================================
        # FIXME: Lame caching (to allow for precomputed best
        # slopes, so this can be useful without Sage)
        if (not force and self.__cached_bestslope != None and
            self.__cached_bestslope_ratprecision == rat_precision):
            return self.__cached_bestslope
        # ======================================================

        (p, solutions) = self.solve_inventory_equation()
        if len(solutions) == 0:
            return 0
        else:
            # NOTE: This computation currently requires Sage.
            _package_ensure("sage")
            from sage.all import log, round, sqrt

            (alpha, beta) = map(lambda x: x.rhs(), solutions[0])

            # ==================================================================
            # FIXME: document where this math comes from.

            if beta.n() == 1 or (log(alpha)/log(beta)).n() < 0:
                # complicated stuff
                ks_zero = (
                    p(x=1).coefficient(y**(0)) +
                    2*sqrt(p(x=1).coefficient(y**(-1)) * p(x=1).coefficient(y**(-1))))
                ks_max = (
                    p(y=1).coefficient(x**(0)) +
                    2*sqrt(p(y=1).coefficient(x**(-1)) * p(y=1).coefficient(x**(-1))))
                if ks_zero < ks_max:
                    # vertical half plane
                    return (1,0)
                else:
                    # horizontal half plane
                    return (0,1)

            else:
                proposed_slope = log(alpha)/log(beta)
                if round(proposed_slope.n()) == proposed_slope.n():
                    # an integer
                    return round(proposed_slope.n())
                else:
                    # a rational or transcendant
                    intpart = int(proposed_slope.n())
                    farey = _farey_rat_approx(proposed_slope.n()-intpart, rat_precision)
                    (dragons, den) = (farey[0] + intpart*farey[1], farey[1])
                    return (dragons, den)

            # ==================================================================

    @property
    def slope(self):
        return (self.__slope_p, self.__slope_q)

    @slope.setter
    def slope(self, value):
        if type(value) is tuple and len(value) == 2:
            (self.__slope_p, self.__slope_q) = value
        else:
            self.__slope_p = value
            self.__slope_q = 1
        for s in self.__set:
            s.slope = (self.__slope_p, self.__slope_q)
