from math import *
# A Complex number is a Number, and numbers can be added or multiplied together.
# How numbers can be added or multiplied is abstracted by the method names add and mul
# This class requires that Number objects have add and mul methods, but does not define them.
#  Moreover, it does not have an __init__method.
# The purpose of Number is not to be instantiated directly,
# but instead to server as a superclass of various specific number classes.
# Our next task is to define add and mul appropriately for complex numbers
class Number:
    def __add__(self, other):
        return self.add(other)

    def __mul__(self, other):
        return self.mul(other)

# A complex number can be thought of as a point in two-dimensional space 
# with two orthogonal axes, the real axis and the imaginary axis.
# From this perspective, the complex number c = real + imag * i (where i*i = -1)
# can be thought of as the point in the plane whose horizontal coordinate is real and whose vertical coordinate is imag.
# Adding complex numbers involves adding their respective real and imag coordinates

class Complex(Number): # The Complex class inherits from Number and describes arithmetic for complex numbers.
    def add(self, other):
        return ComplexRI(self.real + other.real, self.imag + other.imag)
    
    def mul(self, other):
        magnitude = self.magnitude * other.magnitude
        return ComplexMA(magnitude, self.angle + other.angle)

# When multiplying complex numbers, it is more natural to think in terms of 
# representing a complex number in polar form, as a magnitude and a angle.
# The product of two complex numbers is the vector obtained by stretching one complex number
# by a factor of the length of the other, and then rotating it through the angle of the other.
class ComplexRI(Complex):
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    @property
    def magnitude(self):
        print('real and imag are not is equal to 0')
        return (self.real**2 + self.imag**2) ** 0.5
    
    @magnitude.setter
    def magnitude(self, new_magnitude):
        if self.real == 0:
            print('real is equal to 0 ')
            return (self.imag**2) ** 0.5
        if self.imag == 0:
            print('imag is equal to 0')
            return (self.real**3) ** 0.5

    @property
    def angle(self):
        return atan2(self.imag, self.real)

    # def conjugate(self):
    #     return 'Conjugate( {0:g}, {1:g} )'.format(self.real, (-1) * self.imag)   

    def conjugate(self):
        self.real = self.real
        self.imag =  (-1) * self.imag

    @property
    def inverse_of_a_complex_number(self):
        real = self.real /(self.real**2 + self.imag**2)
        imag = ((-1)*self.imag) / (self.real**2 + self.imag**2)
        return ComplexRI(real, imag)


    def __repr__(self):
        return 'ComplexRI( {0:g}, {1:g} )'.format(self.real, self.imag)        

class ComplexMA(Complex):
    def __init__(self, magnitude, angle):
        self.magnitude = magnitude
        self.angle = angle
    @property
    def real(self):
        return self.magnitude * cos(self.angle)
    @property
    def imag(self):
        return self.magnitude * sin(self.angle)

    def __repr__(self):
        return 'ComplexMA( {0:g}, {1:g} * pi)'.format(self.magnitude, self.angle/pi)

m = ComplexRI(1, 2) + ComplexMA(2, pi/2)
print(m)
n = ComplexRI(0,1) * ComplexRI(0,1)
print(n)


# Let's say that this class is a part of your program.
# You are modeling a house with a House class
# (at the moment, the class only has a  price instance attribute defined)
class House:
    def __init__(self, price):
        self._price = price
    def hoan(self):
        print('is public')
    def price_0(self):
        return self.hoan
    def price_1(self):
        return self.hoan()

    # Here we have the getter method:
    @property
    def price(self): #
        return self._price # this line is exactly what you would expect in a regular getter.
        # The value of the protected attribute is returned.
        # Here is an example of the use of the getter method:
    # Now we have the setter method:
    # Notice the syntax:

    @price.setter # useed to indicate that this is the setter method for the price property
    def price(self, new_price):
        if new_price > 0 and isinstance(new_price, float):
            self._price = new_price
        else:
            print('Please enter a valid price')
    # Notice how we are not changing the syntax, but now we are using
    # an intermediary(the setter) to validate the argument before assigning it.
    # the new value (45000.0) is passed as an argument to the setter:
    # If we try to assign an invalid value, we see the descriptive message. 
    # we can also check that the value was not updated

    @price.deleter
    def price(self):
        del self._price

# This instance attribute is public because its name doesn't have a leading underscore.
# Since the attribute is currently public, it is very likely that you and other developers
# in your team accessed and modified the attribute directly in other parts of the program 
# using dot notation, like this:














class Student:
    def __init__(self, fname):
        self._fname = fname

    @property
    def fname(self):
        print('Getting fname')
        return self._fname
    
    @fname.setter
    def fname(self, value):
        print('Setting fname to ' + value)
        self._fname = value

    @fname.deleter
    def fname(self):
        print('Deleting fname')
        del self._fname

s = Student('hoan')
print('The fnam is: ', s.fname)
s.fname = 'Millie'
del s.fname



class House2:
    def __init__(self, price):
        self._price = price

    def get_price(self):
        return self._price

    def set_price(self, new_price):
        if new_price > 0 and isinstance(new_price, int):
            self._price = new_price
        else:
            print('never give up')        
    def del_price(self):
        del self._price
    
    x  = property(get_price, set_price, del_price, 'I am the x property.')
