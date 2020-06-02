'''functions required:
displaying board
turn
win-
    row
    column
    diagonal
tie
'''
print("\t Welcome!" )
print("Here's your initial board, Start playing !")
board=["-","-","-",
       "-","-","-",
       "-","-","-"] #saving the board in form of list elements(empty list)

game_still_going= True
current_player="X"
winner=None

def display_board():
    #assign position to the board
    print(board[0]+ " | "+ board[1] +" | "+ board[2])
    print(board[3]+ " | "+ board[4] +" | "+ board[5])
    print(board[6]+ " | "+ board[7] +" | "+ board[8])

def play_game():
    display_board()
    while game_still_going:
        handle_player(current_player)

        flip_player()
        
        check_if_game_over()
        
        
        
    if winner == "X" or winner == "O":
        print("Wohoo! Congratulations " + winner + " you won")
    else:
        print("Tie :( ")
    

def handle_player(current_player):
    position=int(input("Enter your position:"))-1
    if board[position]=="-":
        board[position]=current_player
        display_board()
    else:
        print("Position already filled")
        handle_player(current_player)
   

def check_if_game_over():
    global winner
    winner=check_if_win()
    check_if_tie()
    
def check_if_win():
    global game_still_going
    row_1 = board[0]==board[1]==board[2]!="-"
    col_1 = board[0]==board[3]==board[6]!="-"
    d_1   = board[0]==board[4]==board[8]!="-"
    row_2 = board[3]==board[4]==board[5]!="-"
    col_2 = board[1]==board[4]==board[7]!="-"
    row_3 = board[6]==board[7]==board[8]!="-"
    col_3 = board[2]==board[5]==board[8]!="-"
    d_2   = board[2]==board[4]==board[6]!="-"
    if row_1 or col_1 or d_1:
        game_still_going=False
        return board[0]
    elif row_2 or col_2:
        game_still_going=False
        return board[1]
    elif row_3 or col_3 or d_2:
        game_still_going=False
        return board[2]
    else:
        winner=None
    return 1;

def flip_player():
    global current_player
    if current_player=="X":
        current_player="O"
    elif current_player=="O":
        current_player="X"
    
    return
def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going=False
play_game()
