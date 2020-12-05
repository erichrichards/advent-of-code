import math

inputFile = open("input03.txt", "r")
fileLines = inputFile.readlines()

inputRows = float(len(fileLines))
inputColumns = float(len(fileLines[0].strip()))

movesRightTuple = (1, 3, 5, 7, 1)
movesDownTuple =  (1, 1, 1, 1, 2)
treeMultProduct = 1

for pos in range(5):
	movesRight = movesRightTuple[pos]
	movesDown = movesDownTuple[pos]

	traveledWidth = (inputRows - 1) * movesRight + 1
	numberOfTesselatedColumns = math.ceil(traveledWidth / inputColumns) - 1
	#numberOfTesselatedColumns = movesRight

	newFileLines = []
	for i in range(int(inputRows)):
		newFileLines.append(fileLines[i].strip() + int(numberOfTesselatedColumns) * fileLines[i].strip())
		#print(fileLines[i].strip() + int(numberOfTesselatedColumns) * fileLines[i].strip())

	countTree = 0
	countOpen = 0
	countOfMoves = 0
	replacementChar = ""

	for j in range(int(inputRows)):
		if movesDown == 1:
			if newFileLines[j][movesRight*j:movesRight*j+1] == ".":
				replacementChar = "O"
				countOpen = countOpen + 1
			elif newFileLines[j][movesRight*j:movesRight*j+1] == "#":
				replacementChar = "X"
				countTree = countTree + 1

			newFileLines[j] = newFileLines[j][:movesRight*j] + replacementChar + newFileLines[j][movesRight*j+1:]
		else:
			if j % movesDown == 0:
				if newFileLines[j][movesRight*countOfMoves:movesRight*countOfMoves+1] == ".":
					replacementChar = "O"
					countOpen = countOpen + 1
				elif newFileLines[j][movesRight*countOfMoves:movesRight*countOfMoves+1] == "#":
					replacementChar = "X"
					countTree = countTree + 1
				newFileLines[j] = newFileLines[j][:movesRight*countOfMoves] + replacementChar + newFileLines[j][movesRight*countOfMoves+1:]
				countOfMoves = countOfMoves + 1
		print(newFileLines[j])

	treeMultProduct = treeMultProduct * countTree
	print("right: {} down: {} trees: {}").format(movesRight,movesDown,countTree)

print("tree mult product: {}").format(treeMultProduct)