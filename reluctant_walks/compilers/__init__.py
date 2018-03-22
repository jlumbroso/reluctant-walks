# @Date:   2018-03-21-20:22
# @Email:  lumbroso@cs.princeton.edu
# @Filename: __init__.py
# @Last modified time: 2018-03-21-22:10

#from ..config import package_info as _package_info
#from ..config import package_ensure as _package_ensure
from reluctant_walks.config import package_info as _package_info
from reluctant_walks.config import package_ensure as _package_ensure

# ==============================================================================

class WalkCompiler(object):

    def __init__(self, stepset):
        self.__stepset = stepset
        self.__equations = ""
        self.__walks = []

    def compile_equations(self):
        pass

    def compile(self):
        pass

    @property
    def walks(self):
        return self.__walks

# ==============================================================================

from reluctant_walks.compilers.boltzoc import BoltzOCWalkCompiler
from reluctant_walks.compilers.combstruct import CombstructWalkCompiler
from reluctant_walks.compilers.genrgens import GenRGenSWalkCompiler
from reluctant_walks.compilers.maple import MapleWalkCompiler
