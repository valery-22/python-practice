from getpass import getpass as input

print("E P I C 🪨 📜✂️  B A T T L E")
print()
print("Select your move(R , P or S")
print()

player1Move = input("Player 1 >")
print()
player2Move = input("Player 2 >")
print()

if player1Move == "R":
  if player2Move == "R":
    print("You both picked Rock, draw! ")
elif player2Move == "S":
  print("Player1 smashed Player2's scissors into dust with their rock!")
elif player2Move == "P":
  print("Player1's rock is smothered by Player2's paper!")
else:
  print("Invalid Move Player 2!")
if player1Move == "P":
    print("Player1's paper is cut into tiny pieces by Player2's scissors")
elif player2Move == "S":
    print("Player2's rock is smothered by Player1's paper!")
elif player2Move == "P":
    print("Player1's paper is cut into tiny pieces by Player's2 scissors!")
  else:
    print("Invalid Move Playeelse:
print("Invalid Move Player 1!")

