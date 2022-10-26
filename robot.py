class PhantomX:

    def joint_publisher(self, points: [[]]):
        for point in points:
            if point[0] == '':
                if menu_while() == 'x':
                    break

            print(point)


def menu_while():
    while True:
        key = input('\nSalto de linea '
                    '\n\n  - Pulse x para finalizar '
                    '\n  -Pulse c para continuar\n')
        if key.lower() == 'x' or key.lower() == 'c':
            break
    return key
