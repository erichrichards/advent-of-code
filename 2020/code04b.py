import pprint
import re

def passportToSingleLines(passport):
	passport = passport.replace("\n"," ")
	return passport

def addKeyCount(passports):
	for i in range(len(passports)):
		passports[i]["cnt"] = len(passports[i].keys())
	return passports

def byr(byr):
	if (int(byr) >= 1920 and int(byr) <= 2002):
		return True
	else:
		return False

def iyr(iyr):
	if (int(iyr) >= 2010 and int(iyr) <= 2020):
		return True
	else:
		return False

def eyr(eyr):
	if (int(eyr) >= 2020 and int(eyr) <= 2030):
		return True
	else:
		return False

def hgt(hgt):
	value = int(re.search("^\d*",hgt).group(0))
	unit = re.search("[a-z][a-z]",hgt)
	if unit:
		unit = unit.group(0)
	if unit == "in":
		if (value >= 59 and value <= 76):
			return True
		else:
			return False
	elif unit == "cm":
		if (value >= 150 and value <= 193):
			return True
		else:
			return False
	else:
		return False

def hcl(hcl):
	if hcl[:1] == "#":
		if re.search("[0-9|a-f]*",hcl[1:]):
			return True
	else:
		return False

def ecl(ecl):
	if ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
		return True
	else:
		return False

def pid(pid):
	if (len(pid) == 9 and re.search("[0-9]{9}",pid)):
		return True
	else:
		return False

def countValidPassports(passports):
	count = 0
	goodPassports = []
	for i in range(len(passports)):
		if (passports[i]["cnt"] == 8) or (passports[i]["cnt"] == 7 and "cid" not in passports[i]):
			if(byr(passports[i]["byr"]) and \
				iyr(passports[i]["iyr"]) and \
				eyr(passports[i]["eyr"]) and \
				hgt(passports[i]["hgt"]) and \
				hcl(passports[i]["hcl"]) and \
				ecl(passports[i]["ecl"]) and \
				pid(passports[i]["pid"])):
					goodPassports.append(passports[i])
					count = count +1
	return count, goodPassports


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

pprint.pprint(countValidPassports(passports)[1])
print("\nCount of valid passports: {}\n").format(countValidPassports(passports)[0])
