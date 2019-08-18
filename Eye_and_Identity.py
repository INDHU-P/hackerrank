import numpy
x = input().split(" ")
n1 = int(x[0])
n2 = int(x[1])

print(str(numpy.eye(n1,n2)).replace('1',' 1').replace('0',' 0'))
