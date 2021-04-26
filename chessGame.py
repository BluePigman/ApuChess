"""This is a chess game in Python, where you play against a computer.
The computer will play random legal moves, so you likely will beat it
with ease. It will first ask you the side you want to play on,
then it will start the game. You type moves by typing the piece you
want to move followed by the square you want to go to (no spaces, no
extra symbols required for captures, for promotions, add the letter
you want to promote to at the end (e.g. g7h8q for queen, e2e4).
The computer will automatically make its move after, and it will print
the move order every time a move is made. 

April 20, 2021
@BluePigman
"""

import chess
import random

board = chess.Board()

board.reset()

def start(): # Choose a side
    while True:
        side = input("Choose side: W (white), B (black)").lower()
        
        if side == "w":
            print("You will play as white")
            return side
        
        if side == "b":
            print("You will play as black")
            return side
            
        else:
            print("Invalid input, please enter"
                 + " either w for white or b for black.")
            continue


def help(): # Help
    resign = "Resign: <resign to end game."
    
def game(): # play game
    userSide = start()
    userQuit = False
    currentMove = "w"
    computerSide = None
    pgn = ""
    moveCount = 1
    increment = 0

    if userSide == "w": # First move, user is white.
        computerSide = "b"
        currentMove = "b"
        while True: 
            startMove = input("You are starting, enter start move: ")

            if startMove.lower() == "resign":
                print("You quit FeelsBadMan")
                userQuit = True
                break
            if len(startMove) != 4: 
                print("Invalid input, should be in format e2e4: " + startMove)
                continue
            if not checkInput(startMove):
                print("Invalid characters inputted: " + startMove)
                continue
            
            move = chess.Move.from_uci(startMove) # Convert to uci
            # Check if the move is legal
            if isLegalMove(move): 
                pgn += str(moveCount) + "." +  get_san(move) + " "
                board.push(move)
                increment += 1
                print(pgn + "\n")
                print(board)
                print()
                break

            else: 
                print("Invalid move, try again: " + startMove)
                continue

    else: # First move, user is black, computer goes first.
        currentMove = "b"
        move = getRandomMove()
        computerSide = "w"
        print("The computer starts with {}".format(move))
        pgn += str(moveCount) + "." +  get_san(move) + " "
        board.push(move) 
        increment += 1
        print(pgn + "\n")
        print(board)
        print()

    while not userQuit: # Remaining moves
        
        if (board.is_checkmate()): #Check for mate
            result = str(board.outcome());
            winner = result[55:]
            if winner[:len(winner) - 1] == "True":
                if userSide == "w":
                    print(board)
                    print("Checkmate, you win! PogChamp" + "\n")
                    print("PGN: " + pgn)
                else:
                    print(board)
                    print("Checkmate, you lose! MaxLOL" + "\n")
                    print("PGN: " + pgn)
            else:
                if userSide == "b":
                    print(board)
                    print("Checkmate, you win! PogChamp" + "\n")
                    print("PGN: " + pgn)
                else:
                    print(board)
                    print("Checkmate, you lose! MaxLOL" + "\n")
                    print("PGN: " + pgn)
            
            break

        if (board.is_stalemate()): #Check for stalemate
            print("Stalemate")
            break

        if (board.is_insufficient_material()): # Check for draw by insufficient material
            print("Draw by insufficient material")
            break


        if currentMove == "w": #White to play
            
            if currentMove == userSide: #User's turn, user makes their move

                while True: # Get move from user
                    moveInput = input("Enter your move: ")
                    print()
                    if moveInput.lower() == "resign":
                        print("You quit FeelsBadMan")
                        userQuit = True
                        break
                    
                    # Check if the move exists.
                    if not(len(moveInput) == 4 or len(moveInput) == 5): 
                        print("Invalid input, should be in format e2e4, " +
                              "for promotions: f7g8q: " + moveInput)
                        continue
                    
                    if not checkInput(moveInput):
                        print("Invalid characters inputted or bad move: "
                              + moveInput)
                        continue
                    
                    if len(moveInput) == 5:
                        if not checkPromotion(moveInput):
                            print("Invalid move: " + moveInput)
                            continue

                    move = chess.Move.from_uci(moveInput) # Convert to uci
                    # Check if the move is legal
                    if isLegalMove(move):
                        
                        # (The chess PGN is always 1. Wmove Bmove 2. Wmove ...)
                        if increment % 2 == 0:
                            moveCount += 1
                            pgn += str(moveCount) + "." +  get_san(move) + " " 
                        else:
                            pgn += get_san(move) + " "
                        board.push(move)
                        increment += 1
                        currentMove = "b" #Black plays next move
                        break

                    else: 
                        print("Invalid move, try again: " + moveInput)
                        continue
                    
            
            else: # Computer makes their move
                move = getRandomMove()
                print("The computer plays {}".format(move) + "\n")
                
                if increment % 2 == 0:
                    moveCount += 1
                    pgn += str(moveCount) + "." +  get_san(move) + " " 
                else:
                    pgn += get_san(move) + " "
                board.push(move)
                increment += 1
                print(pgn + "\n")
                print(board)
                print()
                currentMove = "b" #Black plays next move

            continue
        
        if currentMove == "b":# Black to play
            
            if currentMove == userSide: #User's turn, user makes their move

                while True: # Get move from user
                    moveInput = input("Enter your move: ")
                    print()
                    
                    if moveInput.lower() == "resign":
                        print("You quit FeelsBadMan")
                        userQuit = True
                        break
                        
                    if not(len(moveInput) == 4 or len(moveInput) == 5):
                        print("Invalid input, should be in format e2e4, " +
                              "for promotions: f7g8q: " + moveInput)
                        continue

                    if not checkInput(moveInput):
                        print("Invalid characters inputted: " + moveInput)
                        continue

                    if not checkPromotion(moveInput):
                        print("Invalid move: " + moveInput)
                        continue
                    
                    move = chess.Move.from_uci(moveInput) # Convert to uci
                    # Check if the move is legal
                    if isLegalMove(move):
                        
                        if increment % 2 == 0:
                            moveCount += 1
                            pgn += str(moveCount) + "." +  get_san(move) + " "
                        else:
                            pgn += get_san(move) + " "
                        board.push(move)
                        increment += 1
                        currentMove = "w" #White plays next move
                        break

                    else: 
                        print("Invalid move, try again: " + moveInput)
                        continue    
            
            else: # Computer makes their move
                move = getRandomMove()
                print("The computer plays {}".format(move) + "\n")
                if increment % 2 == 0:
                    moveCount += 1
                    pgn += str(moveCount) + "." +  get_san(move) + " " 
                else:
                    pgn += get_san(move) + " "
                board.push(move)
                increment += 1
                print(pgn + "\n")
                print(board)
                print()
                currentMove = "w" #White plays next move    
        
def getLegalMoves():
    return list(board.legal_moves)

def isLegalMove(move):
    return (move in list(board.legal_moves))

def getRandomMove():
    legal_moves = list(board.legal_moves)
    return random.choice(legal_moves)

def checkInput(move): # Check if a move makes sense (right format)
    numbers = "12345678"
    letters = "abcdefgh"
    
    if move[0] not in letters or move[1] not in numbers:
        return False
    elif move[2] not in letters or move[3] not in numbers:
        return False
    
    return True

def checkPromotion(move): # Check if a promotion move is valid.
    symbols = "bkqr"
    return move[4:] in symbols

"""
Get standard algebraic notation of move (e2e4 becomes e4).
move is a uci representation of move.
"""
def get_san(move):
    return board.san(move)

game()
