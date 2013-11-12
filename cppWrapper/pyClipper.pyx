
cdef extern from "clipper.hpp" namespace "clipper":
    #enum ClipType { ctIntersection, ctUnion, ctDifference, ctXor };
    cdef enum ClipType:
        ctIntersection=1,
        ctUnion=2,
        ctDifference=3,
        ctXor=4

    #enum PolyType { ptSubject, ptClip };
    cdef enum PolyType:
        ptSubject=1,
        ptClip=2

    #enum PolyFillType { pftEvenOdd, pftNonZero };
    cdef enum PolyFillType:
        pftEvenOdd=1,
        pftNonZero=2,

    ctypedef signed long long long64
    ctypedef char bool

    cdef struct IntPoint:
        long64 X
        long64 Y
        #IntPoint(X, Y)
        #IntPoint(long64 X = 0, long64 Y = 0)
        #IntPoint(long64 x = 0, long64 y = 0): X(x), Y(y) {};
        #friend std::ostream& operator <<(std::ostream &s, IntPoint &p);

    cdef cppclass Polygon:
        Polygon()
        void push_back(IntPoint&)
        IntPoint& operator[](int)
        IntPoint& at(int)
        int size()
    
    cdef cppclass Polygons:
        Polygons()
        Polygon& operator[](int)
        Polygon& at(int)
        int size() 

    cdef cppclass Clipper:
        Clipper()
        #~Clipper()
        bool Execute(ClipType clipType,  Polygons solution,  PolyFillType subjFillType,  PolyFillType clipFillType)
        bool AddPolygon( Polygon pg, PolyType polyType)



_operationMap = {
    "union" : ctUnion,
    "intersection" : ctIntersection,
    "difference" : ctDifference,
    "xor" : ctXor
}

_fillTypeMap = {
    "evenOdd" : pftEvenOdd,
    "noneZero" : pftNonZero,
}

def clipExecute(subjectContours, clipContours, operation, subjectFillType="noneZero", clipFillType="noneZero"):
    cdef Clipper c = Clipper()
    cdef IntPoint a
    cdef Polygon poly
    cdef Polygons solution = Polygons()

    for contour in subjectContours:
        poly = Polygon()
        for point in contour:
            a = IntPoint(point[0], point[1])
            poly.push_back(a)
        c.AddPolygon(poly, ptSubject)

    for contour in clipContours:
        poly = Polygon()
        for point in contour:
            a = IntPoint(point[0], point[1])
            poly.push_back(a)
        c.AddPolygon(poly, ptClip)
    
    c.Execute(_operationMap[operation], solution, _fillTypeMap[subjectFillType], _fillTypeMap[clipFillType])

    pySolution = list()
    for i in range(solution.size()):
        poly = solution[i]
        pySolution.append([])
        for j in range(poly.size()):
            pySolution[-1].append((poly[j].X, poly[j].Y))
    return pySolution
    

    