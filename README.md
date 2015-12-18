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

The extension module is generated using [Cython](http://cython.org/). 

The source distributions already contain a pre-generated `pyClipper.cpp` file, thus only a C++ compiler is required to build the extension module.

Since this file is not stored in the git repository, if you want to build from a cloned repository, you will also need Cython in order to generate the `.cpp` source file.

The `setup.py` script will automatically fetch and install Cython locally (to a temporary "./.eggs" folder) if Cython is not already installed and the pre-generated C++ file is absent.

To compile the module in the same location as the Python sources:

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
