from __future__ import print_function, division, absolute_import

import sys
import os
import unittest

# from fontPens.digestPointPen import DigestPointPen

###### remove when fontPens is on PyPI
from ufoLib.pointPen import AbstractPointPen


class DigestPointPen(AbstractPointPen):
    """
    This calculates a tuple representing the structure and values in a glyph:

        - including coordinates
        - including components
    """

    def __init__(self, ignoreSmoothAndName=False):
        self._data = []
        self.ignoreSmoothAndName = ignoreSmoothAndName

    def beginPath(self, identifier=None):
        self._data.append(('beginPath', identifier))

    def endPath(self):
        self._data.append('endPath')

    def addPoint(self, pt, segmentType=None, smooth=False, name=None, **kwargs):
        if self.ignoreSmoothAndName:
            self._data.append((pt, segmentType))
        else:
            self._data.append((pt, segmentType, smooth, name))

    def addComponent(self, baseGlyphName, transformation, identifier=None):
        t = []
        for v in transformation:
            if int(v) == v:
                t.append(int(v))
            else:
                t.append(v)
        self._data.append((baseGlyphName, tuple(t), identifier))

    def getDigest(self):
        """
        Return the digest as a tuple with all coordinates of all points.
        """
        return tuple(self._data)

    def getDigestPointsOnly(self, needSort=True):
        """
        Return the digest as a tuple with all coordinates of all points,
        - but without smooth info or drawing instructions.
        - For instance if you want to compare 2 glyphs in shape,
          but not interpolatability.
        """
        points = []
        for item in self._data:
            if isinstance(item, tuple) and isinstance(item[0], tuple):
                points.append(item[0])
        if needSort:
            points.sort()
        return tuple(points)

###### end remove

import defcon
import booleanOperations


VERBOSE = False


class BooleanTests(unittest.TestCase):

    pass


def _makeTestCase(glyph, booleanMethodName, args=None):
    # get the font
    font = glyph.font
    # skip if the booleanMethodName does not exist as layer
    if booleanMethodName not in font.layers:
        return False, None
    expectedLayer = font.layers[booleanMethodName]
    # skip if the glyph name does not exist in the expected layer
    if glyph.name not in expectedLayer:
        return False, None
    expectedGlyph = expectedLayer[glyph.name]

    if args is None:
        if len(glyph) < 2:
            # skip if not args are given and the glyph has only 1 contour
            return False, None
        # set the first contour as subject contour and the rest as clip contour
        args = [[glyph[0]], glyph[1:]]

    func = getattr(booleanOperations, booleanMethodName)

    def test(self):
        if VERBOSE:
            print("test: '%s' for '%s'" % (glyph.name, booleanMethodName))
        testPen = DigestPointPen()
        func(*args, outPen=testPen)
        expectedPen = DigestPointPen()
        expectedGlyph.drawPoints(expectedPen)
        self.assertEqual(testPen.getDigest(), expectedPen.getDigest(), "Glyph name '%s' failed for '%s'." % (glyph.name, booleanMethodName))

    return True, test


def _makeUnionTestCase(glyph, method):
    return _makeTestCase(glyph, method, args=[glyph])


def _addGlyphTests():
    root = os.path.join(os.path.dirname(__file__), 'testdata')
    path = os.path.join(root, "test.ufo")
    font = defcon.Font(path)

    booleanMethods = {
        "union": _makeUnionTestCase,
        "difference": _makeTestCase,
        "intersection": _makeTestCase,
        "xor": _makeTestCase,
    }

    for glyph in font:
        for booleanMethod, testMaker in booleanMethods.items():
            shouldPerformTest, testMethod = testMaker(glyph, booleanMethod)
            if shouldPerformTest:
                testMethodName = "test_%s_%s" % (glyph.name, booleanMethod)
                testMethod.__name__ = testMethodName
                setattr(BooleanTests, testMethodName, testMethod)


_addGlyphTests()


if __name__ == '__main__':
    sys.exit(unittest.main())
