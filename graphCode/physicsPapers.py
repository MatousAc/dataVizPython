# data from Standford edu: http://snap.stanford.edu/data/cit-HepPh.html
import csv
import networkx as nx
import matplotlib.pyplot as plt

# reading the data
with open('CitationNodes.txt', 'r') as nodeFile: # Open the file
	nodereader = csv.reader(nodeFile, delimiter="\t")
	nodes = [n for n in nodereader][1:]

node_ids = [n[0] for n in nodes] # Get a list of only the node ids

with open('CitationEdges.txt', 'r') as edgeFile: # Open the file
	edgereader = csv.reader(edgeFile, delimiter="\t")
	edges = [tuple(e) for e in edgereader][4:] # skip first 4 lines

print(len(node_ids))
print(len(edges))

# making the graph
graph = nx.Graph()
graph.add_nodes_from(node_ids)
graph.add_edges_from(edges)

# peeking at the data
# for i in range(0, 10):
# 	print(f"node_ids[{i}] = {node_ids[i]}")

# for i in range(0, 10):
# 	print(f"edges[{i}] = {edges[i]}")
# looks good

nx.draw(graph)
plt.savefig("citations.png")