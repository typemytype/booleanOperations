from __future__ import print_function, division, absolute_import


class Error(Exception):
    """Base BooleanOperations exception"""


class InvalidContourError(Error):
    """Rased when any input contour is invalid"""


class InvalidSubjectContourError(InvalidContourError):
    """Rased when a 'subject' contour is not valid"""


class InvalidClippingContourError(InvalidContourError):
    """Rased when a 'clipping' contour is not valid"""


class ExecutionError(Error):
    """Raised when clipping execution fails"""
