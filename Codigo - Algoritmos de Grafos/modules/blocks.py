from auxiliary import printc

class Blox:
	def __init__(self, brick='#', size=60, color="blue"):
		self.brick = brick
		self.size = size
		self.color = color

	def setBrick(self, brick): self.brick = brick
	def setSize(self, size): self.size = size
	def setColor(self, color): self.color = color
	
	def make_cover(self):
		for i in range(self.size): printc(self.color,self.brick,end='')
		print()
	
	def make_blox(self, phrase=""):
		printc(self.color,self.brick,end='')
		void = int((self.size -2 -len(phrase))/2)
		for i in range(void): printc(self.color, ' ', end='')
		printc(self.color, phrase,end='')
		for i in range(void): printc(self.color, ' ', end='')
		if(len(phrase)%2!=0): printc(self.color, ' ' + self.brick)
		else: printc(self.color, self.brick)

	def make_bloxLeft(self, phrase=""):
		printc(self.color,self.brick,end='')
		void = (self.size -4 -len(phrase))
		printc(self.color, '  ', end='')
		printc(self.color, phrase,end='')
		for i in range(void): printc(self.color, ' ', end='')
		printc(self.color, self.brick)

def normal_blox(text, brick='#', size=60, color="blue", left=False): # Recebe um texto em um array, onde cada elemento é uma linha.
	w = Blox(brick, size, color)						 			 							# Para fazer uma linha em braco, basta colocar um elemento como ''.
	w.make_cover()
	w.make_blox()
	if(left): 
		for i in range(len(text)): w.make_bloxLeft(text[i])
	else: 
		for i in range(len(text)): w.make_blox(text[i])
	w.make_blox()
	w.make_cover()

def options_blox(options, color="blue"):
	for i in range(len(options)):
		printc(color, "  " + options[i])

def header_blox(title, brick='#', size=60, color="blue", header="MENU", headerColor="bwhite"):
	normal_blox(title, brick, size, color)
	w = Blox(' ', size, headerColor)
	w.make_blox("~~~~~~~~ " + header + " ~~~~~~~~")
	print()
