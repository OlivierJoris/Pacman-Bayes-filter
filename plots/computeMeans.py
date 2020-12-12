import sys

f = open(sys.argv[1], "r")
g = open(sys.argv[2], "w")

currentSum = 0

for y in f:
    currentSum += float(y)

g.write(str(currentSum / 10))

f.close()
g.close()
