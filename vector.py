
# imports
from math import sqrt
'''
Class for vector operations
'''
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

# Calculate magnitue of a list of vectors:
# sum of the sqrt of coordinates squared
    def magnitude(self):
        coordinates_squared = [x**2 for x in self.coordinates]
        return sqrt(sum(coordinates_squared))

# Normalize vectors.
# Mulitiply scalar by magnitude.  Result is 1/magnitude
    def normalized(self):
        try:
            magnitude = self.magnitude
            return self.times_scalar(1./magnitude())

        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector')

#  Add vectors together
    def plus(self, v):
        new_coordinates = [x+y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

# Subtract vectors.  zip up the coordinates, x-y.
    def minus(self, v):
        new_coordinates = [x-y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

# Multipy scalar times x factor (magnitue)
    def times_scalar(self, c):
        new_coordinates = [c*x for x in self.coordinates]
        return Vector(new_coordinates)

# Print coordinates to stdout
    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

# Test equality, return T/F
    def __eq__(self, v):
        return self.coordinates == v.coordinates

## Simple vectors
# my_vector = Vector([1,2,3])
# print(my_vector)
# my_vector2 = Vector([1,2,3])
# my_vector3 = Vector([-1,2,3])
# print(my_vector == my_vector2)
# print(my_vector == my_vector3)

# # Add vectors
# v = Vector([8.218,-9.341])
# w = Vector([-1.129,2.111])
# print(v.plus(w))
#
# # Subtract vectors
# v = Vector([7.199,8.215])
# w = Vector([-8.223,0.878])
# print(v.minus(w))
#
# # Scalar product of a vector
# v = Vector([1.671,-1.012,-0.318])
# c= 7.41
# print(v.times_scalar(c))

# Normalize vectors
v = Vector([-0.221, 7.437])
print(v.magnitude())

v = Vector([8.813, -1.331, -6.247])
print(v.magnitude())

v = Vector([5.581, -2.136])
print(v.normalized())

v = Vector([1.996, 3.108, -4.554])
print(v.normalized())
