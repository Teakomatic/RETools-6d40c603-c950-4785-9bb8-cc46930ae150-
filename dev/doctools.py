"""
This module contains functions for interacting with Rhino's
document and docobjects.
"""

from scriptcontext import doc


# Doc Selection -> Docobjects


def GetSelectedCurves():  # Type: None -> Rhino.Doc.DocObject<Curve>[]
    selected_curves = list(doc.Objects.GetSelectedObjects(False, False))
    return selected_curves


# Docobjects -> Doc Deletion


def Delete(doc_objects):  # Type: Rhino.Doc.DocObject[] -> None
    for doc_object in doc_objects:
        doc.Objects.Delete(doc_object)


# Geometry -> Doc
AddCurve = doc.Objects.AddCurve


# Type: Rhino.Geometry.Circle -> Rhino.Doc.DocObject<Circle>
AddCircle = doc.Objects.AddCircle


# Type: Rhino.Geometry.Line -> Rhino.Doc.DocObject<Line>
AddLine = doc.Objects.AddLine


# Docobjects -> Geometry


# Type: Rhino.Doc.DocObject[] -> Rhino.Geometry.Any[]
def Geometry(document_objects):
    """
    Extract the geometry objects from a list of document objects.

    Args:
        curves: Rhino.Doc.DocObject[]. A list of curves to convert to geometry.

    Returns:
        Rhino.Geometry.Any[]. A list of Rhino.Geometry.Curve objects.
    """
    return [
        document_object.Geometry for document_object in document_objects
    ]  # Type: Rhino.Geometry.Any[]
