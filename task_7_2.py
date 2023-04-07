class Road:
    __const = 25

    def __int__(self, length, width):
        self._length = length
        self._width = width

    def MassAsphalt(self, thickness):
        result1 = self._length * self._width * self.__const * thickness
        result2 = result1 / 1000
        print(f'Result: {result1} kg = {result2} tonne')


try:
    a = Road()
    x = float(input('Enter the length in meters: '))
    y = float(input('Enter the width in meters: '))
    z = float(input('Enter the thickness in meters: '))
    a.__int__(x, y)
    a.MassAsphalt(z)
except ValueError:
    print('!')
