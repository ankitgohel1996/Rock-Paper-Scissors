import random

def rules():
	print("Rock paper scissors is a classic 2 player game. Each player chooses either rock, paper or scissors. The possible outcomes:")
	print("Rock destroys scissors.")
	print("Scissors cut paper.")
	print("Paper covers rock.")
	print("")

def playerChoice():
	global player
	player = input("Enter your choice (rock/paper/scissors): ")
	player = player.lower()

	while (player != "rock" and player != "paper" and player != "scissors"):
		print(player)
		player = input("That choice is not valid. Enter your choice (rock/paper/scissors): ")
		player = player.lower()

	print("")

def computerChoice():
	computerInt = random.randint(0,2)

	global computer
	if (computerInt == 0):
		computer = "rock"
	elif (computerInt == 1):
		computer = "paper"
	elif (computerInt == 2):
		computer = "scissors"

def winner():

	global result

	if (player == computer):
		result="Draw!"
		outcome()

		print("SInce it's a draw, please play again.")
		print("")

		playerChoice()
		computerChoice()
		winner()

	elif (player == "rock"):
		if (computer == "paper"):
			result="Computer wins!"
		else:
			result="You win!"

	elif (player == "paper"):
		if (computer == "rock"):
			result="You win!"
		else:
			result="Computer wins!"

	elif (player == "scissors"):
		if (computer == "rock"):
			result="Computer wins!"
		else:
			result="You win!"

def outcome():

	print("Your choice: ", player)
	print("Computer's choice: ", computer)
	print(result)

def scoreCalculate(result):
	global scoreComputer
	global scorePlayer

	if(result== "Computer wins!"):
		scoreComputer+=1
	elif (result=="You win!"):
		scorePlayer+=1

def scoreReturn():
	return (scorePlayer, scoreComputer)


def game():

	choice="yes"
	rules()

	global scoreComputer
	global scorePlayer

	scoreComputer=0
	scorePlayer=0

	while(choice=="yes"):
		playerChoice()
		computerChoice()
		winner()
		outcome()
		scoreCalculate(result)

		choice=input("Do you want to play again? (Yes/No) ")
		choice=choice.lower()
		print("")

		while (choice!="yes" and choice!="no"):
			choice = input("That choice is not valid. Enter again: ")
			choice=choice.lower()

		if(choice=="no"):
			scorePlayer, scoreComputer=scoreReturn()
			print("Thank you for playing! Here are the final results:")
			
			print("Your score is ", scorePlayer)
			print("The computer's score is ", scoreComputer)
			print("")
			
			if(scoreComputer>scorePlayer):
				print("Sorry, the computer wins overall!")
			elif(scorePlayer==scoreComputer):
				print("It's a draw!")
			elif(scoreComputer<scorePlayer):
				print("Congratulations! You win!")
		
game()



