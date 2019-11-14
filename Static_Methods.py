from Vectors2d import *


def str_changer(string):
    string.strip()
    string.lstrip('(')
    string.rstrip(')')
    if string.alphnum() or string.replace('.', '').isalphnum():
        if string.isdigit():
            string = int(string)
            component = None
            return string, component
        if '.' in string:
            try:
                string = float(string)
                component = None
                return string, component
            except ValueError:
                pass

        if string[-1] in 'iIxXîÎ':
            string = string.rstrip('iIxXîÎ')
            string, component = str_changer(string)
            component = 'x'
            return string, component
        elif string[-1] in 'jJyYĵĴ':
            string = string.rstrip('jJyYĵĴ')
            string, component = str_changer(string)
            component = 'y'
            return string, component
    if (',' in string) or (' ' in string):
        if ',' in string:
            string = string.split(',')
        else:
            string = string.split()
        if len(string) == 2:
            string[0], temp_cx = str_changer(string[0])
            string[1], temp_cy = str_changer(string[1])
            if temp_cx == 'y' or temp_cy == 'x':
                string[0], string[1] = string[1], string[0]
            component = 'xy'
            return string, component


def operand_optimize(func):
    def common(obj):
        result = []
        if isinstance(obj, Vector2d):
            result = [obj.val['X'], obj.val['Y']]
        elif isinstance(obj, tuple) or isinstance(obj, list):
            if len(obj) == 2:
                for i in obj:
                    if i.isinstance(int) or i.isinstance(float) or i.isinstance(complex):
                        result.append(i)
                    elif i.isinstance(str):
                        temp_obj, component = str_changer(i)
                        if component is None:
                            result.append(temp_obj)
                        elif component == 'x':
                            result = [temp_obj] + result
                        elif component == 'y':
                            result = result + [temp_obj]


