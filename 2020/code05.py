def splitRowsRecursively(rows, rowCode, i):
	if len(rows) == 1:
		return rows[0]
	else:
		mid = len(rows) // 2
		if rowCode[i] == "F":
			return splitRowsRecursively(rows[:mid], rowCode, i + 1)
		elif rowCode[i] == "B":
			return splitRowsRecursively(rows[mid:], rowCode, i + 1)

def splitColumnsRecursively(columns, columnCode, j):
	if len(columns) == 1:
		return columns[0]
	else:
		mid = len(columns) // 2
		if columnCode[j] == "L":
			return splitColumnsRecursively(columns[:mid], columnCode, j + 1)
		elif columnCode[j] == "R":
			return splitColumnsRecursively(columns[mid:], columnCode, j + 1)

def findMySeat(seatIdList):
	seatIdList.sort()
	for i in range(0, len(seatIdList)+1):
		if seatIdList[i + 1] == seatIdList[i] + 2:
			return seatIdList[i] + 1

# main
inputFile = open("input05.txt", "r")

rows = range(0, 128)
columns = range(0, 8)
maxSeatId = 0
seatIdList = []

for seatCode in inputFile:
	rowCode = seatCode[:7]
	columnCode = seatCode[7:]

	row = splitRowsRecursively(rows, rowCode, 0)
	column = splitColumnsRecursively(columns, columnCode, 0)
	seatId = row * 8 + column
	seatIdList.append(seatId)

	if seatId > maxSeatId:
		maxSeatId = seatId

	print("{}  {}  {}  {}").format(seatCode.strip(), str(row).rjust(4, " "), str(column).rjust(2, " "), str(seatId).rjust(4, " "))


print("Max Seat ID: {}").format(maxSeatId)
print("My Seat ID: {}").format(findMySeat(seatIdList))