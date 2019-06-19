#Shardar Mohammed Quraishi
#UCID: 30045559
#05 Nov 2017
#Assignment 3
#successfully solved all 3 parts of the program


import random
#Introduction to the game and setting up the input
def start_Game():
	print("Welcome to the game of nuts!")
	nuts=int(input("How many nuts are there on the table initially (10-100)? "))
	while(nuts<10 or nuts>100):
		nuts=int(input("Enter a number between 10 and 100: "))
	return nuts
#setting up the options, and asking for which game mode to play
def game_Mode():
	print("Options: ")
	print("Play against a friend (1)")
	print("Play against the computer (2)")
	print("Play against the trained computer (3)")
	game_Option=int(input("Which option do you take (1-3): "))
	while(game_Option<1 or game_Option>3):
		game_Option=int(input("Which option do you take (1-3): "))
	return game_Option
#defining the human vs human function
def player_Vs_Player(nuts):
	while(nuts>0):
		nuts = player_Turn("Player 1", nuts)
		if nuts<=0:
			print("Player 1, you lose.")
			continue
		nuts = player_Turn("Player 2", nuts)
		if nuts<=0:
			print("Player 2, you lose.")
#defining function choosing nuts
def player_Turn(player, nuts):
	print("There are", nuts, "nuts on the board")
	choose_Nuts = int(input(player+": How many nuts do you take? (1-3) "))
	while(choose_Nuts<1 or choose_Nuts>3):
		choose_Nuts = int(input("Choose between 1 and 3 nuts! "))
		continue
	nuts -= choose_Nuts
	return nuts

#initializing hats with nuts
def hats(nuts):
	hats = []
	for i in range (nuts):
		row = [1, 1, 1]
		hats += [row]
	return hats

def makeHatsBeside(nuts):#init hats with beside
	hatsBeside = []
	for i in range (nuts):
		row = [0, 0, 0]
		hatsBeside += [row]
	return hatsBeside

def p_1(nuts,hats):

	for i in s:
		print (s)
		if i == nuts_number:
			return i
			print (i)

def select(p, nuts):#Ai selection

	total = p[0] + p[1] + p[2]
	r_int = random.randint(1, total)
	if r_int <= p[0]:
		move = 0
	elif (r_int <= p[0] + p[1]):
		move = 1
	else:
		move = 2
	return move


def player_Vs_Ai(nuts):
	runGameAi(hats(nuts),nuts)#init hats and send to runGameAI


def runGameAi(hatsContent,nuts):
	originalNuts = nuts
	hatsBeside = makeHatsBeside(nuts)
	while nuts >0:
		nuts = player_Turn("Player 1", nuts)
		if nuts <= 0:
			print("Player 1, you lose.")
			resetKnowledgeBaseAIWon(hatsContent, hatsBeside, originalNuts)
			continueQues(hatsContent,originalNuts)

		move = select(hatsContent[nuts], nuts)
		hatsContent[nuts][move]-=1
		hatsBeside[nuts][move]+=1
		print("Ai picks: ", move+1, "nuts")
		nuts -= (move+1)
		if nuts <= 0:
			print("AI, you lose.")
			resetKnowledgeBaseAILost(hatsContent, hatsBeside, originalNuts)
			continueQues(hatsContent,originalNuts)
#resetting knowledge, throwing away all the balls
def resetKnowledgeBaseAILost(hatsContent, hatsBeside, nuts):
	for i in range(nuts):
		for j in range (0,3):
			hatsContent[i][j] += hatsBeside[i][j]
	return
#updating knowledge base when Ai wins
def resetKnowledgeBaseAIWon(hatsContent, hatsBeside, nuts):
	for i in range(nuts):
		for j in range (0,3):
			if(hatsBeside[i][j] != 0):
				hatsContent[i][j] += (hatsBeside[i][j]+1)
	return

#defining functions for asking question if the palyer wants to play again
def continueQues(hatsContent,originalNuts):
	continueVariable = int(input("Play again (1 = yes, 0 = no)? "))
	if(continueVariable == 1):
		runGameAi(hatsContent,originalNuts)
	else:
		main()


#defing function for human vs trained Ai, and also training the Ai
def player_Vs_trainedAi(nuts):
	print("Training AI... please wait.")
	originalNuts = nuts
	hatsContentAi1 = hats(nuts)
	hatsContentAi2 = hats(nuts)
	hatsBesideAi1 = makeHatsBeside(nuts)
	hatsBesideAi2 = makeHatsBeside(nuts)
#training the Ai by making them play against each other for 100000 times
	for i in range (0,100000):
		nuts = originalNuts

		while nuts > 0:
			move = select(hatsContentAi1[nuts-1], nuts)
			hatsContentAi1[nuts-1][move]-=1 #sub 1 from hatsContent(nuts)[move]
			hatsBesideAi1[nuts-1][move]+=1 #add 1 to hatsBeside(nuts)[move]
			nuts -= (move+1)
			if nuts <= 0:
				resetKnowledgeBaseAILost(hatsContentAi1, hatsBesideAi1, originalNuts)
				resetKnowledgeBaseAIWon(hatsContentAi2, hatsBesideAi2, originalNuts)


			move = select(hatsContentAi2[nuts-1], nuts)
			hatsContentAi2[nuts-1][move]-=1 #sub 1 from hatsContent(nuts)[move]
			hatsBesideAi2[nuts-1][move]+=1 #add 1 to hatsBeside(nuts)[move]
			nuts -= (move+1)
			if nuts <= 0:
				resetKnowledgeBaseAILost(hatsContentAi2, hatsBesideAi2, originalNuts)
				resetKnowledgeBaseAIWon(hatsContentAi1, hatsBesideAi1, originalNuts)
	#training ends here--------------now adding the Knowledgebase of both AI's
	nuts = originalNuts
	for i in range(nuts):
		for j in range (0,3):
			hatsContentAi1[i][j] += hatsContentAi2[i][j]
	print(hatsContentAi1) #print the table contents after training the Ai



	while nuts >0:
		nuts = player_Turn("Player 1", nuts)
		if nuts <= 0:
			print("Player 1, you lose.")
			continueQues(hatsContentAi1,originalNuts)

		move = select(hatsContentAi1[nuts], nuts)
		print("Ai picks: ", move+1, "nuts")
		nuts -= (move+1)
		if nuts <= 0:
			print("AI, you lose.")
			continueQues(hatsContentAi1,originalNuts)

#defining the main function, the programs starts here
def main():
	nuts = start_Game()
	option = game_Mode()
	#player_Vs_trainedAi(nuts)
	#player_Vs_Ai(nuts)
	if(option == 1):
		player_Vs_Player(nuts)
	elif(option == 2):
		player_Vs_Ai(nuts)
	elif(option == 3):
		player_Vs_trainedAi(nuts)
	else:
		print("invalid input")



main()
wn.mainloop()
