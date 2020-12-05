import pprint

def passportToSingleLines(passport):
	passport = passport.replace("\n"," ")
	return passport

def addKeyCount(passports):
	for i in range(len(passports)):
		passports[i]["cnt"] = len(passports[i].keys())
	return passports

def countValidPassports(passports):
	count = 0
	for i in range(len(passports)):
		if (passports[i]["cnt"] == 8) or (passports[i]["cnt"] == 7 and "cid" not in passports[i]):
			count = count +1
	return count

with open("input04.txt", "r") as inputFile:
	fileData = inputFile.read()

passports = []

for passport in fileData.split("\n\n"):
	passportDict = {}
	passportText = passportToSingleLines(passport)
	for passportField in passportText.split(" "):
		passportFieldKey = passportField.split(":")[0]
		passportFieldVal = passportField.split(":")[1]
		passportDict[passportFieldKey] = passportFieldVal
	passports.append(passportDict)

passports = addKeyCount(passports)

pprint.pprint(passports)
print("\nCount of valid passports: {}\n").format(countValidPassports(passports))
