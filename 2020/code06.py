import pprint
import string

def groupToSingleLine(group):
	group = group.replace("\n"," ")
	return group

def countResponses(groups):
	totalCount = 0
	for group in groups:
		letterCount = 0
		for letter in string.ascii_lowercase:
			if letter in group:
				letterCount = letterCount + 1
		totalCount = totalCount + letterCount
	return totalCount


with open("input06.txt", "r") as inputFile:
	fileData = inputFile.read()

groups = []

for groupResponses in fileData.split("\n\n"):
	groupResponseSet = set()
	groupResponsesLine = groupToSingleLine(groupResponses)
	for personResponse in groupResponsesLine.split(" "):
		for letter in personResponse:
			groupResponseSet.add(letter)
	groups.append(groupResponseSet)

pprint.pprint(groups)
print("Total count: {}").format(countResponses(groups))
