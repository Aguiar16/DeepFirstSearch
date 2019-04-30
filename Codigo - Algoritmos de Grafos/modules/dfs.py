import subprocess
import auxiliary as aux

def run(graph_path):
	print("Compilando o código em c++...")
	x = subprocess.getoutput("g++ -std=c++11 modules/deepFirstSearch.cpp -o DFS")
	if(x==""):
		print("Executando o algoritmo...")
		proc = subprocess.Popen(["./DFS", graph_path])
		proc.wait()
		print("Finalizado com sucesso!")

def read_file(results_path):
	print("Gerando os resultados...")
	f = open(results_path,"r+")
	lines = [line for line in f.readlines()]
	f.close()
	return lines

def results(graph_path):
	run(graph_path)
	results_path = "modules/Resultados/" + graph_path[:-4] + "_out.txt"
	report = read_file(results_path)
	print("Tudo pronto!\n")
	aux.press_enter()
	return report

