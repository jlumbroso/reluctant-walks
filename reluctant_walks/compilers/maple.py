# @Date: 2018-03-21-20:43
# @Email: lumbroso@cs.princeton.edu
# @Filename: maple.py
# @Last modified time: 2018-03-21-22:12

#from . import _package_ensure, _package_info
#from . import CombstructWalkCompiler
from reluctant_walks.compilers import _package_info, _package_ensure
from reluctant_walks.compilers.combstruct import CombstructWalkCompiler

# ==============================================================================

_TEMPLATE_MAPLE_GRAMMAR = """
with(combstruct):
randomize():
clean_string:= proc(w)
eval(subs( Prod=(()-> args), Sequence=(()->args), E=NULL, Epsilon=NULL, w))
end proc:
{equations}:
for i from 1 to {object_count} do
obj := clean_string(draw([PP, Sys, unlabelled], size={size})):
printf(convert([obj], string)):
printf("\n"):
end do:
quit():"""

# ==============================================================================

class MapleWalkCompiler(CombstructWalkCompiler):

    def __init__(self, stepset):
        self.__stepset = stepset
        self.__equations = ""
        self.__equations_list = []
        self.__walks = []

    @property
    def walks(self):
        return self.__walks

    def generate(self, times, size):
        # NOTE: requires the Maple binary be installed.
        _ensure_package('maple')

        #
        self.call_script(times, size)
        string_walks = self.__latest_output.strip().split('\n')
        walks = []
        for sw in string_walks:
            walks += [ map(lambda n: self.__stepset.get(n), sw[1:-1].split(', ')) ]
        self.__walks += walks
        return walks

    def call_script(self, times, size):
        # NOTE: requires the GenRGenS binary be installed.
        _ensure_package('maple')

        #
        from tempfile import NamedTemporaryFile
        self.compile(times, size)
        try:
            script_file = NamedTemporaryFile()
            script_file.write(self.__script)
            script_file.flush()
            self.__latest_output = self.run_maple(times, size, script_file.name)
            script_file.close()
        except KeyboardInterrupt:
            raise
        except:
            self.__latest_output = ""
        return self.__latest_output

    def _run_maple(self, times, size, filename):
        """
        Calls the Maple binary on the filename and captures output.
        """
        # NOTE: requires the GenRGenS binary be installed.
        _ensure_package('maple')
        PATH_TO_MAPLE = _package_info('maple').get('path', '')

        # FIXME: check Python 2/3 compatibility
        from subprocess import Popen, PIPE
        output = Popen([PATH_TO_MAPLE, "-q", filename ],
                       stdout=PIPE,
                       stderr=open("/dev/null", "w")).communicate()[0]

        return output

    def compile(self, times, size):
        """
        """
        # Ensure equations are compiled
        self.compile_equations()

        # FIXME: 'object_count' seems to not working?
        self.__script = _TEMPLATE_MAPLE_GRAMMAR.format(
            equations=self.__equations,
            object_count=times,
            size=size)

        return self.__script
