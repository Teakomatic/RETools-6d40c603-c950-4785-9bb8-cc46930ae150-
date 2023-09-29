"""
Zoom to next fillet in the document.

Algorithm:
    1. Get all curves on the "Final" layer
    2. Find all endpoints of those curves
    3. Select a random endpoint
    4. Find the neartest endpoint
    5. Zoom to both endpoints
"""

import Rhino
from scriptcontext import doc
import rhinoscriptsyntax as rs
from Rhino.DocObjects import CurveObject
import rhino

from command import SUCCESS
from services.log import info

# Layer name to scan for geometry
LAYER = "Final"
MODE = "random"
def layer_curves(layer_name):
    """Return all curves on a layer."""
    layer_objects = doc.Objects.FindByLayer(layer_name)
    if not layer_objects:
        return []
    return [crv for crv in layer_objects if isinstance(crv, CurveObject)]

def RunCommand(is_interactive):
    curves = layer_curves(LAYER)
    end_points = rhino.end_points(curves)
    pairs_estimated = len(end_points)/2
    
    if not end_points:
        info("No endpoints found. Nothing to do!")
        return SUCCESS

    info("Fillets left: {}".format(pairs_estimated))

    if MODE == "random":
        rhino.zoom_random_close_pair(end_points)
    
    if MODE == "nearest":
        rhino.zoom_nearest_close_pair(end_points)
    
    if MODE == "lowest_left":
        rhino.zoom_upper_left_close_pair(end_points)

    return SUCCESS
     