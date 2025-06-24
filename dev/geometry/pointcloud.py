import geometry
from services import log

class PointCloud(list):

    @property
    def centroid(self):
        """
        Computes the center of mass of the point cloud

        Returns:
            Point3d: The pointcloud's center mean
        """
        # Compute point cloud average
        return sum(self, geometry.Origin) / len(self)

    @property
    def normal(self):
        """
        Computes the normal of a point cloud.

        Returns:
            Vector3D: The point cloud normal, as a vector in RxRxR^+
        """

        # Compute normal
        plane = geometry.fit_plane(self)  # TODO: handle errors
        normal = plane.Normal

        if not normal.IsUnitVector:
            log.warning("Generated non-unit normal: {}. Unitizing.".format(normal))
            normal.Unitize()

        # Correct downward facing normals
        if normal.Z < 0:
            normal.Reverse()

        return normal
