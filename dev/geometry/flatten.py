from services import log
import geometry

REPORT = "Correction angle: {}, axis: {}."


def flatten(objects):  # Type: DocObjects -> Transform
    """
    Solves the inclination correction transform for colection of objects

    This:
        - Sends the objects to a horizontal plane
        - Tranforms around the objects' center of mass
        - Does not project the objects to 2d / retains 3d structure

    args:
        objects (DocObjects): A collection of document objects

    returns:
        Transform: A transform that corrects the inclination
    """

    p = geometry.sample(objects)  # Type: PointCloud

    # Compute correction transform
    correction_angle = geometry.angle(p.normal, geometry.Z)
    correction_axis = geometry.cross(p.normal, geometry.Z)
    correction_matrix = geometry.rotate(correction_angle, correction_axis, p.centroid)

    # Report and verify transform
    log.debug(REPORT.format(correction_angle, correction_axis))
    validate_flatness(correction_matrix, p)

    return correction_matrix


def validate_flatness(correction_matrix, p):  # Type: Transform, PointCloud -> bool
    """
    Invariant: The correction transforms p's normal into the z axis wrt p's centroid
    """

    result = correction_matrix * (p.normal + p.centroid) - p.centroid
    error = result - geometry.Z

    if not error.IsTiny():
        raise Exception(
            "Transform {} failed to correct error. Result: {}, Expected 0,0,1.".format(
                correction_matrix, result
            )
        )
