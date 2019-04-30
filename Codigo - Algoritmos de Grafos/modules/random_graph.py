from random import randint, shuffle, choice
import networkx as nx
import auxiliary as aux
# import draw_graph as dg

def complete_graph(G, v): # Grafo completo
	for i in range(1, v+1):
		for j in range(i+1, v+1):
			G.add_edge(i,j,weight=randint(1,v))
	return G

def connected_graph(G,v): # Grafo não completo mas conexo
	if(v==0): return G
	if(v==1): return G # Casos especiais (1 e 2) 
	if(v==2): # Se são conexos, são sempre completos. No entanto, como utilizo este método
		G.add_edge(list(G)[0],list(G)[1], weight=randint(1,v)) # para auxiliar o desconexo, tenho que criar a exceção (e também
		return G #  deixa este algoritmo mais genérico).
	x = list(G)
	shuffle(x) # Dá um shuffle nos nós (para o caminho não ser sempre do 1 ao 10, certinho)
	e = v*(v-1)/2 - 1 # Conexo não completo
	for i in range(len(x)-1): G.add_edge(x[i],x[i+1], weight=randint(v-2,e)) # Cria um caminho entre todos os nós (para garantir que é conexo)
	for i in range(0,randint(0,v)): # Qtd de nós que vão ter grau >= 1
		on = list(range(0,i))+list(range(i+1,v)) # Outros nós
		for j in range(randint(0,v)): # Qtd de vezes que vai adicionar arestas no nó
			aleat = choice(on) # Escolhe um nó aleatório entre os outros (i.e., diferente do nó x[i])
			if(not G.has_edge(x[i], x[aleat])): G.add_edge(x[i],x[aleat], weight=randint(v-2,e))
	if(G.number_of_edges() == (v*(v-1)/2)): # Se o grafo for completo (raro, mas pode acontecer se todos os randint acima gerarem v)
		v1 = v2 = randint(0,v-1)
		while (v1==v2): v2 = randint(0,v-1)
		G.remove_edge(list(G)[v1],list(G)[v2]) # Remove uma aresta qualquer do grafo completo
	return G

def disconnected_graph(G,v): # Grafo desconexo
	# Criando qtds aleatórias de subconjuntos aleatórios de nós (vértices).
	if(v==1 or v==2): return G
	subGraphs = []
	x = list(G)
	shuffle(x)
	num_of_subsets = randint(2,v)
	for i in range(num_of_subsets):
		sub_i = []
		subGraphs.append(sub_i)
	while(len(x)!=0):
		add = choice(x)
		subGraphs[randint(0,num_of_subsets-1)].append(add)
		x.remove(add)
	resultGraph = nx.Graph()
	temp = nx.Graph()
	for i in range(num_of_subsets):
		temp.clear()
		temp.add_nodes_from(subGraphs[i])
		subG = connected_graph(temp, len(subGraphs[i]))
		resultGraph = nx.compose(resultGraph,subG)
	return resultGraph

def create(v, complete, connected):
	G = nx.Graph()
	for i in range(1,v+1): G.add_node(i)
	if(complete): G = complete_graph(G, v) # COMPLETO <--
	elif(connected): G = connected_graph(G,v) # CONEXO <--
	else: G = disconnected_graph(G,v) # DESCONEXO <--
	return G

def save_file(v,e,G, filename):
	filename = "modules/Grafos/" + filename
	f = open(filename, "w")
	line = "%d %d\n" % (v, e)
	f.write(line)
	for i in G:
		line = "%d %d %d\n" % (i[0], i[1], i[2])
		f.write(line)
	f.write('\n')
	f.close()

def generate(v, complete, connected, filename):
	G = create(v,complete,connected)
	save_file(v,G.number_of_edges(),list(G.edges(data='weight')),filename)
	aux.printc("green", "Grafo salvo em: " + filename)
	aux.press_enter()

	
# dg.draw_graph(G)


