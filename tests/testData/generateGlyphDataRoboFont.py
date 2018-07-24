import booleanOperations
try:
    from mojo.UI import getDefault, setDefault
    hasMojo = True
except ImportError:
    hasMojo = False

try:
    CurrentFont
except NameError:
    class CurrentFont(dict):

        def save(self, path=None):
            pass


f = CurrentFont()

if hasMojo:
    glyphViewRoundValues = getDefault("glyphViewRoundValues")
    setDefault("glyphViewRoundValues", 0)


for g in f:
    g.leftMargin = 0
    g.rightMargin = 0
    n = g.naked()    
    d = g.getLayer("union")
    d.clear()
    d.appendGlyph(g)
    d.removeOverlap(round=0)

    if len(g) > 1:
        for method in "xor", "difference", "intersection":            
            d = g.getLayer(method)     
            d.clear()
            func = getattr(booleanOperations, method)
            func([n[0]], n[1:], d.getPointPen())

    f.save()

if hasMojo:
    setDefault("glyphViewRoundValues", glyphViewRoundValues)