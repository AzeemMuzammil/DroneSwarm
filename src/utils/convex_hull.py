import math


class ConvexHull:
    def _neighbors(self, coord):
        for dir in (1, 0):
            for delta in (-1, 1):
                yield (coord[0]+dir*delta, coord[1]+(1-dir)*delta)

    def _get_angle(self, dir1, dir2):
        angle = math.acos(dir1[0] * dir2[0] + dir1[1] * dir2[1])
        cross = dir1[1] * dir2[0] - dir1[0] * dir2[1]
        if cross > 0:
            angle = -angle
        return angle

    def trace(self, p):
        if len(p) <= 1:
            return p

        # start at top left-most point
        pt0 = min(p, key=lambda t: (t[1], t[0]))
        dir = (0, -1)
        pt = pt0
        outline = [pt0]
        while True:
            pt_next = None
            angle_next = 10  # dummy value to be replaced
            dir_next = None

            # find leftmost neighbor
            for n in self._neighbors(pt):
                if n in p:
                    dir2 = (n[0]-pt[0], n[1]-pt[1])
                    angle = self._get_angle(dir, dir2)
                    if angle < angle_next:
                        pt_next = n
                        angle_next = angle
                        dir_next = dir2
            if angle_next != 0:
                outline.append(pt_next)
            else:
                # previous point was unnecessary
                outline[-1] = pt_next
            if pt_next == pt0:
                return outline[:-1]
            pt = pt_next
            dir = dir_next


# polygon_tiles = [(1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (5, 3), (5, 4), (4, 4), (3, 4), (2, 4), (1, 4), (1, 3)]
# outline = trace(polygon_tiles)
# print(outline)
