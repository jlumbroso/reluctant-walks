# @Date:   2018-03-21-18:28
# @Email:  lumbroso@cs.princeton.edu
# @Filename: config.py
# @Last modified time: 2018-03-22-13:09

import os as _os
import platform as _platform
import subprocess as _subprocess

# ==============================================================================

_MAKE_ABS = True

_ENV_MAPLE_PATH='MAPLE_PATH'
_ENV_BOLTZ_PATH='BOLTZOC_PATH'
_ENV_GENRGENS_PATH='GENRGENS_PATH'

_BIN_MAPLE_DEFAULT = "/Library/Frameworks/Maple.framework/Versions/{}/bin/maple"

_STR_UNAVAILABLE_MSG="Requested feature requires '{}', detected as unavailable."

# ==============================================================================

class UnavailableException(Exception):
    pass

# ==============================================================================

def detect_env():

    info = {}

    sage_info = {}
    maple_info = {}
    java_info = {}
    genrgens_info = {}

    # Detect if sage is available or not
    sage_info['available'] = False
    try:
        import sage
    except ImportError:
        sage_info['error'] = 1
        sage_info['message'] = "Sage does not seem available (not run from Sage terminal)."
    except KeyboardInterrupt:
        sage_info['error'] = 2
        sage_info['message'] = "Keyboard event aborted detection of Sage."
    except Exception as e:
        sage_info['error'] = 3
        sage_info['message'] = "Unexpected error while importing Sage: {}".format(e)

    # Detect if specific subpackage is available
    if not 'error' in sage_info:
        try:
            import sage.all as sage_all
            sage_info['available'] = True
        except Exception as e:
            sage_info['available'] = False
            sage_info['error'] = 4
            sage_info['message'] = (
                "Sage present, but seems broken (sage.all not found): {}".format(e)
                )

    # Detect availability of "which"
    has_which = (_os.system("which which 1> /dev/null 2> /dev/null") == 0)

    # Detect availability of Java/JRE/JDK
    java_info['available'] = False

    if _platform.system() == 'Darwin':
        # Mac OS X has this weird hack that running "java" or "javac"
        # will produce a dialog even when they are not available.
        # This block will catch the issue and prevent it from affecting
        # the rest of the code.
        #
        # From: https://stackoverflow.com/a/31776543/408734

        try:
            out = _subprocess.check_output(
                "/usr/libexec/java_home -V 2> /dev/stdout",
                shell=True)
        except _subprocess.CalledProcessError as e:
            # If error code is 1 (or more) then no VM available
            java_info['available'] = False
            java_info['error'] = 5
            java_info['message'] = e.output

    if 'error' not in java_info:

        if _os.environ.get('JAVA_HOME', "") != "":
            java_info['available'] = True

        if has_which:
            if _os.system("which java 1> /dev/null 2> /dev/null") == 0:
                java_info['available'] = True
                java_info['path'] = _subprocess.check_output(
                    "which java", shell=True)

                # Remove whitespace if any
                if java_info['path'] != None:
                    java_info['path'] = java_info['path'].strip()
            else:
                java_info['available'] = False


    # Detect availability of Maple
    maple_info['available'] = has_which and (
        _os.system("which maple 1> /dev/null 2> /dev/null") == 0)

    if not maple_info['available'] and _os.environ.get(_ENV_MAPLE_PATH, '') != '':
        # Check environment variable
        maple_path = _os.environ.get(_ENV_MAPLE_PATH, '')

        if file.exists(maple_path):
            maple_info['available'] = True
            maple_info['path'] = maple_path

    if not maple_info['available']:

        # Try looking in hardcoded places
        import glob as _glob

        versions_path = _glob.glob(_BIN_MAPLE_DEFAULT.format("*"))
        versions_name = list(map(
            lambda path: path.split('/')[-3], versions_path))

        selected_version_name = None
        if len(versions_name) > 0:
            # Select 'Current' or most recent
            if "Current" in versions_name:
                selected_version_name = "Current"
            else:
                selected_version_name = sorted(versions_name,
                                               reverse=True)[0]

        if selected_version_name != None:
            maple_info['available'] = True
            maple_info['path'] = _BIN_MAPLE_DEFAULT.format(selected_version_name)

    # Detect GenRGenS' availability
    genrgens_info['available'] = False
    import reluctant_walks as _rw

    # Look for the .jar file
    _opa = lambda s: s
    if _MAKE_ABS:
        _opa = _os.path.abspath

    files_a = _os.listdir(_os.path.join(_rw.__path__[0], "."))
    files_b = _os.listdir(_os.path.join(_rw.__path__[0], ".."))
    tmp_lambda = (lambda x: "GenRGenS" in x and "-bin.jar" in x)
    files_a = list(filter(tmp_lambda, files_a))
    files_b = list(filter(tmp_lambda, files_b))
    if len(files_a) > 0:
        genrgens_info['available'] = True
        genrgens_info['path'] = _os.path.join(_opa(
            _os.path.join(_rw.__path__[0], ".")), files_a[0])
    if len(files_b) > 0:
        genrgens_info['available'] = True
        genrgens_info['path'] = _os.path.join(_opa(
            _os.path.join(_rw.__path__[0], "..")), files_b[0])

    if _os.environ.get(_ENV_GENRGENS_PATH, '') != '':
        s = _os.environ.get(_ENV_GENRGENS_PATH)
        if _os.path.exists(s) or genrgens_info.get('path', '') == '':
            genrgens_info['available'] = True
            genrgens_info['path'] = _opa(s)

    # Detect availability of Darrasse's C Boltzmann sampler
    # FIXME: implement this.

    # Assemble
    info['sage'] = sage_info
    info['maple'] = maple_info
    info['java'] = java_info
    info['genrgens'] = genrgens_info

    return info

SETUP_INFO = detect_env()

# ==============================================================================

def package_raise(package_name, info=None):

    msg = _STR_UNAVAILABLE_MSG.format(package_name)

    if package_name == 'sage':
        msg = "This feature requires sage: Run from sage kernel."

    elif package_name == 'maple':
        msg = ("This feature still requires Maple: Acquire license, or " +
               "help implement an open-source alternative!")

    raise UnavailableException(msg)

def package_info(package_name, info=None):

    if info == None:
        info = SETUP_INFO

    pkg_info = info.get(package_name, {})

    return pkg_info

def package_ensure(package_name, info=None, fail=True):

    pkg_info = package_info(package_name=package_name, info=info)
    pkg_available = pkg_info.get('available', False)

    if pkg_available:
        return True
    else:
        if fail:
            package_raise(package_name=package_name, info=info)

    return False

# ==============================================================================

# Src:
# http://www.johndcook.com/blog/2010/10/20/best-rational-approximation/

def farey_rat_approx(x, N):
    a, b = 0, 1
    c, d = 1, 1
    while (b <= N and d <= N):
            mediant = float(a+c)/(b+d)
            if x == mediant:
                    if b + d <= N:
                            return a+c, b+d
                    elif d > b:
                            return c, d
                    else:
                            return a, b
            elif x > mediant:
                    a, b = a+c, b+d
            else:
                    c, d = a+c, b+d

    if (b > N):
            return c, d
    else:
            return a, b
