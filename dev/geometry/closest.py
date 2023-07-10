def closest(self, other):
    return min(
        [(a, b) for a in self for b in other],
        key=lambda ab: ab[0].DistanceToSquared(ab[1]),
    )
