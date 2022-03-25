import csv
from operator import itemgetter
import networkx as nx
from networkx.algorithms import community
import matplotlib.pyplot as plt

# reading the data
with open('quakers_nodelist.csv', 'r') as nodecsv: # Open the file
	nodereader = csv.reader(nodecsv) # Read the csv
	nodes = [n for n in nodereader][1:]

node_names = [n[0] for n in nodes] # Get a list of only the node names

with open('quakers_edgelist.csv', 'r') as edgecsv: # Open the file
	edgereader = csv.reader(edgecsv) # Read the csv
	edges = [tuple(e) for e in edgereader][1:] # Retrieve the data

print(len(node_names))
print(len(edges))

# making the graph
graph = nx.Graph()
graph.add_nodes_from(node_names)
graph.add_edges_from(edges)

# print(graph.nodes)
# print(graph.edges)
# print(graph.degree)
nx.draw(graph)
plt.savefig("quakers.png")