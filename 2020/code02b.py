inputFile = open("input02.txt", "r")

def isLetterAtPosition(position, letter, password):
	if password[position-1:position] == letter:
		return True

countOfMatches = 0

for line in inputFile:
	letterReq = line[line.find(" ")+1:line.find(":")]
	position1 = int(line[:line.find("-")])
	position2 = int(line[line.find("-")+1:line.find(" ")])
	password = line[line.find(": ")+2:].strip()

	if ( isLetterAtPosition(position1, letterReq, password) or isLetterAtPosition(position2, letterReq, password) ) and \
	not ( isLetterAtPosition(position1, letterReq, password) and isLetterAtPosition(position2, letterReq, password) ):
		print('{},{},{},{}').format(letterReq,position1,position2,password)
		countOfMatches = countOfMatches + 1

print(countOfMatches)

