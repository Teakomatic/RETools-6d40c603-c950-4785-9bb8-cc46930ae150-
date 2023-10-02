"""
This module contains functions for interacting with Rhino's
document and docobjects.
"""

from scriptcontext import doc
from rhinoscriptsyntax import ObjectType

# Rhino document object types
POINT = 1
CURVE = 4


class DocData:
    pass


class DocObjects:
    def __init__(self, items):
        self.curves = []
        self.points = []
        self.others = []

        for item in items:
            type = ObjectType(item)
            if type == CURVE:
                self.curves.append(item)
            elif type == POINT:
                self.points.append(item)
            else:
                info("Warning: Selected nonstandard geometry")
                self.others.append(item)

    def __nonzero__(self):
        return self.curves or self.points or self.others

    def __iter__(self):
        return iter(self.points + self.curves)

    def delete(self):
        for obj in self.points + self.curves + self.others:
            doc.Objects.Delete(obj)

    @classmethod
    def GetSelected(cls):
        return cls(doc.Objects.GetSelectedObjects(False, False))

    @staticmethod
    def DeselectAll():
        doc.Objects.UnselectAll()

    @staticmethod
    def AddCurve(curve):
        doc.Objects.AddCurve(curve)
    
    @staticmethod
    def AddCircle(circle):
        doc.Objects.AddCircle(circle)
    
    @staticmethod
    def AddLine(line):
        doc.Objects.AddLine(line)
    
    @staticmethod
    def AddPoint(point):
        doc.Objects.AddPoint(point)

AddCurve = doc.Objects.AddCurve
AddCircle = doc.Objects.AddCircle
AddLine = doc.Objects.AddLine
AddPoint = doc.Objects.AddPoint
