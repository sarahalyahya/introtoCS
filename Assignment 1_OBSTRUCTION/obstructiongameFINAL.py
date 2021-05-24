import random 
import os

#defining the global variables (for dynamic board)
PLAYERS_NO = 2
ROW_NO = 5
COL_NO = 5
board = []
col_headings = []

#making a list for column headers, for loop to make it dynamic, mapping using ASCII. 
for i in range (65, COL_NO+65 ):
	col_headings.append(chr(i))


#we need to clear the screen before starting
os.system("clear")

#printing the column headers 
col_header = "   "
for col in range(COL_NO):
 	col_header = col_header + col_headings[col] + "   " 
 #print statement is outside the for loop cause otherwise it will continue to re-print. 
print("\n" + (col_header))

#printing top board border
print ( " +" + "---+"*COL_NO)

#appending dots to the board list 
for row in range (ROW_NO):
	row_list = []
	for col in range (COL_NO):
		row_list.append(' . ')
	board.append(row_list)

#printing the board and the | separators
for row in range(ROW_NO):
	print (str(row) + "|", end="") #we type cast bc we cannot add int to string
	for col in range (COL_NO): 
		print(board[row][col] + "|" , end="" )
#printing the bottom border		
	print ("\n"+ " +" +"---+"*COL_NO)

#a list of possible moves to use to check so we avoid errors if someone enters an invalid move. the for loop makes it dynamic. type casting row number to string because user enters a string. 

accepted_moves = []
for row in range (ROW_NO):
	for col in range (COL_NO):
		accepted_moves.append(col_headings[col] + str(row))


 #randomizing picking the first player:
first_turn = random.randint(0,PLAYERS_NO-1)

#assigning checker symbols:
if first_turn == 0 :
	checker = "X"
else:
	checker = "O"


#we need to initialize with a boolean variable on false, and then when it becomes true, the game ends. 
stop = False 

while stop == False :
#another boolean variable that will change to true if the player makes one of the accepted moves through a while loop. 
	valid_move = False 
	while valid_move == False:
		#asking for player's move
		move = input( "Player" + " " + checker + ", please enter your desired move: ")

		#an if statement that checks if the player made a valid entry:
		if move in accepted_moves:  
			col = col_headings.index(move[0]) #we need to enter the col_headings list, because we need to assign the col to an index, 
			#not a letter so we can insert the checker. It's index 0 because the column is the first part of the move, 
			row = int(move[1]) #tyoe casting cause the input is a string

			#now we need to check the validity of entered move i.e. if it is a cell with "." in it, not already occupied. 
			if board[row][col] == ' . ':
				valid_move = True 
				board[row][col] = " " + checker +" "

				for hash_row in range (row-1,row+2): 
					for hash_col in range(col-1,col+2):
				 		if hash_row in range (ROW_NO) and hash_col in range(COL_NO): #we check the range. If it is a corner checker, we dont want the hashes to be inserted into negative indices
				 			if board[hash_row][hash_col] == ' . ':
				 				board[hash_row][hash_col] = " # "

				#clearing the screen 					
				os.system("clear")

				#reprinting the board
				col_header = "   "
				for col in range(COL_NO):
 					col_header = col_header + col_headings[col] + "   "
				print("\n" + (col_header))

				print ( " +" + "---+"*COL_NO)

				for row in range(ROW_NO):
					print (str(row) + "|", end="")
					for col in range (COL_NO): 
						print(board[row][col] + "|" , end="" )

					print ("\n"+ " +" +"---+"*COL_NO)

				free_cell = False  #boolean variable to check free cells. if it changes to true, it will exit the checking loop, and go back to the game. 
				for row in range (ROW_NO):
					for col in range (COL_NO):
						if board[row][col] == ' . ':
							free_cell = True #here, it found an empty space, so we change the variable to true to alter initial condition and continue the game.


				if free_cell == False: #here no empty spaces were found, so the if condition was not executed. The variable is changed to false which indicates no empty spaces
					print ("Game Over! The winner is " + checker + "!!!")
					stop = True #first boolean variable we introduced is now true so the while loop that includes the game is not executing anymore. game stops. 




			else: 
				print ("Cell is not empty")		 #if someone tries to insert a checker into a cell occupied with a "." or a "#"			
		else:
			print("Invalid Move!") #if someone tries to enter a move not in the accepted moves list. 

	#code to switch between players 		
	if checker == "X":
		checker = "O"
	else:
		checker = "X"




