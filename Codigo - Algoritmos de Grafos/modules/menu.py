import texts as t
import auxiliary as aux
import vlc
import algorithms as a

sound_path = "modules/sounds/merge.mp3"
p = vlc.MediaPlayer(sound_path)

def pause(state):
	if(state): 
		p.pause()
		return False
	else: 
		p.play()
		return True

def instructions():
	error = False
	while (True):
		op = t.general_menu("Instruções", "instructions_options", error=error)
		error=False
		if(op=="1"): t.instruction1()
		elif(op=="2"): t.instruction2()
		elif(op=="3"): t.instruction3()
		elif(op=="4"): break
		else: error = True

def run():
	sound_state = False
	error = False
	while(True):
		op = t.general_menu(error=error)
		error=False
		if(op=="1"): a.run()
		elif(op=="2"): sound_state = pause(sound_state)
		elif(op=="3"): instructions()
		elif(op=="4"): t.credits()
		elif(op=="5"): break
		else: error=True