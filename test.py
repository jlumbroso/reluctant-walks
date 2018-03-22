# @Date:   2018-03-21-21:14
# @Email:  lumbroso@cs.princeton.edu
# @Filename: test.py
# @Last modified time: 2018-03-21-21:15

import reluctant_walks
import reluctant_walks.plane
ssl3 = [(0, 1), (1, 0), (1, -1), (-1, -1), (-1, 0), (-1, 1)]
ss3 = reluctant_walks.plane.StepSet(ssl3)

import reluctant_walks.compilers
import reluctant_walks.compilers.combstruct

cwc = reluctant_walks.compilers.combstruct.CombstructWalkCompiler(ss3)
