# Task 4: Rock, Paper, Scissors
# Description:
#  Ask for two players to each enter "rock", "paper" or "scissors".
#  Determine who wins:
# Rock beats scissors
# Scissors beats paper
# Paper beats rock
# If same → “It’s a tie”

# Example:
# Player 1: rock  
# Player 2: scissors  
# Output: Player 1 wins

player1 = input("Player1 enter your choice:" )

player2 = input("Player2 enter your choice:" )


if player1 == "rock" and player2 == "scisser":
    print("player1 wins")
elif player1 == "rock" and player2 == "paper":
    print("player2 wins")
elif player1 == "scissor" and player2 == "rock":
    print("player2 wins")
elif player1 == "scissor" and player2 == "paper":
    print("player1 wins")
elif player1 == "paper" and player2 == "rock":
    print("player1 wins")
elif player1 == "paper" and player2 == "scissor":
    print("player2 wins")
elif player1 == player2:
    print("It's a tie")
else:
    print("Invalid input")

