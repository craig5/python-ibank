# vim: set filetype=python expandtab tabstop=4 shiftwidth=4 autoindent smartindent:
import os
import unittest
import nose

##### HACK!
# TODO fix virtualenv :(
import site
_IBANK_BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_IBANK_LIB_DIR  = os.path.join(_IBANK_BASE_DIR, 'lib')
site.addsitedir(_IBANK_LIB_DIR)
#####
import ibank


class TestiBankReader(unittest.TestCase):

    def setUp(self):
        print "setting up"

    @nose.tools.raises(ibank.BadDataFileException)
    def test_data_file_not_dir(self):
        ibank_reader = ibank.Reader(data_file='foo')

# End of file.
