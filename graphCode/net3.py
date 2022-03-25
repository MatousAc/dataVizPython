from pyvis import network as net
import networkx as nx

g = net.Network(notebook=True)
nxg = nx.complete_graph(5)
g.from_nx(nxg)
g.show("example.html")