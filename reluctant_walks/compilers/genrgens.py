# @Date: 2018-03-21-20:33
# @Email: lumbroso@cs.princeton.edu
# @Filename: genrgens.py
# @Last modified time: 2018-03-27-23:58

import os as _os
try:
    # Python 3
    from functools import reduce
except ImportError:
    pass

from reluctant_walks.compilers import _package_info, _package_ensure
from reluctant_walks.compilers import WalkCompiler

from reluctant_walks.config import package_raise as _package_raise

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
        # Call GenRGenS and capture stdout
        self.call_script(times, size)

        # Parse the output and create the actual walks
        string_walks = self.__latest_output.strip().split('\n')

        walks = []
        for sw in string_walks:
            string_steps = sw.split(' ')
            walks.append(list(map(
                lambda n: self.__stepset.get(n), string_steps)))

        self.__walks.append(walks)

        return walks

    def call_script(self, times, size):
        # NOTE: requires the GenRGenS binary be installed.
        _package_ensure('genrgens')
        _package_ensure('java')
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
        _package_ensure('genrgens')
        _package_ensure('java')

        PATH_TO_GENRGENS = _package_info('genrgens').get('path', '')

        if not _os.path.exists(PATH_TO_GENRGENS):
            _package_raise('genrgens')

        # FIXME: ensure this is Python 2/3 compatible.
        from subprocess import Popen, PIPE
        genrgens_cmdline = [ "java", "-cp",
                             PATH_TO_GENRGENS,
                             "GenRGenS.GenRGenS",
                             "-nb", str(times),
                             "-size", str(size),
                             filename ]

        output = Popen(genrgens_cmdline,
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



# ==============================================================================
# This is some legacy code that compiles the equation using a more Pythonic
# structure than the string implementation above.
#
# NOTE: Not clear this is functional, or efficient.
# NOTE: This is probably supplemented by the work done by combstruct2json.
# FIXME: Determine if this is efficient and possibly refactor with above
#        implementation
# ==============================================================================

TERM_NEUTRAL=     "TERM_NEUTRAL"#1
TERM_ATOM=        "TERM_ATOM" #2
EPSILON=          "EPSILON" #16
PRODUCT=          "PROD" #4
UNION=            "UNION" #8
SYMBOL=           "SYMBOL" #32

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

def using_symbols(rule):
    import operator
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
