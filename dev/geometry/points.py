import random
import math

from Rhino.Geometry import Point3d


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, p2):
        return Point(self.x + p2.x, self.y + p2.y)

    def __sub__(self, p2):
        return Point(self.x - p2.x, self.y - p2.y)

    def dot(self, p2):
        return self.x * p2.x + self.y * p2.y

    def dist(self, p2):
        diff = self - p2
        return math.sqrt(diff.dot(diff))

    def __eq__(self, p2):
        return self.x == p2.x and self.y == p2.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __lt__(self, other):

        return self.y < other.y or (self.y == other.y and self.x < other.x)


def toPoint3d(point):
    return Point3d(point.x, point.y, 0)


def fromPoint3d(point):
    #    assert(isinstance(point, Point3d))

    return Point(point.X, point.Y)


def Points(points):

    results = []

    for point in points:
        results.append(fromPoint3d(point))

    return results


def horizontal_grid(rows, spacing):
    index = 0

    while True:
        column = index // rows
        row = index % rows
        index += 1
        yield column * spacing, row * spacing


def nearest_neighbor(base_point, points):
    return min(points, key=base_point.dist)


def random_nearest_pair(points):

    points = set(points)
    base_point = random.choice(list(points))
    points.remove(base_point)

    neighbor = nearest_neighbor(base_point, points)

    return base_point, neighbor


def test_random_nearest_neighbor():

    A, B, C = Point(0, 0), Point(1, 0), Point(0, 1)

    point_name = {
        Point(0, 0): "A",
        Point(1, 0): "B",
        Point(0, 1): "C",
    }

    pts = [A, B, C]

    for i in range(1000):

        r1, r2 = random_nearest_pair(pts)

        #        result_name 

        rset = {r1, r2}
        print("Attempt", i, "of", 1000)
        print("Result:", r1, r2)
        print("Result:", point_name[r1], point_name[r2])
        assert A in rset

    print("Success!")

if __name__ == "__main__":

    test_random_nearest_neighbor()
