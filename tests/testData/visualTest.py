# run in DrawBot RoboFont extension
border = 20
dotSize = 10
offDotSize = dotSize * .5

try:
    CurrentFont
except NameError:
    class CurrentFont(dict):

        glyphOrder = []

        def save(self, path=None):
            pass

try:
    saveImage
except NameError:
    def saveImage(*args, **kwargs):
        pass


f = CurrentFont()


def drawOffCurve(anchor, off):
    x, y = anchor
    offx, offy = off
    if offx or offy:
        offx += x
        offy += y
        with savedState():
            stroke(1, 0, 0)
            fill(1, 0, 0)
            line((x, y), (offx, offy))
            oval(offx - offDotSize, offy - offDotSize, offDotSize * 2, offDotSize * 2)


def drawGlyphWithPoints(glyph):
    fill(0, .1)
    stroke(0)
    drawGlyph(glyph)
    stroke(None)

    for contour in glyph:
        fill(0, 1, 0)
        for point in contour.bPoints:
            x, y = point.anchor
            drawOffCurve((x, y), point.bcpIn)
            drawOffCurve((x, y), point.bcpOut)
            oval(x - dotSize, y - dotSize, dotSize * 2, dotSize * 2)
            fill(1, 0, 0)


for glyphName in f.glyphOrder:
    if glyphName not in f:
        continue
    g = f[glyphName]
    bounds = g.bounds
    if not bounds:
        continue
    minx, miny, maxx, maxy = bounds
    w = maxx - minx
    h = maxy - miny
    layerCount = len(f.layers)
    newPage((w + border) * layerCount + border, h  + border * 2 + 100)
    translate(border, border + 100)
    translate(-minx, -miny)
    fontSize(20)
    stroke()
    text("%s" % g.name, (w * .5, -100 + miny), align="center")
    drawGlyphWithPoints(g)
    translate(w + border, 0)
    for layer in f.layers:
        if layer.name == "foreground":
            continue
        fill(0)
        text(layer.name, (w * .5, -100 + miny), align="center")
        if g.name not in layer:
            translate(w + border)
            continue
        lg = layer[g.name]
        drawGlyphWithPoints(lg)
        translate(w + border)


saveImage("visualTest.pdf")