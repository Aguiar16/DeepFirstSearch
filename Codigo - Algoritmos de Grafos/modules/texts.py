import blocks as b
import auxiliary as aux
import algorithms as a

def header(head="MENU"):
	title = [
		"Trabalho de Grafos",
		"",
		"Equipe (Nome Temporário)",
		]
	b.header_blox(title, header=head, color="cyan")

def algorithms_options():
	options = []
	i = 1
	for alg in a.algorithms:
		options.append(str(i)+". "+alg)
		options.append("")
		i+=1
	options.append(str(i)+". Voltar")
	b.options_blox(options, "yellow")
	cursor_up = len(options)+1
	return cursor_up

def algorithms_options2(alg, graph):
	graph = "Nenhum" if graph=="" else graph
	aux.printc("cyan", "Grafo escolhido: \033[1;35m" + graph)
	print()
	options = [
			"1. Executar " + alg, "",
			"2. Visualizar grafo", "",
			"3. Visualizar resultados", "",
			"4. Escolher um Grafo", "",
			"5. Voltar"
		]
	b.options_blox(options, "yellow")
	cursor_up = len(options)+3 # Caso especial de cursor up
	return cursor_up

def main_options():
	options = [
		"1. Iniciar", "",
		"2. Música (Parar/Tocar)", "",
		"3. Instruções", "",
		"4. Créditos", "", 
		"5. Sair"
		]
	b.options_blox(options, "yellow")
	cursor_up = len(options)+1
	return cursor_up

def choose_graph_options():
	options = [
		"1. 18 Vértices", "",
		"2. 26 Vértices", "",
		"3. 58 Vértices", "",
		"4. Gerar grafo aleatório", "",
		"5. Escolher grafo manualmente", "",
		"6. Voltar"
	]
	b.options_blox(options, "yellow")
	cursor_up = len(options)+1
	return cursor_up

def instructions_options():
	options = [
			"1. Como utilizar o programa", "",
			"2. Como adicionar grafos personalizados", "",
			"3. Como inserir novos algoritmos", "",
			"4. Voltar"
		]
	b.options_blox(options, "yellow")
	cursor_up = len(options)+1
	return cursor_up

def call_options(options, alg="", graph=""):
	if(options=="algorithms_options"): return algorithms_options()
	elif(options=="algorithms_options2"): return algorithms_options2(alg, graph)
	elif(options=="main_options"): return main_options()
	elif(options=="choose_graph_options"): return choose_graph_options()
	elif(options=="instructions_options"): return instructions_options()

# Obs: O cursor_up é, contando com o "voltar", sempre: 2*(número de opções - 1) + 2

# Desenha um menu geral (com as opções definidas acima)
# os parâmatros são: (título do cabeçalho, opções do menu, parâmatro específico de um outro menu, nome do grafo, quantidade de cursor up, mensagem de erro, erro 2, número da msg de erro 2)
def general_menu(header_title="MENU", options="main_options", alg="", graph="", error=False, error2=False, error2n=3):
	aux.clear_screen()
	header(header_title)
	if(error): aux.error_msg()
	if(error2): aux.error_msg(error2n)
	print("\n")
	cursor_up = call_options(options, alg, graph)
	aux.cursor_up(cursor_up)
	op = input("Escolha uma opção: ")
	aux.clear_screen()
	return op

def credits():
	aux.clear_screen()
	text = [
		"UECE - Universidade Estadual do Ceará",
		"Curso de Ciência da Computação",
		"Disciplina de Teoria dos Grafos",
		"",
		"Docente:",
		"Mestra Camila Campos Colares das Dores",
		"",
		"Discentes:",
		"Gabriel Furtado Lins Melo",
		"José Gabriel Uchoa Holanda",
		"Lucas Almeida Aguiar",
		"Vinicius Amaro Sampaio",
		"",
		"Linguagens de Desenvolvimento:",
		"Python 3",
		"C++",
		]
	b.normal_blox(text,size=74,color="white")
	print()
	aux.press_enter()
	aux.clear_screen()

def instruction1():
	aux.clear_screen()
	text = [
		"Como utilizar o programa:", "",
		"   Escolha a opção \"Iniciar\", então escolha o algoritmo que deseja",
		"   executar. ", "",
		"   Após isto, escolha o grafo no qual deseja usar o algoritmo.", "",
		"   Por fim, escolha a opção \"Executar\".", "",
		"   Para visualizar os resultados novamente escolha \"Visualizar ",
		"   resultados\".", "",
		"   Se desejar visualizar o grafo escolha \"Visualizar grafo\"."
	]
	b.normal_blox(text,"@",76,"white",True)
	print()
	aux.press_enter()
	aux.clear_screen()

def instruction2():
	aux.clear_screen()
	text = [
		"Como adicionar grafos personalizados:", "",
		"-> Grafos personalizados:", "",
		"   O arquivo de grafo tem extensão \".txt\" e suas linhas devem",
		"   conter o seguinte formato:",
		"   > Primeira linha - número de vértices e de arestas, nesta ordem e",
		"   separados por um espaço", 
		"   > Linhas seguintes - primeiro vértice, segundo vértice e peso (ou",
		"   distância) da aresta, nesta ordem e separados por um espaço.","",
		"-> Inserir / Remover os arquivos personalizados:", "",
		"   Os arquivos estão localizados no caminho \"~/modules/Grafos\"."
	]
	b.normal_blox(text,"@",76,"white",True)
	print()
	aux.press_enter()
	aux.clear_screen()

def instruction3():
	aux.clear_screen()
	text = [
		"Como inserir novos algoritmos:", "",
		"-> Inserindo em código:", "",
		"   O módulo com seu código deve estar na pasta \"~/modules\".",
		"   Abra o arquivo \"algorithms.py\" e, na sessão indicada por",
		"   comentários no código, insira as informações e o algoritmo",
		"   nos devidos locais instruídos. Bem como, deve-se importar",
		"   um módulo em python, com seu algoritmo, no local indicado.",
		"   Caso seu algoritmo não esteja em python, deve-se realizar ",
		"   uma interação entre as linguagens. Isto foi feito para nosso",
		"   algoritmo (dfs) e pode ser visualizado no arquivo \"dfs.py\".", "",
		"-> Formato dos retorno dos resultados:", "",
		"   Os resultados retornados pelo módulo em python devem estar",
		"   em um array, onde cada elemento é uma linha, terminada por",
		"   \"\\n\", se quiser ter uma quebra de linha. Recomendamos que",
		"   se leve em conta o tamanho do terminal na escritura dos",
		"   resultados. Uma maneira fácil de fazer isto é escrevendo os ",
		"   resultados em um arquivo de texto, com a formatação de seu",
		"   gosto, e ler as linhas do arquivo para um array. O que também",
		"   foi feito no módulo \"dfs.py\"."
	]
	b.normal_blox(text,"@",76,"white",True)
	print()
	aux.press_enter()
	aux.clear_screen()