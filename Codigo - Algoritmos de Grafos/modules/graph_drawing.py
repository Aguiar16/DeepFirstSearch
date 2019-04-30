import matplotlib.pyplot as plt
import networkx as nx
import re

def get_graph(graph_path):
	f = open(graph_path,"r+")
	lines = [line for line in f.readlines()]
	f.close()
	G = nx.Graph()
	vertices = int((lines[0].split())[0])
	for i in range(1, vertices+1): G.add_node(i)
	lines = lines[1:-1]
	for i in range(len(lines)):
		lines[i] = lines[i][:-1]
		edge = list(map(int, re.findall('\d+', lines[i])))
		G.add_edge(edge[0],edge[1],weight=edge[2])
	return G

def draw_graph(graph_filename):
	graph_path = "modules/Grafos/" + graph_filename
	G = get_graph(graph_path)
	pos=nx.spring_layout(G)
	nx.draw(G,pos)
	labels = nx.get_edge_attributes(G,'weight')
	nx.draw_networkx_labels(G,pos)
	# nx.draw_networkx_edge_labels(G,pos,edge_labels=labels) # Com os pesos das arestas fica muito feio
	plt.show()
