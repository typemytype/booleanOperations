import booleanOperations
try:
    from mojo.UI import getDefault, setDefault
    hasMojo = True
except ImportError:
    hasMojo = False

try:
    f = CurrentFont()
except NameError:
    f = {}

if hasMojo:
    glyphViewRoundValues = getDefault("glyphViewRoundValues")
    setDefault("glyphViewRoundValues", 0)


for g in f:
    n = g.naked()
    d = g.getLayer("union")
    d.clear()
    d.appendGlyph(g)
    d.removeOverlap(round=0)

    if len(g) > 1:

        d = g.getLayer("xor")
        d.clear()
        booleanOperations.xor([n[0]], n[1:], d.getPointPen())

        d = g.getLayer("difference")
        d.clear()
        booleanOperations.difference([n[0]], n[1:], d.getPointPen())

        d = g.getLayer("intersection")
        d.clear()
        booleanOperations.intersection([n[0]], n[1:], d.getPointPen())

f.save()

if hasMojo:
    setDefault("glyphViewRoundValues", glyphViewRoundValues)