class Point:
    x_coord = 0
    y_coord = 0

    def __init__(self, x, y):
        if isinstance(x, (int, float)) and isinstance(y, (int, float)):
            self.x_coord = x
            self.y_coord = y
        else:
            raise TypeError("x and y must be of type int or float")

    def __str__(self):
        return f'Point {self.x_coord} {self.y_coord}'

    def __getitem__(self, item):
        print(f'__getitem__ {item}')
        if item == 0:
            return self.x_coord
        elif item == 1:
            return self.y_coord
        else:
            raise TypeError

    def __setitem__(self, item, value):
        print(f'__setitem__ {item}, {value}')
        if item == 0:

            if isinstance(value, (int, float)):
                self.x_coord = value
            else:
                raise TypeError("Value must be of type int or float")
        elif item == 1:

            if isinstance(value, (int, float)):
                self.y_coord = value
            else:
                raise TypeError("Value must be of type int or float")
        else:
            raise TypeError

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x_coord == other.x_coord and self.y_coord == other.y_coord
        else:
            return False

    def distance(self, other):
        if isinstance(other, Point):
            dx = self.x_coord - other.x_coord
            dy = self.y_coord - other.y_coord
            return (dx ** 2 + dy ** 2) ** 0.5
        else:
            raise TypeError("Distance can only be calculated between two points")

p1 = Point(3, 7)
p2 = Point(1, 2)

print(p1[0])
print(p1[1])

p1[1] = 100
print(p1)

class Line:
    begin_point = None
    end_point = None

    def __init__(self, begin, end):
        if isinstance(begin, Point) and isinstance(end, Point):
            self.begin_point = begin
            self.end_point = end
        else:
            raise TypeError("begin and end must be instances of Point")

    def __str__(self):
        return f'Line from [{self.begin_point}] to [{self.end_point}]'

    def length(self):
        k1 = self.begin_point.x_coord - self.end_point.x_coord
        k2 = self.begin_point.y_coord - self.end_point.y_coord

        return (k1 ** 2 + k2 ** 2) ** 0.5

    def __len__(self):
        """ len(obj) """
        return 2

    def __contains__(self, item):
        """ a in b """
        print('__contains__', item)
        return self.begin_point == item or self.end_point == item

line = Line(p1, p2)

print(line)

class Triangle:
    def __init__(self, point1, point2, point3):
        self._point1 = None
        self._point2 = None
        self._point3 = None
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3

    def _validate_point(self, value):
        if not isinstance(value, Point):
            raise TypeError("Point object expected")
        return value

    def _get_point1(self):
        return self._point1

    def _set_point1(self, value):
        self._point1 = self._validate_point(value)

    point1 = property(_get_point1, _set_point1)

    def _get_point2(self):
        return self._point2

    def _set_point2(self, value):
        self._point2 = self._validate_point(value)

    point2 = property(_get_point2, _set_point2)

    def _get_point3(self):
        return self._point3

    def _set_point3(self, value):
        self._point3 = self._validate_point(value)

    point3 = property(_get_point3, _set_point3)

    def area(self):
        a = self._point1.distance(self._point2)
        b = self._point2.distance(self._point3)
        c = self._point3.distance(self._point1)

        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

        return area

    def __iter__(self):
        self._iter_index = 1
        return self

    def __next__(self):
        if self._iter_index == 1:
            self._iter_index += 1
            return self._point1
        elif self._iter_index == 2:
            self._iter_index += 1
            return self._point2
        elif self._iter_index == 3:
            self._iter_index += 1
            return self._point3
        else:
            raise StopIteration

p1 = Point(0, 0)
p2 = Point(3, 0)
p3 = Point(0, 4)

triangle = Triangle(p1, p2, p3)

triangle_area = triangle.area()
print(triangle_area)

for point in triangle:
    print(point)