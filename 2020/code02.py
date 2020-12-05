inputFile = open("input02.txt", "r")

def countCharInPassword(letterReq, password):
	count = 0
	for i in password:
		if i == letterReq:
			count = count + 1
	return count

countOfMatches = 0

for line in inputFile:
	letterReq = line[line.find(" ")+1:line.find(":")]
	letterMin = int(line[:line.find("-")])
	letterMax = int(line[line.find("-")+1:line.find(" ")])
	password = line[line.find(": ")+2:].strip()

	countOfChar = countCharInPassword(letterReq,password)
	if countOfChar >= letterMin and countOfChar <= letterMax:
		print('{},{},{},{},{}').format(letterReq,letterMin,letterMax,password,countOfChar)
		countOfMatches = countOfMatches +1

print("matches: {}").format(countOfMatches)

