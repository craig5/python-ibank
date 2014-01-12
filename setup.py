#!/usr/bin/env python
# vim: set filetype=python expandtab tabstop=4 shiftwidth=4 autoindent smartindent:
#from distutils.core import setup
import os
import logging
import setuptools
import distutils.cmd
import subprocess

# TODO add check to make sure required libs are present (eg sqlite3)

_PACKAGE_NAME     = 'python-ibank',
_PACKAGE_VERSION  = '0.0.1'
_LIB_DIR          = 'lib'
_BIN_DIR          = 'bin'
_DESCRIPTION      = ''
_HOME_DIR         = os.path.expanduser('~')
print "home:",_HOME_DIR
_HOME_DIR = '/Users/csebenik'
# TODO verify _HOME_DIR makes sense
# TODO ugh.... this isnt working :/
#_VIRTUALENV_DIR   = os.path.join(_HOME_DIR, '.virtualenvs', _PACKAGE_NAME)
_VIRTUALENV_DIR   = os.path.join('.virtualenv')

# TODO remove all of the print statements and replace with logging
_LOGGER_NAME      = __name__
logger            = logging.getLogger(_LOGGER_NAME)



class VirtualEnv(distutils.cmd.Command):
    """Setup virtualenv."""
    description = "Setup virtualenv."
    user_options = []

    def __init__(self, dist=None):
        self.announce('Init virtualenv.', level=3)
        self.finalized = None

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        """Create the virtualenv."""
        # TODO finish automating virtualenv... manual is ok for now
        self.announce('Running virtualenv.', level=2)
        print "Creating virtual env in:", _VIRTUALENV_DIR
        # TODO check to make sure parent dir exists
        # TODO what do to if already exists? re-create? destroy and create?
        cmd = 'virtualenv --no-site-packages {0}'.format(_VIRTUALENV_DIR)
        print "cmd:",cmd
        proc = subprocess.Popen(cmd, shell=True,
                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout,stderr = proc.communicate()
        returnCode = proc.returncode
        print "stdout:",stdout
        print "stderr:",stderr
        print "return code:", returnCode
        # TODO need to symlink bin/* into .virtualenv/bin/


setuptools.setup(
    name          = _PACKAGE_NAME,
    version       = _PACKAGE_VERSION,
    description   = 'Python libraries for reading iBank files.',
    author        = 'Craig Sebenik',
    author_email  = 'craig5@users.noreply.github.com',
    url           = 'https://github.com/craig5/python-ibank',
    scripts       = [os.path.join(_BIN_DIR,cur) for cur in os.listdir(_BIN_DIR)
                        if not cur.endswith('.swp')],
    package_dir   = {'': _LIB_DIR},
    packages      = setuptools.find_packages(_LIB_DIR),
    cmdclass      = {'virtualenv':VirtualEnv}
)
# End of file.
