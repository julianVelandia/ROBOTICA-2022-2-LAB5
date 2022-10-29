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
    with open(file_name, newline='') as File:
        reader = csv.reader(File)
        for row in reader:
            XYZ.append(row)
    for cor in XYZ:
    	x = float(cor[0])
    	y = float(cor[1])
    	z = float(cor[2])
    	L1 = 4
    	L2 = 10.5
    	L3 = 10.5
    	L4 = 9.1
    	d = 8
    	r = math.sqrt(x**2+z**2)
    	a = math.sqrt((L1+d)**2+r**2)-L4
    	
    	q1 = math.atan(y/x)        
    	q2 = math.acos(a/(2*L2))
    	q3 = -math.acos(((a**2)/(2*L2**2))-1)
    	q4 = q2
    	q5 = 1.5
    	
    	response.append([q1,q2,q3,q4,q5])
    
    return response

