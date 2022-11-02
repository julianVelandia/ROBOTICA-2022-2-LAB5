import csv
import math

def read_csv_points(file_name=None):
    if file_name is None:
        file_name = 'csv/test.csv'

    response = []
    with open(file_name, newline='') as File:
        reader = csv.reader(File)
        for row in reader:
            response.append(row)

    return response
    
def read_csv_XY():
    file_name = 'csv/test.csv'

    response = []
    Q = []
    with open(file_name, newline='') as File:
        reader = csv.reader(File)
        for row in reader:
            response.append(row)
    for cor in response:
        x = float(cor[0])
        y = float(cor[1])
        z = float(cor[2])
        L1 = 4
        L2 = 10.5
        L3 = 10.5
        L4 = 9.1
        d = 8

        D = math.sqrt(x**2+y**2)
        beta = math.atan((z-L1)/D)
        r = math.sqrt(D**2-z**2)
        cosAlfa = (r-L4)/(2*L2)
        sinAlfa = math.sqrt(1-cosAlfa**2)
        Alfa = math.atan2(sinAlfa,cosAlfa)
        q_1 = math.atan2(y,x)
        q_2 = -(Alfa+beta)
        cosQ3 = ((r-L4)**2/(2*L2**2))-1
        sinQ3 = math.sqrt(1-cosQ3**2)
        q_3 = -math.atan2(sinQ3,cosQ3)
        q_4 = Alfa
        q_5 = math.pi/2
    	
        Q.append([q_1,q_2,q_3,q_4,q_5])
    
    return Q
