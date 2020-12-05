import math

inputFile = open("input03.txt", "r")
fileLines = inputFile.readlines()

inputRows = float(len(fileLines))
inputColumns = float(len(fileLines[0].strip()))

traveledWidth = 1 + 3 * (inputRows -1)
numberOfTesselatedColumns = math.ceil(traveledWidth / inputColumns) - 1

newFileLines = []
for i in range(int(inputRows)):
	newFileLines.append(fileLines[i].strip() + int(numberOfTesselatedColumns) * fileLines[i].strip())
	#print(fileLines[i].strip() + int(numberOfTesselatedColumns) * fileLines[i].strip())

countTree = 0
countOpen = 0

print

for j in range(int(inputRows)):
	if newFileLines[j][3*j:3*j+1] == ".":
		replacementChar = "O"
		countOpen = countOpen + 1
	elif newFileLines[j][3*j:3*j+1] == "#":
		replacementChar = "X"
		countTree = countTree + 1

	newFileLines[j] = newFileLines[j][:3*j] + replacementChar + newFileLines[j][3*j+1:]
	print(newFileLines[j])

print("trees: {}").format(countTree)