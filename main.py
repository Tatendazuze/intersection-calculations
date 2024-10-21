#calculate_intersection_to_point_P
import math
y_2 = float(input("enter y coordinate fo point 2:"))
x_2 = float(input("enter x coordinate of point 2:"))
y_1 = float(input("enter y coordinate of point 1:"))
x_1 = float(input("enter x coordinate of point 1:"))
t_1 = float(input("enter direction t1 to P in degrees:"))
t_2 = float(input("enter direction t2 to P in degrees:"))
xp = x_2+((y_2-y_1)-(x_2-x_1)*math.tan((t_1/180)*math.pi)/(math.tan((t_1/180)*math.pi)-math.tan((t_2/180)*math.pi)))
print(f'xp x coordinate: {xp} degrees')
yp = y_2 - (x_2-xp) *math.tan((t_2/180)*math.pi)
print(f'yp y coordinate: {yp} degrees')