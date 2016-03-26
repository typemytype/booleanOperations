from __future__ import print_function, division, absolute_import
from .booleanOperationManager import BooleanOperationManager

__version__ = "0.2"

# export BooleanOperationManager static methods
union = BooleanOperationManager.union
difference = BooleanOperationManager.difference
intersection = BooleanOperationManager.intersection
xor = BooleanOperationManager.xor
getIntersections = BooleanOperationManager.getIntersections
