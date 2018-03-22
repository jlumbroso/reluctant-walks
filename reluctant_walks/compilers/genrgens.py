# @Date: 2018-03-21-20:33
# @Email: lumbroso@cs.princeton.edu
# @Filename: genrgens.py
# @Last modified time: 2018-03-21-20:53

from . import _package_ensure
from . import WalkCompiler

# ==============================================================================

_TEMPLATE_GENRGENS_GRAMMAR = """
TYPE = GRAMMAR
SYMBOLS = WORDS
START = PP
RULES =
{}
"""

# ==============================================================================

class GenRGenSWalkCompiler(WalkCompiler):

    def __init__(self, stepset):
        self.__stepset = stepset
        self.__equations = ""
        self.__walks = []

    @property
    def walks(self):
        return self.__walks

    def generate(self, times, size):
        self.call_script(times, size)
        string_walks = self.__latest_output.strip().split('\n')
        walks = []
        for sw in string_walks:
            walks += [ map(lambda n: self.__stepset.get(n), sw.split(' ')) ]
        self.__walks += walks
        return walks

    def call_script(self, times, size):
        # NOTE: requires the GenRGenS binary be installed.
        _ensure_package('genrgens')

        #
        from tempfile import NamedTemporaryFile
        self.compile(times, size)
        try:
            script_file = NamedTemporaryFile()
            script_file.write(self.__script)
            script_file.flush()
            self.__latest_output = self.run_genrgens(times, size, script_file.name)
            script_file.close()
        except KeyboardInterrupt:
            raise
        except:
            self.__latest_output = ""
        return self.__latest_output

    def run_genrgens(self, times, size, filename):
        # NOTE: requires GenRGenS binary be installed.
        _ensure_package('genrgens')

        # FIXME: ensure this is Python 2/3 compatible.
        from subprocess import Popen, PIPE
        output = Popen(["java", "-cp",
                        PATH_TO_GENRGENS,
                        "GenRGenS.GenRGenS",
                        "-nb", str(times),
                        "-size", str(size),
                        filename ],
                       stdout=PIPE,
                       stderr=open("/dev/null", "w")).communicate()[0]

        return output

    def compile(self, times, size):
        self.compile_equations()
        self.__script = _TEMPLATE_GENRGENS_GRAMMAR.format(self.__equations)
        return self.__script

    def gcd(self, *numbers):
        from fractions import gcd
        return reduce(gcd, numbers)

    def lcm(self, *numbers):
        def lcm(a, b):
                return (a * b) // self.gcd(a, b)
        return reduce(lcm, numbers, 1)

    def compile_equations(self):
        stepset = self.__stepset

        lparam = stepset.max_up #max(stepset.max_up, stepset.min_down)
        rparam = stepset.min_down
                                 #lcm(stepset.max_up, stepset.min_down))

        # D = eps + Z(0)s D + { Li Ri, i = 1 .. k }
        d_equations = [ "" ]     # epsilon
        d_equations += map(lambda s: "%s DD" % s.symbol, stepset.select(0))
        max_k = min(stepset.max_up, stepset.min_down)
        d_equations += [ "L%d R%d" % (k,k) for k in range(1, max_k + 1) ]
        d_equations = map(lambda x: "DD -> %s" % x, d_equations)

        # Paux = eps + Z(0)s P + { Li P, i = 1 .. k }
        p_equations = [ "" ]
        #p_equations += map(lambda s: "%s Paux" % s.symbol, stepset.select(0))
        p_equations += [ "L%d Paux" % k for k in range(1, stepset.max_up + 1) ]
        p_equations = map(lambda x: "Paux -> %s" % x, p_equations)

        # Li = Z(i)s D + { Lk R(k-i), k = i+1..a }
        li_equations = []
        for i in range(1, lparam + 1):
            zdsi = map(lambda s: "%s DD" % s.symbol, stepset.select(i))
            max_k = min(stepset.max_up, i + stepset.min_down)
            lrsi = [ "L%d R%d" % (k, k-i)
                             for k in range(i+1, max_k + 1) ]
            if len(zdsi) + len(lrsi) == 0:
                li_equations += [ "L%d ->" % i ]
            li_equations += map(lambda x: "L%d -> %s" % (i, x), zdsi + lrsi)

        # Rj equations
        # Rj = Z(-j)s D + { L(k-j) Rk, k = j+1..b }
        rj_equations = []
        for j in range(1, rparam + 1):
            zdsj = map(lambda s: "%s DD" % s.symbol, stepset.select(-j))
            max_k = min(j+stepset.max_up, stepset.min_down)
            lrsj = [ "L%d R%d" % (k-j, k)
                             for k in range(j+1, max_k + 1) ]
            rj_equations += map(lambda x: "R%d -> %s" % (j, x), zdsj + lrsj)

        all_equations = (["PP -> DD Paux"] +
                                         p_equations +
                                         d_equations +
                                         li_equations +
                                         rj_equations)

        self.__equations = " ;\n".join(all_equations) + ";"
        return self.__equations
