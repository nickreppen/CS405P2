#Part 2 Solution
#Nicholas Reppen
#CS 505 Project 2
from collections import OrderedDict
import networkx as nx
#from sets import Set

#Create directed graph G
G = nx.DiGraph()
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

#Create a list of tuples to resemble each edge in our graph
edge_list = []
for line in content:
        for person in line[1:]:
                edge_list.append([line[0],person])
                i+=1
G.add_edges_from(edge_list)
#print "Number of nodes", G.number_of_nodes(), "number of edges" , G.number_of_edges()
print("Number of nodes {} number of edges {}".format(G.number_of_nodes(), G.number_of_edges()))
clique_list = []
clique_list = list(nx.find_cliques_recursive(G))
triangles = []
for cl in clique_list:
        if len(cl) == 3:
              triangles.append(cl) 
common_vertices_counter = 0
butterfly = []
stop  = 0
common_node = 1111
for i in range(len(triangles)):
	#print(triangles[i])
	for j in range(i+1,len(triangles)):
		if stop == 0:
			for k in range(2):
				for l in range(2):
					if triangles[i][k] == triangles[j][l]:
						common_vertices_counter = common_vertices_counter + 1
			if common_vertices_counter == 1:
				print("clique 1: {} clique 2: {}".format(triangles[i],triangles[j]))
				print(set(triangles[i]) | set(triangles[j]))
				butterfly.append(set(triangles[i]) | set(triangles[j]))
				stop = 1
			common_vertices_counter = 0


