# @Date:   2018-03-21-20:32
# @Email:  lumbroso@cs.princeton.edu
# @Filename: combstruct.py
# @Last modified time: 2018-03-21-22:25

try:
    # Python 3
    from functools import reduce
except ImportError:
    pass
#from . import _package_ensure, _package_info
#from . import WalkCompiler
from reluctant_walks.compilers import _package_info, _package_ensure
from reluctant_walks.compilers import WalkCompiler

# ==============================================================================

_TEMPLATE_COMBSTRUCT_HEADER = """
Sys := {
    %s
}
"""

# ==============================================================================

class CombstructWalkCompiler(WalkCompiler):

    def __init__(self, stepset):
        self.__stepset = stepset
        self.__equations = ""
        self.__equations_list = []
        self.__walks = []

    @property
    def equations(self):
        return self.__equations_list

    @property
    def walks(self):
        raise Exception(
            "The 'combstruct' abstract class cannot generate objects.")

    def generate(self, times, size):
        raise Exception(
            "The 'combstruct' abstract class cannot generate objects.")

    def compile(self, header=True):
        """
        """
        # Ensure equations are compiled
        self.compile_equations()

        # Generate string output
        if header:
            # Sys := { A = ..., B = ..., ...}
            self.__script = _TEMPLATE_COMBSTRUCT_HEADER % (
                ",\n    ".join(self.__equations_list)
            )

        else:
            self.__script = ",\n".join(self.__equations_list)

        return self.__script

    def make_op(self, op, lst):
        if len(lst) == 0:
            return ""
        elif len(lst) == 1:
            return lst[0]
        else:
            return "%s(%s)" % (op, ", ".join(lst))

    def compile_equations(self):
        stepset = self.__stepset

        # do the atoms and epsilon
        unit_equations = list(map(lambda s: "%s=Atom" % s.symbol, stepset)) + \
                              ["E=Epsilon"]

        # D equation
        max_k = min(stepset.max_up, stepset.min_down)
        zds = list(map(lambda s: "Prod(%s, DD)" % s.symbol, stepset.select(0)))
        lrs = [ "Prod(L%d, R%d)" % (k,k) for k in range(1, max_k + 1) ]
        d_equation = "DD=%s" % self.make_op("Union", ["E"] + zds + lrs)

        # Paux equation
        #zps = map(lambda s: "Prod(%s, Paux)" % s.symbol, stepset.select(0))
        zps = []
        lps = [ "Prod(L%d, Paux)" % i for i in range(1, stepset.max_up + 1) ]
        p_equation = "Paux=%s" % self.make_op("Union", ["E"] + zps + lps)

        # Li equations
        li_equations = []
        for i in range(1, stepset.max_up + 1):
            zdsi = list(map(lambda s: "Prod(%s, DD)" % s.symbol,
                            stepset.select(i)))
            max_k = min(stepset.max_up, i + stepset.min_down)
            lrsi = [ "Prod(L%d, R%d)" % (k, k-i)
                             for k in range(i+1, max_k + 1) ]
            all = zdsi + lrsi
            if len(all) > 0:
                li_equations += [ "L%d=%s" % (i, self.make_op("Union", all)) ]

        # Rj equations
        rj_equations = []
        for j in range(1, stepset.min_down + 1):
            zdsj = list(map(lambda s: "Prod(%s, DD)" % s.symbol,
                            stepset.select(-j)))
            max_k = min(j + stepset.max_up, stepset.min_down)
            lrsj = [ "Prod(L%d, R%d)" % (k-j, k)
                             for k in range(j+1, max_k + 1) ]
            all = zdsj + lrsj
            if len(all) > 0:
                rj_equations += [ "R%d=%s" % (j, self.make_op("Union", all)) ]

        all_equations = (["PP=Prod(DD, Paux)"] +
                                         [p_equation] +
                                         [d_equation] +
                                         li_equations +
                                         rj_equations +
                                         unit_equations)

        self.__equations_list = all_equations
        return self.__equations_list
