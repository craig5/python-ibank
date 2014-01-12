# vim: set filetype=python expandtab tabstop=4 shiftwidth=4 autoindent smartindent:
import os
import logging

_LOGGER_NAME  = __name__


class BadDataFileException(Exception):
    pass


class Reader(object):

    # Yes, it's a little confusing that "data_file" is really a dir.
    # This is the "data file" configured for iBank.
    # May need to change this at some point.
    # This is why "data_file" is a named arg: it'll be easier to deprecate.
    def __init__(self, data_file=None):
        """
            Initialize reader object.

            params: data_file
        """
        self.logger = logging.getLogger(_LOGGER_NAME)
        self.logger.debug("Logger initialized.")
        self.data_file = data_file
        self.logger.debug("Data file: {0}".format(self.data_file))
        self.__verify_arguments()

    def __verify_arguments(self):
        self.logger.debug("Verifying arguments.")
        if self.data_file is None:
            raise BadDataFileException("No data file provided.")
        if not os.path.isdir(self.data_file):
            raise BadDataFileException("Data file given is not a directory.")
        self.logger.debug("Data file passes tests: {0}".format(self.data_file))

    def __call__(self):
        self.logger.debug("Inside call.")

# End of file.
