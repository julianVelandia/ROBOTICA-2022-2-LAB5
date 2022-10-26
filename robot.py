import math

class PhantomX:

    def joint_publisher(self, points: [[]], is_degree=None):

        for point in points:
            if point[0] == '':
                if menu_while() == 'x':
                    break
                else:
                    continue

            if is_degree is not None:
                point = degrees_to_radians(point)

            print(point)


def menu_while():
    while True:
        key = input('\nSalto de linea '
                    '\n\n  - Pulse x para finalizar '
                    '\n  -Pulse c para continuar\n')
        if key.lower() == 'x' or key.lower() == 'c':
            break
    return key


def degrees_to_radians(degrees: []):
    return list(map(lambda d: (float(d) * math.pi / 180), degrees))
