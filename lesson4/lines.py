from my_packages import point, line


A = point.Point(0, 10)
B = point.Point(10, 0)
C = point.Point(10, 5)
D = point.Point(5, 10)

line1 = line.Line(A, B)
line2 = line.Line(C, D)

print(line1.x_diff(), line1.y_diff())
print(line2.x_diff(), line2.y_diff())

