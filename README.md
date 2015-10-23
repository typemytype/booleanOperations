BooleanOperations
=================

Boolean operations on paths based on a super fast [polygon clipper library by Angus Johnson](http://www.angusj.com/delphi/clipper.php).

You can download the latest version from:

<https://github.com/typemytype/booleanOperations/releases/latest>.

Install
-------

[Pip](https://pip.pypa.io/en/stable/) is the recommended tool to download and install booleanOperations.

If your Python doesn't come with pip pre-installed, you can install it by downloading the official [get-pip.py](https://bootstrap.pypa.io/get-pip.py), and running it as a normal script:

```
python get-pip.py
```

To install the booleanOperations package with pip, you do:

```
pip install --find-links https://github.com/typemytype/booleanOperations/releases/latest booleanOperations
```

Pip will first try to download the Python [wheel](http://pythonwheels.com/) archive that was compiled for your platform and Python version.

For the current version, wheels are only available for **Python 2.7** on **OS X** (10.6 and above) and **Windows** (32-bit).

If the wheel isn't available, pip will attempt to compile the package from the source distribution (`.tar.gz` or `.zip`).

Build
-----

The included `setup.py` file operates in one of two modes depending on the presence/absence of an empty file named `dev` in the project root directory.

When the file is present, as in the Github repository, then [Cython](http://cython.org/) is required in order to convert the `.pyx` files to `.cpp`.

In the source distributions this 'dev' file is missing, and pre-generated `.cpp` files are present instead.

This mechanism allows source distributions to be installed on systems which don't have Cython, or have a different versions (the idea comes from <https://github.com/MattShannon/bandmat>).

In both cases a C++ compiler is needed to build the Python extension module.

For example, to compile it in the same location as the Python sources:

```
python setup.py build_ext --inplace
```

BooleanOperationManager
-----------------------

Containing a `BooleanOperationManager` handling all boolean operations on paths. Paths must be similar to `defcon`, `robofab` contours. A manager draws the result in a `pointPen`.

    from booleanOperations import BooleanOperationManager
    
    manager = BooleanOperationManager()

    
### BooleanOperationManager()

Create a `BooleanOperationManager`.

#### manager.union(contours, pointPen)

Performs a union on all `contours` and draw it in the `pointPen`.
(this is a what a remove overlaps does)

#### manager.difference(contours, clipContours, pointPen)

Knock out the `clipContours` from the `contours` and draw it in the `pointPen`.

#### manager.intersection(contours, clipContours, pointPen)

Draw only the overlaps from the `contours` with the `clipContours`and draw it in the `pointPen`.

#### manager.xor(contours, clipContours, pointPen)

Draw only the parts that not overlaps from the `contours` with the `clipContours`and draw it in the `pointPen`.

#### manager.getIntersections(contours)

Returning all intersection for the given contours

BooleanGlyph
------------

A glyph like object with boolean powers.

    from booleanOperations.booleanGlyph import BooleanGlyph
    
    booleanGlyph = BooleanGlyph(sourceGlyph)

### BooleanGlyph(sourceGlyph)

Create a `BooleanGlyph` object from `sourceGlyph`. This is a very shallow glyph object with basic support.

#### booleanGlyph.union(other)

Perform a **union** with the `other`. Other must be a glyph or `BooleanGlyph` object.
    
    result = BooleanGlyph(glyph).union(BooleanGlyph(glyph2))
    result = BooleanGlyph(glyph) | BooleanGlyph(glyph2)

#### booleanGlyph.difference(other)

Perform a **difference** with the `other`. Other must be a glyph or `BooleanGlyph` object.

    result = BooleanGlyph(glyph).difference(BooleanGlyph(glyph2))
    result = BooleanGlyph(glyph) % BooleanGlyph(glyph2)

#### booleanGlyph.intersection(other)

Perform a **intersection** with the `other`. Other must be a glyph or `BooleanGlyph` object.

    result = BooleanGlyph(glyph).intersection(BooleanGlyph(glyph2))
    result = BooleanGlyph(glyph) & BooleanGlyph(glyph2)

#### booleanGlyph.xor(other)

Perform a **xor** with the `other`. Other must be a glyph or `BooleanGlyph` object.

    result = BooleanGlyph(glyph).xor(BooleanGlyph(glyph2))
    result = BooleanGlyph(glyph) ^ BooleanGlyph(glyph2)

#### booleanGlyph.removeOverlap()

Perform a **union** on it self. This will remove all overlapping contours and self intersecting contours.

    result = BooleanGlyph(glyph).removeOverlap()

----

#### booleanGlyph.name

The **name** of the `sourceGlyph`.

#### booleanGlyph.unicodes

The **unicodes** of the `sourceGlyph`.

#### booleanGlyph.width

The **width** of the `sourceGlyph`.

#### booleanGlyph.lib

The **lib** of the `sourceGlyph`.

#### booleanGlyph.note

The **note** of the `sourceGlyph`.

#### booleanGlyph.contours

List the **contours** of the glyph.

#### booleanGlyph.components

List the **components** of the glyph.

#### booleanGlyph.anchors

List the **anchors** of the glyph.
