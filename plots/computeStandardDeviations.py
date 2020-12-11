import sys
import math

f = open(sys.argv[1], "r")
g = open(sys.argv[2], "w")

currentSum = 0
variance = 0
values = []

for y in f:
    currentSum += float(y)
    values.append(float(y))

mean = currentSum / 10

for v in values:
    tmp = (float(v) - mean)**2
    variance += tmp

variance /= 10
g.write(str(math.sqrt(variance)))

f.close()
g.close()