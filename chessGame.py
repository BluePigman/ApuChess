"""This is a chess game in python, where you play against a computer.
The computer will play random legal moves, so you likely will beat
with ease. It will first ask you the side you want to play on,
then it will start the game. You type moves by typing the piece you
want to move followed by the square you want to go to (no spaces, no
extra symbols required for captures, for promotions, add the letter
you want to promote to at the end (e.g. g7h8q for queen, e2e4).
The computer will automatically make its move after, and it will print
the move order every time a move is made. 

April 11, 2021
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
                quit()
            if len(startMove) != 4: 
                print("Invalid input, should be in format e2e4: " + startMove)
                continue
            if not checkInput(startMove):
                print("Invalid characters inputted: " + startMove)
                continue
            
            move = chess.Move.from_uci(startMove) # Convert to uci
            # Check if the move is legal
            if isLegalMove(move): 
                board.push(move)
                pgn += str(moveCount) + ". " + chess.Move.uci(move) + " " 
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
        board.push(move)
        pgn += str(moveCount) + ". " + chess.Move.uci(move) + " "  
        increment += 1
        print(pgn + "\n")
        print(board)
        print()

    while True: # Remaining moves
        
        if (board.is_checkmate()): #Check for mate
            result = str(board.outcome());
            winner = result[55:]
            if winner[:len(winner) - 1] == "True":
                if userSide == "w":
                    print("Checkmate, you win! PogChamp")
                else:
                    print("Checkmate, you lose! MaxLOL")
            else:
                if userSide == "b":
                    print("Checkmate, you win! PogChamp")
                else:
                    print("Checkmate, you lose! MaxLOL")
            
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
                        quit()
                        
                    if not(len(moveInput) == 4 or len(moveInput) == 5): 
                        print("Invalid input, should be in format e2e4, " +
                              "for promotions: f7g8q: " + moveInput)
                        continue

                    if not checkInput(moveInput):
                        print("Invalid characters inputted: " + moveInput)
                        continue

                    if not checkPromotion(moveInput):
                        print("Can only promote to b, q, r, k: " + moveInput)
                        continue

                    move = chess.Move.from_uci(moveInput) # Convert to uci
                    # Check if the move is legal
                    if isLegalMove(move):
                        
                        board.push(move)
                        if increment % 2 == 0:
                            moveCount += 1
                            pgn += str(moveCount) + ". " + chess.Move.uci(move) + " " 
                        else:
                            pgn += chess.Move.uci(move) + " "
                        increment += 1
                        currentMove = "b" #Black plays next move
                        break

                    else: 
                        print("Invalid move, try again: " + moveInput)
                        continue
                    
            
            else: # Computer makes their move
                move = getRandomMove()
                print("The computer plays {}".format(move) + "\n")
                board.push(move)
                if increment % 2 == 0:
                    moveCount += 1
                    pgn += str(moveCount) + ". " + chess.Move.uci(move) + " " 
                else:
                    pgn += chess.Move.uci(move) + " "
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
                        quit()
                        
                    if not(len(moveInput) == 4 or len(moveInput) == 5):
                        print("Invalid input, should be in format e2e4, " +
                              "for promotions: f7g8q: " + moveInput)
                        continue

                    if not checkInput(moveInput):
                        print("Invalid characters inputted: " + moveInput)
                        continue

                    if not checkPromotion(moveInput):
                        print("Can only promote to b, q, r, k: " + moveInput)
                        continue
                    
                    move = chess.Move.from_uci(moveInput) # Convert to uci
                    # Check if the move is legal
                    if isLegalMove(move):
                        
                        board.push(move)
                        if increment % 2 == 0:
                            moveCount += 1
                            pgn += str(moveCount) + ". " + chess.Move.uci(move) + " "
                        else:
                            pgn += chess.Move.uci(move) + " "
                        increment += 1
                        currentMove = "w" #White plays next move
                        break

                    else: 
                        print("Invalid move, try again: " + moveInput)
                        continue    
            
            else: # Computer makes their move
                move = getRandomMove()
                print("The computer plays {}".format(move) + "\n")
                board.push(move)
                if increment % 2 == 0:
                    moveCount += 1
                    pgn += str(moveCount) + ". " + chess.Move.uci(move) + " "
                else:
                    pgn += chess.Move.uci(move) + " "
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

def checkInput(move): # Check if a move's squares are on chess board.
    symbols = "12345678abcdefgh"
    for c in move: # Loop through the move string
        if c not in symbols: 
            return False # If any letter is not in symbols, the move is invalid
    return True

def checkPromotion(move): # Check if a promotion move is valid.
    symbols = "bkqr"
    return move[4:] in symbols
game()