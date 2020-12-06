import pprint
import string

def groupToSingleLine(group):
	group = group.replace("\n"," ")
	return group

def countGroupAlphas(groups):
	count = 0
	for group in groups:
		count = count + len(group)
	return count

with open("input06.txt", "r") as inputFile:
	fileData = inputFile.read()

groups = []
for group in fileData.split("\n\n"):
	group = groupToSingleLine(group)
	groupSet = set()
	for alpha in string.ascii_lowercase:
		alphaCount = 0
		personCount = len(group.split(" "))
		for person in group.split(" "):
			if alpha in person:
				alphaCount = alphaCount + 1
		if alphaCount == personCount:
			groupSet.add(alpha)
	groups.append(groupSet)

pprint.pprint(groups)
print("Total count: {}").format(countGroupAlphas(groups))
