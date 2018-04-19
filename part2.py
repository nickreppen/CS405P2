#Part 2 Solution
#Nicholas Reppen
#CS 505 Project 2
from collections import OrderedDict
import networkx as nx

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
print "Number of nodes", G.number_of_nodes(), "number of edges" , G.number_of_edges()
clique_list = []
clique_list = list(nx.find_cliques_recursive(G))
#print clique_list
cl_l = 0
for cl in clique_list:
        if len(cl) > cl_l:
                cl_l = len(cl)
print "The largest clique size is ", cl_l
final_list = []
for cl in clique_list:
        if len(cl) == cl_l:
                final_list.append(cl)
print "The cliques of size", cl_l, "are: " , final_list
