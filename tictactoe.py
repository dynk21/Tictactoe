from tkinter import*
import random

# This function is called when a player makes a move on the game board.
def next_turn(row, column):

    # Accessing the global variable 'player' which stores the current player's symbol.
    global player

    # Checking if the button at the specified row and column is empty and if there is no winner yet.
    if buttons[row][column]['text'] == "" and check_winner() is False:

        # If the current player is the first player:
        if player == players[0]:

            # Set the text of the button at the specified row and column to the current player's symbol.
            buttons[row][column]['text'] = player

            # If there is no winner after this move:
            if check_winner() is False:
                # Switch to the second player's turn.
                player = players[1]
                # Update the label to indicate the second player's turn.
                label.config(text = (players[1] + " turn"))
            # If the first player wins:
            elif check_winner() is True:
                # Update the label to indicate the first player's win.
                label.config(text = (players[0] + " wins!"))
            # If it's a tie:
            elif check_winner() == "Tie":
                # Update the label to indicate a tie.
                label.config(text = "Tie!")
        else: # If the current player is the second player:

            # Set the text of the button at the specified row and column to the current player's symbol.
            buttons[row][column]['text'] = player

            # If there is no winner after this move:
            if check_winner() is False:
                # Switch to the first player's turn.
                player = players[0]
                # Update the label to indicate the first player's turn.
                label.config(text = (players[0] + " turn"))
            # If the second player wins:
            elif check_winner() is True:
                # Update the label to indicate the second player's win.
                label.config(text = (players[1] + " wins!"))
            # If it's a tie:
            elif check_winner() == "Tie":
                # Update the label to indicate a tie.
                label.config(text = "Tie!")
    
def check_winner():
    
    # Check horizontal winning pattern ➡⬅
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            # Change background color of winning pattern
            buttons[row][0].config(bg = "green", state = "disabled")
            buttons[row][1].config(bg = "green", state = "disabled")
            buttons[row][2].config(bg = "green", state = "disabled")
            return True
    
    # Check vertical winning pattern ⬆⬇
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            # Change background color of winning pattern
            buttons[0][column].config(bg = "green", state = "disabled")
            buttons[1][column].config(bg = "green", state = "disabled")
            buttons[2][column].config(bg = "green", state = "disabled")
            return True
    
    # Check diagonal winning pattern ↘↖
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        # Change background color of winning pattern
        buttons[0][0].config(bg = "green", state = "disabled")
        buttons[1][1].config(bg = "green", state = "disabled")
        buttons[2][2].config(bg = "green", state = "disabled")
        return True
    
    # Check diagonal winning pattern ↗↙
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        # Change background color of winning pattern
        buttons[0][2].config(bg = "green", state = "disabled")
        buttons[1][1].config(bg = "green", state = "disabled")
        buttons[2][0].config(bg = "green", state = "disabled")
        return True
    
    elif empty_spaces is False:

        # Change background color if all spaces are filled and no wins: Tie!
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg = "yellow")
        
        return "Tie"
    else:
        return False

def empty_spaces(): # Check if there is empty spaces remaining
    
    spaces = 9

    # Iteration to count or to check if there is still available spaces in the grid
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1
    
    if spaces == 0:
        return False
    else:
        return True

def new_game(): # Reset game board
    
    global player

    player = random.choice(players)

    label.config(text = player + " turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text = "", bg = "white", state = "normal")

# Game initialization/launch
# Create the main window of the game
window = Tk()
window.title("Tic-Tac-Toe")
players = ["X", "o"]
player = random.choice(players)


# Buttons on the grid
buttons = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

label = Label(text = player + " turn", font = ('consolas', 40))
label.pack(side = "top")
reset_button = Button(text = "Restart", font = ('consolas', 20), command = new_game)
reset_button.pack(side = "top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text = "", font = ('consolas', 40), width = 5, height = 2, command = lambda row = row, column = column: next_turn(row, column))

        buttons[row][column].grid(row = row, column = column)

window.mainloop()