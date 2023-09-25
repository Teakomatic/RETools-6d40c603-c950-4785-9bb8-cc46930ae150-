from contextlib import contextmanager

from Rhino.Geometry import BoundingBox
import rhinoscriptsyntax as rs

import points


def silent(command):
    rs.Command(command, False)


"""
Document basics
"""


def save():
    silent("-save enter")


def close():
    silent("exit")


def current_folder():
    return rs.WorkingFolder()


@contextmanager
def no_redraw():
    try:
        silent("setredrawoff")
        yield
    finally:
        silent("setredrawon")


def clear():
    print("Clearing document")
    silent("selall enter delete")


def zoom(pts):
    zoom_box = BoundingBox(pts)
    zoom_box.Inflate(30, 30, 0)
    rs.ZoomBoundingBox(zoom_box)


def zoom_upper_left_close_pair(pts):
    pts = points.Points(pts)
    pts = sorted(pts)
    pts = pts[0], points.nearest_neighbor(pts[0], pts[1:])
    pts = map(points.toPoint3d, pts)
    zoom(pts)
    return pts


def zoom_random_close_pair(pts):
    pts = points.Points(pts)
    pts = points.random_nearest_pair(pts)
    pts = map(points.toPoint3d, pts)
    zoom(pts)
    return pts


"""
Markup
"""


def text(string, height, position):
    x, y = position
    command = '-text Height={height} "{string}" {x},{y}'.format(
        height=height,
        string=string,
        x=x,
        y=y,
    )
    silent(command)


def text_centered(string, height, position):
    silent("-SetCurrentAnnotationStyle Centered")
    text(string, height, position)
    silent("-SetCurrentAnnotationStyle Default")


def text_centered_vertical(string, height, position):
    silent("-SetCurrentAnnotationStyle Centered-Vertical")
    text(string, height, position)
    silent("-SetCurrentAnnotationStyle Default")


"""
Geometry
"""


def guid2geom(guids):
    """Get a list of geometry objects from a list of guids

    Args:
        guids (GuidList): The list of guis to process

    Returns:
        GeomList: The list of geometry objects
    """
    return [rs.rhutil.coercegeometry(guid, False) for guid in guids]


def end_points(curves, tol=0.001):
    """
    Grab the endpoints of open curves
    """
    results = []

    for curve in curves:
        start = rs.CurveStartPoint(curve)
        end = rs.CurveEndPoint(curve)
        distance = start.DistanceTo(end)

        # Add endpoints only if they are distinct (= open curve)
        if distance > tol:
            results += [start, end]

    return results


def bbox(guids):
    """Get a rhino.geometry bbox object

    Args:
        geom_list (Iterable[GuidList]): A iterator of object guids

    Returns:
        Rhino.Geometry.BoundingBox: The input's bounding box
    """
    _bbox = BoundingBox.Empty

    for geom in guid2geom(guids):
        _bbox.Union(geom.GetBoundingBox(accurate=True))

    return _bbox
