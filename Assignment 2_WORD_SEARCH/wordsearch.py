import random, os


#a function that prints the board
def printBoard():
	os.system("clear")
	print ( " +" + "---+"*DIM)
	for row in range(0,DIM):
		print(" | ", end="")
		for col in range(0,DIM):
			print(board[row][col]+ ' | ', end='')
		print ("\n"+ " +" +"---+"*DIM)

def updateBoard(word):
	#horizontal (L to R)
	row_list = []
	for row in range(DIM):
		row_word="".join(board[row]) #joins columns to make a one dimensional list where each element is the row as a word
		row_word.join(board[row])
		row_list.append(row_word)
	for i in range(len(row_list)):
		start_index = row_list[i].find(word,0,DIM) #it searches for the start index of our desired string
		if start_index != -1: #if it equals -1 it means the word was not found
			for col in range (start_index,start_index+len(word)+1):
				board[i][col] = board[i][col].upper() #here, if it finds the starting index it goes through every column to capitalize it all
		#horizontal (R TO L)		
		else: 
			row_list[i] = row_list[i][::-1] #we reverse the strings to find it in the other direction 
			start_index = row_list[i].find(word,0,DIM)
			if start_index != -1:
				for col in range(DIM-1-start_index,DIM-1-start_index-len(word),-1): #similarly we go through every col
					board[i][col] = board[i][col].upper()
	#vertical (Up to Down)				
	col_list = [] 
	for col in range(DIM):
		col_word = ""
		for row in range(DIM):
			col_word = col_word +(board[row][col])  #same concept we turn all of our columns into "one words" as strings in order to find words among them 
		col_list.append(col_word)
	for i in range(len(col_list)):
		start_index = col_list[i].find(word,0,DIM) #using starting index to find if our word exists vertically
		if start_index != -1:
			for row in range (start_index,len(word)+1+start_index):
				board[row][i] = board[row][i].upper() #iterating through each row to make it in upper case
		#vertical (down to up)		
		else:
			col_list[i] = col_list[i][::-1] #reversing the column strings to find it the other way around
			start_index = col_list[i].find(word,0,DIM)
			if start_index != -1:
				for row in range(DIM-1-start_index,DIM-1-start_index-len(word),-1):
					board[row][i] = board[row][i].upper()

	





		

#a function that checks invalid characters (lowercase letters and numbers), and word lengths.  
def checkInvalid(word):
	for i in range(0, len(word)): 
		if ord(word[i]) not in range(95,123):
			print("Invalid Character")
			return False
		


	if len(word) < 3:
		print("Invalid word")
		return False
	else:
		return True 

	
	
#creating a list of boards so the random function can pick an index to randomize the board size as desired. 
boards=["board_1.csv","board_2.csv","board_3.csv","board_4.csv","board_5.csv",
"board_6.csv","board_7.csv","board_8.csv","board_9.csv",
"board_10.csv","board_11.csv","board_12.csv"]



file = open( boards[random.randint(0,len(boards)-1)] ,"r") #we use the random function to randomly pick one of the provided boards.



#we create a list of the elements in the first line to access the first element which gives us the board dimensions
line1 = file.readline().strip().split(",")

 
DIM = int(line1[0]) #acessing the list element that gives us the dimensions

PLAYERS_NO = 2 #specifing that it's a two player game. 
board = []
accepted_words = [] #initializing empty list to later append to
for i in line1:
	if i not in line1[0] and line1[1]: #we create this for loop to avoid having the first two elements (which are the dimensions) in our accepted words list
		accepted_words.append(i)



#The next for loop apending the letters into our board by creating a board list. 
for line in file:
	line = line.strip().split(",")
	row = []
	for col in line:
		row.append(col)
	board.append(row)

printBoard()

#randomizing picking the first player:
player = random.randint(0,PLAYERS_NO-1)

#two empty lists to use them later for displaying score and progress 
player0_words = []
player1_words = []



#boolean variable to control the game loop
win = False
while not win:
	valid_word = False 

	while not valid_word:

		word = input( "Player " + str(player) + ", please enter a word: ")
		valid_word = checkInvalid(word) #calling the function to check the validity before anything else

		


	if word in accepted_words: #it checks which player picked the correct word and adds it to their list
		if player == 0 :
			player0_words.append(word)
		else:
			player1_words.append(word)
		accepted_words.remove(word)
		os.system("clear")
		updateBoard(word) #calls the function that gives us the uppercase word
		printBoard() #reprints the board with uppercase after cleaning
		print( "Score:")
		print("Player 0: ", len(player0_words) , player0_words)
		print( "Player 1: " , len(player1_words) , player1_words)      #prints the scoreboard with each player's point list
		
			
	else:
		print("Word not found on board") #entering a valid word but a word that isnt available

	if len(accepted_words) == 0: 
		win = True #ending the game by changing the boolean variable (when all the possible words have been chosen)
		if len(player1_words)>len(player0_words):
			print("player 1 wins!")
		elif len(player0_words) > len(player1_words): #determining which player is the winner based on the length of their point list
			print("player 0 wins!")
		else:
			print("It's a tie")

	player = (player+1) % PLAYERS_NO #alternating roles


file.close()

	















