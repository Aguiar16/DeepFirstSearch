import auxiliary as aux
import texts as t
import os
import random_graph as rg
import graph_drawing as gd

graph_path = ""
results = []


# INSERÇÃO DE ALGORITMOS:
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# Importe o módulo (python) com seu algoritmo abaixo:
# *Se o algoritmo não estiver em python, deve-se fazer uma integração entre as linguagens. No nosso caso, dfs, fizemos
# por arquivo, isto é, o código em C++ gerava os resultados num arquivo e um módulo em python o lê e retorna.
import dfs

# Insira o nome do seu algoritmo nesta lista, juntamente com os já existentes:
algorithms = ['Busca em Profundidade']

# Insira nesta função, juntamente com os métodos já existentes nela, os resultados 
# do seu método. Siga o modelo especificado:
# if(choice == algorithms[posição do seu algoritmo na lista 'algorithms']): return seu_algoritmo.resultados(graph_path)

def call(choice):
	if(choice == algorithms[0]): return dfs.results(graph_path)

# 												  *** !!!!! IMPORTANTE !!!!! ***

# O retorno de seu algoritmo deve ser um array, onde cada elemento é uma linha de um arquivo de texto.
# as quebras de linha são representadas pelos caracteres \n

# O formato do arquivo de leitura do grafo é constituído de:
# primeira linha: quantidade de vértices e quantidade de arestas, separados por um espaço.
# restante das linhas: vértice a, vértice b e peso da ligação entre eles, também separados por um
# espaço (vértice a e vértice b representam uma aresta).

# A variável graph_path não contém o caminho até o grafo, mas sim o nome do arquivo que contém o 
# grafo. Para ver o formato do arquivo navegue, dentro do programa, até as instruções de "inserir
# algoritmo".

# * O caminho até o grafo é dado por: "modules/Grafos/(o que está na variável graph_path)"
# O caminho até o output, em texto, do seu algoritmo (se tiver) deverá ser em "modules/Resultados/
# (nome do seu output)".
# Explicação: Se faz necessário inserir o "modules" no caminho, uma vez que seu algoritmo será chamado
# a partir da main, a qual se encontra na pasta acima de "modules".


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

def choose_custom(alg):
	x = ""
	graphs = os.listdir("modules/Grafos")
	while (x not in graphs):
		aux.clear_screen()
		t.header(alg)
		print()
		aux.printc("yellow","Grafos encontrados:\n")
		for i in graphs:
			aux.printc("lyellow", i)
		print("")
		x = input("Escolha um grafo (ou exit para voltar): ")
		if(x=="exit"): return ""
		elif(x not in graphs):
			print()
			aux.error_msg(3)
			aux.press_enter()
	return x

def random_menu(alg):
	while True:
		aux.clear_screen()
		t.header(alg)
		print()
		vertex = input("Informe a quantidade de vértices do grafo: ")
		if(not vertex.isdigit()):
			aux.printc("red", "\nPor favor digite um inteiro positivo.")
			aux.press_enter()
			continue
		vertex = int(vertex)
		ans = input("Quer um grafo completo? (s/n): ").lower()
		if(ans != 's' and ans != 'n'):
			aux.printc("red", "\nPor favor digite apenas \'s\' ou \'n\' (sem o \')")
			aux.press_enter()
			continue
		complete = True if ans=='s' else False
		if(complete): connected = True
		else:
			ans = input("O grafo é conexo? (s/n): ").lower()
			if(ans != 's' and ans != 'n'):
				aux.printc("red", "\nPor favor digite apenas \'s\' ou \'n\' (sem o \')")
				aux.press_enter()
				continue
			connected = True if ans=='s' else False
		aux.printc("yellow","\nInforme o nome com o qual deseja salvar o arquivo")
		aux.printc("yellow","que contém o grafo (sem a extensão), ou apenas")
		filename = input("\033[1;33mpressione enter para salvar como \"random.txt\": \033[0m") + ".txt"
		if(filename==".txt"): filename = "random.txt"
		print()
		rg.generate(vertex, complete, connected, filename)
		return filename

def choose_graph(alg):
	error = False
	while True:
		x = t.general_menu(alg, "choose_graph_options", error=error)
		error = False
		if(x=="1"):	return "18vertices.txt"
		elif(x=="2"): return "26vertices.txt"
		elif(x=="3"): return "58vertices.txt"
		elif(x=="4"): return random_menu(alg)
		elif(x=="5"): return choose_custom(alg)
		elif(x=="6"): return ""
		else: error = True	

def show_results(alg):
	aux.clear_screen()
	t.header(alg)
	aux.printc("bwhite", "Resultados:")
	print()
	for i in results:
		print(i,end='')
	print()
	aux.press_enter()

def algorithm_menu(alg):
	global graph_path
	global results
	error = False
	error2 = False
	while True:
		x = t.general_menu(alg, "algorithms_options2", alg, graph_path, error, error2)
		error = False
		error2 = False
		if(x=="1"):
			if(graph_path not in os.listdir("modules/Grafos")): error2=True
			else: 
				results = call(alg)
				show_results(alg)
		elif(x=="2"):
			if(graph_path not in os.listdir("modules/Grafos")): error2=True
			else:
				gd.draw_graph(graph_path)
		elif(x=="3"):
			if len(results)==0:
				aux.printc("red", "Execute o algoritmo primeiro!\n")
				aux.press_enter()
			else: show_results(alg)
		elif(x=="4"): graph_path = choose_graph(alg)
		elif(x=="5"): break
		else: error = True

def run():
	error = False
	while True:
		op = t.general_menu("ALGORITMOS", "algorithms_options", error=error)
		error=False
		if(op not in [str(i) for i in range(1, len(algorithms)+2)]): error=True
		elif(int(op)==len(algorithms)+1): break
		else:
			choice = algorithms[int(op)-1]
			algorithm_menu(choice)