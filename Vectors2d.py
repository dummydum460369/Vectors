class Vector2d:
    def __init__(self, x=0.0 + 0j, y=0.0 + 0j):
        self.val = {'X': x, 'Y': y}
        Vector2d.system = '2 Dimensional'

    def math_form(self):
        # Returns Rectangular Coordinates in vector format
        return f"{self.val['X']}î+{self.val['Y']}ĵ"

    def add_value(self, x=0, y=0):
        # Increments given x and/or y value to instance
        # Warning! Doesn't return anything
        self.val['X'], self.val['Y'] = self.val['X'] + x, self.val['Y'] + y
        self.val = {'X': self.val['X'], 'Y': self.val['Y']}

    def sum(self, x=0, y=0):
        # Same as add_value but returns the sum as a new instance
        return Vector2d(x=self.val['X'] + x, y=self.val['Y'] + y)

    def add(self, obj):
        # Requires 1 Positional Argument of Vector2d class
        # Adds given object's values to the instance
        # Warning! Doesn't return anything
        self.val['X'] += obj.val['Y']
        self.val['Y'] += obj.val['Y']

    def __add__(self, obj):
        # Requires 1 Positional Argument of Vector2d class
        # Returns Resultant of instance and the given object
        if isinstance(obj, Vector2d):
            return Vector2d(x=self.val['X'] + obj.val['X'], y=self.val['Y'] + obj.val['Y'])
        elif isinstance(obj, tuple) or isinstance(obj, list):
            if len(obj) == 2:
                return Vector2d(x=self.val['X'] + obj[0], y=self.val['Y'] + obj[1])
        elif isinstance(obj, str):
            if ((obj.split()[0][-1] in 'iIxXîÎ') and (obj.split()[1][-1] in 'jJyYĵĴ')) or (
                    (obj.split()[1][-1] in 'iIxXîÎ') and (obj.split()[0][-1] in 'jJyYĵĴ')):
                try:
                    return Vector2d(x=self.val['X'] + float(obj.split()[0][:-1]),
                                    y=self.val['Y'] + float(obj.split()[1][:-1]))
                except TypeError:
                    return Vector2d(x=self.val['X'] + complex(obj.split()[0][:-1]),
                                    y=self.val['Y'] + complex(obj.split()[1][:-1]))
            elif obj.split()[0].isdigit() and obj.split()[1].isdigit():
                return Vector2d(x=self.val['X'] + float(obj.split()[0]), y=self.val['Y'] + float(obj.split()[1]))

    def multiply_scalar(self, scalar):
        # Requires 1 Positional Argument of type number
        # Multiplies given scalar to instance
        # Warning! Doesn't return anything
        self.val['X'] *= scalar
        self.val['Y'] *= scalar

    def scalar_product(self, scalar):
        # Same as multiply_scalar but returns the product as a new instance
        return Vector2d(x=self.val['X'] * scalar, y=self.val['Y'] * scalar)
