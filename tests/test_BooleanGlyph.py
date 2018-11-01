from __future__ import print_function, division, absolute_import

import sys
import os
import unittest

from fontPens.digestPointPen import DigestPointPen

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
    root = os.path.join(os.path.dirname(__file__), 'testData')
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
                testMethod.__name__ = str(testMethodName)
                setattr(BooleanTests, testMethodName, testMethod)


_addGlyphTests()


if __name__ == '__main__':
    sys.exit(unittest.main())
