from Rhino.Geometry.Point3d import Origin
from rhinoscriptsyntax import PlaneFitFromPoints


class PointCloud(list):
    @property
    def centroid(self):
        """
        Computes the center of mass of the point cloud

        Returns:
            Point3d: The pointcloud's center mean
        """
        return sum(self, Origin) / len(self)

    @property
    def normal(self):
        """
        Computes the normal of a point cloud.

        Returns:
            Vector3D: The point cloud normal, as a vector in RxRxR^+
        """

        if hasattr(self, "_normal"):
            return self._normal

        # Warning: This may fail and interupt a command.
        # TODO: normalize edge cases and bubble up genuine errors
        self._normal = PlaneFitFromPoints(self).Normal

        # Correct downward facing normals
        if self._normal.Z < 0:
            self._normal.Reverse()

        return self._normal
