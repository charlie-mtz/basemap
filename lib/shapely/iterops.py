"""
"""

from ctypes import c_char_p, c_size_t
from shapely.geos import lgeos


def geos_from_geometry(geom):
    data = geom.to_wkb()
    return lgeos.GEOSGeomFromWKB_buf(
                        c_char_p(data),
                        c_size_t(len(data))
                        )

class BinaryPredicateIterator(object):
    
    """A generating non-data descriptor.
    """
   
    fn = None
    context = None

    def __init__(self, fn):
        self.fn = fn

    def __get__(self, obj, objtype=None):
        self.context = obj
        return self

    def __call__(self, geom, iterator, value=True):
        geos_geom = geos_from_geometry(geom)
        for item in iterator:
            try:
                geom, ob = item
            except TypeError:
                geom = item
                ob = geom
            retval = self.fn(geos_geom, geos_from_geometry(geom))
            if retval == 2:
                raise PredicateError, "Failed to evaluate %s" % repr(self.fn)
            elif bool(retval) == value:
                yield ob


# utilities
disjoint = BinaryPredicateIterator(lgeos.GEOSDisjoint)
touches = BinaryPredicateIterator(lgeos.GEOSTouches)
intersects = BinaryPredicateIterator(lgeos.GEOSIntersects)
crosses = BinaryPredicateIterator(lgeos.GEOSCrosses)
within = BinaryPredicateIterator(lgeos.GEOSWithin)
contains = BinaryPredicateIterator(lgeos.GEOSContains)
overlaps = BinaryPredicateIterator(lgeos.GEOSOverlaps)
equals = BinaryPredicateIterator(lgeos.GEOSEquals)
