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

employee_list = []
for line in content:
	for person in line:
		employee_list.append(person)

employee_list = list(OrderedDict.fromkeys(employee_list))
#print employee_list

for employee in employees_list:
	for line in content:
		if line[0] == employee:
			x=0
