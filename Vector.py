class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def plus(self,v):
        new_coordinates = [x+y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def minus(self,v):
        new_coordinates = [x-y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def scalar(self,v):
        new_coordinates = [c*x for x in self.coordinates]
        return Vector(new_coordinates)

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

myVector = Vector([8.218, -9.341])
add = Vector([-1.129, 2.111])
print myVector.plus(add)

myVector = Vector([7.119, 8.215])
minus = Vector([-8.223, 0.878])
print myVector.minus(minus)

myVector3 = Vector([1.671, -1.012, -0.318])
c = 7.41
print myVector3.scalar(c)