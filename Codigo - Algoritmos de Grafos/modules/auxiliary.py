import os

def cursor_up(num): # Códigos escape ANSI
	CURSOR_UP_ONE = '\x1b[1A'
	ERASE_LINE = '\x1b[2K'
	print(CURSOR_UP_ONE*(num+1), end='')

def cursor_down(num):
	CURSOR_DOWN_ONE = '\x1b[1B'
	print(CURSOR_DOWN_ONE*(num+1), end='')

def clear_screen():
	os.system('cls' if os.name == 'nt' else 'clear')

def press_enter():
	input("\033[1;35mPressione enter para continuar...\033[0m")

def error_msg(msg=1):
	if(msg==1):	printc("red","Opção não reconhecida!\n")
	elif(msg==2): printc("red", "O arquivo não foi encontrado!\n")
	elif(msg==3): printc("red", "Por favor selecione um grafo válido!\n")

def printc(color="white", message="", disable=True, end="\n"):
	red = "\033[1;91m"
	lred = "\033[0;91m"
	gblue = "\033[1;44m"
	blue = "\033[0;96m"
	cyan = "\033[1;36m"
	green = "\033[1;32m"
	bgreen = "\033[0;32m"
	yellow = "\033[1;33m"
	lyellow = "\033[0;33m"
	purple = "\033[1;35m"
	white = "\033[0;37m"
	bwhite = "\033[1;37m"
	endc = '\033[0m'
	if(color=="red"): color = red
	elif(color=="lred"): color = lred
	elif(color=="blue"): color = blue
	elif(color=='gblue'): color = gblue
	elif(color=="cyan"): color = cyan
	elif(color=="green"): color = green
	elif(color=="bgreen"): color = bgreen
	elif(color=="yellow"): color = yellow
	elif(color=="lyellow"): color = lyellow
	elif(color=="purple"): color = purple
	elif(color=="white"): color = white
	elif(color=='bwhite'): color = bwhite
	else:
		print("COLOR DOESN'T EXISTS")
		return
	if(disable):
		print(color + message + endc, end=end)
	else: print(color + message, end=end)

	# para ver as cores e seus números no terminal:
	# for i in range(0, 2):
	#  for j in range(0, 101):
	#   print("\033["+str(i)+";" + str(j) +"m" + str(j) + "\033[0m", end=' ')
	#  
