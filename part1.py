#Part 1 Solution
#Nicholas Reppen
#CS 505 Project 2
from collections import OrderedDict

#This section reads in the dataset
with open('test.txt') as f:
	content = f.readlines()

content = [x.strip() for x in content]

for line in content[:]:
	if line == '':
		content.remove(line)


#This section will parse the dataset into a usable format for the question
#Data should be in a list of lists
i = 0
for line in content:
	content[i] = line.split()
	i+=1

#This section searches each line for the element 'WOODS' for anyone who sent correspondence to 'WOODS'
#Anyone who sent 'WOODS' an email is the one who could have sent the secrets
suspects = []
for line in content:
	if 'WOODS' in line:
		suspects.append(line[0])
	if 'WOODS' == line[0]:
		for suspect in line:
			suspects.append(suspect)

#We know 'WOODS' is guilty and thus is removed from suspects
#Also remove any duplicates
for suspect in suspects[:]:
	if suspect == 'WOODS':
		suspects.remove(suspect)
suspects = list(OrderedDict.fromkeys(suspects))
print suspects
