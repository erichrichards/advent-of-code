inputFile = open("Input 01.txt", "r")
inputDict = {}

for line in inputFile:
	inputDict[int(line)] = 2020 - int(line)

for val in inputDict:
	if inputDict[val] in inputDict:
		print('{} * {} = {}').format(val,inputDict[val],val*inputDict[val])
		break