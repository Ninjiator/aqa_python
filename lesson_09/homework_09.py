class Diamond:
    def __init__(self, side, angle_a):
        self.side = float(side)
        self.angle_a = angle_a
        self.__angle_b = 180.0 - angle_a

    def __setattr__(self, name, value):
        if name == 'side':
            if value <= 0:
                raise AttributeError(f'self.side should be bigger that zero')
            else:
                object.__setattr__(self, name, value)
        elif name == 'angle_a':
            if value <= 0:
                raise AttributeError(f'angle_a should be bigger that zero')
            else:
                object.__setattr__(self, name, value)
                self.__angle_b = 180.0 - self.angle_a
        elif name == '__angle_b' and value + self.angle_a > 180:
            raise AttributeError(f'angle_a + angle_a cannot be > 180')
        else:
            object.__setattr__(self, name, value)

    def __str__(self):
        return f'side is {self.side}, angle_a is {self.angle_a}, angle_b is {self.__angle_b}'


d_1 = Diamond(5, 120)
print('d_1 - ', d_1)
print('-' * 80)
d_2 = Diamond(1, 10)
print('d_2 - ',d_2)
print('-' * 80)
d_2.__angle_b = 180.0
print('d_2 - ', d_2)