inputFile = open("Input 01.txt", "r")
inputDict = {}

for line in inputFile:
	inputDict[int(line)] = ''

def brute():
	for val in inputDict:
		for val2 in inputDict:
			for val3 in inputDict:
				if val + val2 + val3 == 2020:
					#print('{} + {} + {} = {}').format(val,val2,val3,val+val2+val3)
					print('{} * {} * {} = {}').format(val,val2,val3,val*val2*val3)
					return

brute()

