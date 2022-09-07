"""
Line Smash Command

The command name is defined by the filname minus "_cmd.py"

"""

import Rhino
from scriptcontext import doc

from __plugin__ import version

COMMAND_SUCCESS = 0; COMMAND_CANCEL = 1


def RunCommand( is_interactive ):
    """ Linesmash selected curves.
    """

    print("Linesmash version: " + version)
    
    objects, geometry = get_sel_curves()
    
    if not objects:
        return COMMAND_CANCEL

    line = fit_line(geometry)
    line = deformable_line(line)
    
    [doc.Objects.Delete(o) for o in objects]
    doc.Objects.AddCurve(line)
    
    return COMMAND_SUCCESS


def get_sel_curves():
    """Get currently selected curves
    
       Output:
        objects, geometry: DocObject and resulting geometry
    """
    
    objects = list(doc.Objects.GetSelectedObjects(False,False))
    if not objects:
        print('Please select some curves.')
    geometry = [c.Geometry for c in objects]
    
    #TODO: Filter out points!
    
    return objects, geometry


def fit_line(crvs):
    """Fit line to a set of curves

       Input:
         curves: A list of curve objects

       Output
         (a, b): a pair of line endpoints
    """

    points = sample(crvs)
    
    success, line = Rhino.Geometry.Line.TryFitLineToPoints(points)
    
    if not success:
        raise ValueError("Fit Failure")
    
    return line
  

def sample(crvs):
    """Sample crvs

    Args:
        crvs : an iterable of rhino curve document objects
        
    Result: A list of sample points
    """
    
    DELTA = 0.25
    
    points = []
    
    for curve in crvs:
        points.append(curve.PointAtStart)
    
        for t in curve.DivideByLength(DELTA, False) or []:
            points.append(curve.PointAt(t))
    
        points.append(curve.PointAtEnd)
    
    return points



def deformable_line(line):
    
    EASING_PARAMS = (0, 0.125, 0.5, 0.875, 1)
    
    a, b = line.From, line.To
    
    cvs = ((1-t) * a + t * b for t in EASING_PARAMS)
    
    return Rhino.Geometry.Curve.CreateControlPointCurve(cvs, degree=3)