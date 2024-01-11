import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
#import pylab as pl
G=nx.Graph()
G.add_node("A")
G.add_edge("A","C",weight=2)
G.add_edge("A","B",weight=5)
G.add_edge("A","F",weight=8)
G.add_edge("C","K",weight=6)
G.add_edge("B","K",weight=7) 
G.add_edge("B","H",weight=9)
G.add_edge("B","G",weight=10)
G.add_edge("F","G",weight=10)
G.add_edge("G","I",weight=7)
G.add_edge("H","I",weight=6)
G.add_edge("H","K",weight=12)
G.add_edge("H","J",weight=2)
G.add_edge("K","J",weight=12) 
 
pos=nx.spring_layout(G)
nx.draw(G,pos, with_labels=True, font_size=14, font_color="white", font_weight="bold")
nx.draw_networkx_edges(G, pos, width=2.0)
nx.draw_networkx_nodes(G,pos, node_color="red")
labels=nx.get_edge_attributes(G,"weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_weight="bold")
plt.show()

#Algoritmo de Kruskal
T = nx.minimum_spanning_tree(G)
nx.draw(T,pos, with_labels=True, font_size=14, font_color="white", font_weight="bold")

nx.draw_networkx_edges(T, pos, width=2.0)
nx.draw_networkx_nodes(T,pos, node_color="red")
labels=nx.get_edge_attributes(T,"weight")
nx.draw_networkx_edge_labels(T, pos, edge_labels=labels, font_weight="bold")
plt.show()

print("Esta corriendo:")

for vertice in G.nodes:
    print(vertice)