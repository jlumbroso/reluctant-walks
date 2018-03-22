# @Date:     2018-03-21-20:54
# @Email:    lumbroso@cs.princeton.edu
# @Filename: boltzoc.py
# @Last modified time: 2018-03-21-20:59

from . import _package_ensure, _package_info
from . import WalkCompiler

# ==============================================================================

class BoltzOCWalkCompiler(WalkCompiler):

    def __init__(self, stepset):
        self.__stepset = stepset
        self.__equations = ""
        self.__walks = []

    @property
    def walks(self):
        return self.__walks

    def generate(self, times, size):
        grammar = self.compile_equations()
        try:
            self.__latest_output = self.run_boltzmann(grammar, times, size)
        except:
            return []
        string_walks = self.__latest_output.strip().split('\n')
        walks = []
        for sw in string_walks:
            walks += [ map(lambda n: self.__stepset.get(n), sw[:-1].split(',')) ]
        self.__walks += walks
        return walks

    def run_boltzmann(self, grammar, times, size):
        # NOTE: requires the GenRGenS binary be installed.
        _ensure_package('boltzoc')
        PATH_TO_BOLTZOC = _package_info('boltzoc').get('path', '')

        # FIXME: ensure Python 2/3 compatibility.
        from subprocess import Popen, PIPE
        p = Popen([PATH_TO_BOLTZOC,
                   "--size", "{}".format(size),
                   "--times", "{}".format(times) ],
                  stdin=PIPE,
                  stdout=PIPE,
                  stderr=PIPE)
        output = p.communicate(grammar)[0]

        return output

    def split_seq(self, seq, numPieces):
        newseq = []
        splitsize = 1.0/numPieces*len(seq)
        for i in range(numPieces):
            newseq.append(seq[int(round(i*splitsize)):int(round((i+1)*splitsize))])
        return newseq

    def make_op(self, op, lst):
     if len(lst) == 0:
         return ""
     elif len(lst) == 1:
         return lst[0]
     elif len(lst) == 2:
         return "(%s)" % (op.join(lst))
     else:
         halves = self.split_seq(lst, 2)
         halves = map(lambda x: self.make_op(op, x), halves)
         return "(%s)" % (op.join(halves))

    def compile_equations(self):
        stepset = self.__stepset

        # do the atoms and epsilon
        unit_equations = []#map(lambda s: "%s=Atom" % s.symbol, stepset) + \
                                             #    ["E=Epsilon"]

        # D equation
        max_k = min(stepset.max_up, stepset.min_down)
        zds = map(lambda s: "(%s.DD)" % s.symbol, stepset.select(0))
        lrs = [ "(L%d.R%d)" % (k,k) for k in range(1, max_k + 1) ]
        d_equation = "DD=%s" % self.make_op("+", ["E"] + zds + lrs)

        # Paux equation
        #zps = map(lambda s: "Prod(%s, Paux)" % s.symbol, stepset.select(0))
        zps = []
        lps = [ "(L%d.Paux)" % i for i in range(1, stepset.max_up + 1) ]
        p_equation = "Paux=%s" % self.make_op("+", ["E"] + zps + lps)

        # Li equations
        li_equations = []
        for i in range(1, stepset.max_up + 1):
            zdsi = map(lambda s: "(%s.DD)" % s.symbol, stepset.select(i))
            max_k = min(stepset.max_up, i + stepset.min_down)
            lrsi = [ "(L%d.R%d)" % (k, k-i)
                             for k in range(i+1, max_k + 1) ]
            all = zdsi + lrsi
            if len(all) > 0:
                li_equations += [ "L%d=%s" % (i, self.make_op("+", all)) ]

        # Rj equations
        rj_equations = []
        for j in range(1, stepset.min_down + 1):
            zdsj = map(lambda s: "(%s.DD)" % s.symbol, stepset.select(-j))
            max_k = min(j + stepset.max_up, stepset.min_down)
            lrsj = [ "(L%d.R%d)" % (k-j, k)
                             for k in range(j+1, max_k + 1) ]
            all = zdsj + lrsj
            if len(all) > 0:
                rj_equations += [ "R%d=%s" % (j, self.make_op("+", all)) ]

        all_equations = (["PP=(DD.Paux)"] +
                                         [p_equation] +
                                         [d_equation] +
                                         li_equations +
                                         rj_equations +
                                         unit_equations)

        self.__equations = ("; ".join(all_equations))
        return self.__equations
