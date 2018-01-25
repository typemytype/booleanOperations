import booleanOperations

from mojo.UI import getDefault, setDefault

glyphViewRoundValues = getDefault("glyphViewRoundValues")
setDefault("glyphViewRoundValues", 0)


f = CurrentFont()

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

setDefault("glyphViewRoundValues", glyphViewRoundValues)