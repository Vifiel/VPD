import math
file = open("file.csv")

for i in range(100):
    t = 0.1*i
    s = math.sin(t*2)
    file.write("{}, {}\n".format(t,s))

file.close()
