from get_points import read_csv_XY
from robot import PhantomX

if __name__ == '__main__':
    ph = PhantomX()

    # Si read_csv() se envia vacio, ejecuta test.csv
    # joint_publisher recibe is_degree
    ph.joint_publisher()
