# data from Standford edu: http://snap.stanford.edu/data/cit-HepPh.html
from cProfile import label
import csv
# import networkx as nx
from pyvis.network import Network
import matplotlib.pyplot as plt

# reading the data
with open('quakers_nodelist.csv', 'r') as nodecsv: # Open the file
	nodereader = csv.reader(nodecsv)
	nodes = [n for n in nodereader][1:]

node_ids = [n[0] for n in nodes] # Get a list of only the node ids

with open('quakers_edgelist.csv', 'r') as edgecsv: # Open the file
	edgereader = csv.reader(edgecsv)
	edges = [tuple(e) for e in edgereader][4:] # skip first 4 lines

print(node_ids)

# making the Network
net = Network()
net.add_nodes(node_ids, label=node_ids)
net.add_edges(edges)
net.show("quaknodes.html")