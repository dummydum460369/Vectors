class Vector2d:
    def __init__(self, x=0, y=0):
        self.val = {'X': x, 'Y': y}
        Vector2d.system = '2 Dimensional'

    def math_form(self):
        # Returns Rectangular Coordinates in vector format
        return f"{self.val['X']}î, {self.val['Y']}ĵ"

    def add_value(self, x=0, y=0):
        # Increments given x and/or y value to instance
        # Warning! Doesn't return anything
        self.val['X'], self.val['Y'] = self.val['X'] + x, self.val['Y'] + y
        self.val = {'X': self.val['X'], 'Y': self.val['Y']}

    def add(self, obj):
        # Requires 1 Positional Argument of Vector2d class
        # Adds given object's values to the instance
        # Warning! Doesn't return anything
        self.val['X'] += obj.val['Y']
        self.val['Y'] += obj.val['Y']

    def resultant(self, obj):
        # Requires 1 Positional Argument of Vector2d class
        # Returns Resultant of instance and the given object
        return Vector2d(x=self.val['X'] + obj.val['X'], y=self.val['Y'] + obj.val['Y'])
