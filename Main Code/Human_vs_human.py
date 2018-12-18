from utils import printBoard, isMill, numOfPieces, adjacentLocations, possibleMoves_stage2or3
import sys


def HUMAN_V_HUMAN():
    board = []
    for i in range(24):
        board.append('x')

    printBoard(board)
    for i in range(9):
        # FOR PLAYER 1, STAGE 1

        finished1 = False
        while not finished1:
            try:
                pos1 = int(input("\n PLAYER 1: Place a piece '1': "))
                print()
                if pos1 == 99:
                    sys.exit()
                if board[pos1] == 'x':
                    board[pos1] = '1'
                    if isMill(pos1, board):
                        itemPlaced = False
                        while not itemPlaced:
                            try:
                                pos2 = int(
                                    input('\nA Mill is formed.\nRemove a 2 piece: '))
                                if board[pos2] == '2' and not isMill(pos2, board) or (isMill(pos2, board) and numOfPieces(board, '1') == 3):
                                    board[pos2] = 'x'
                                    itemPlaced = True
                                else:
                                    print("Invalid Position! Try again!")
                            except Exception as e:
                                print("Input out of bounds")
                                print(str(e))

                    finished1 = True

                else:
                    print("There is already a piece in position %d !", pos1)
            except Exception as e:
                print("Couldn't get the input value!")
                print(str(e))

        printBoard(board)

        # FOR PLAYER 2, STAGE 1

        finished2 = False
        while not finished2:
            try:
                pos1 = int(input("\n PLAYER 2: Place a piece '2': "))
                print()
                if pos1 == 99:
                    sys.exit()
                if board[pos1] == 'x':
                    board[pos1] = '2'
                    if isMill(pos1, board):
                        itemPlaced = False
                        while not itemPlaced:
                            try:
                                pos2 = int(
                                    input('\nA Mill is formed.\nRemove a 1 piece: '))
                                if board[pos2] == '1' and not isMill(pos2, board) or (isMill(pos2, board) and numOfPieces(board, '2') == 3):
                                    board[pos2] = 'x'
                                    itemPlaced = True
                                else:
                                    print("Invalid Position! Try again!")
                            except Exception as e:
                                print("Input out of bounds")
                                print(str(e))

                    finished2 = True

                else:
                    print("There is already a piece in position %d !", pos1)
            except Exception as e:
                print("Couldn't get the input value!")
                print(str(e))

        printBoard(board)

    print('\n')
    print("STAGE 2")
    print('\n')

    while True:

        # PLAYER 1 STAGE 1 MOVE

        printBoard(board)
        userMoved = False
        while not userMoved:
            try:
                movable = False

                if numOfPieces(board, '1') == 3:
                    only3 = True
                else:
                    only3 = False

                while not movable:
                    pos1 = int(
                        input("\nPLAYER 1: Which '1' piece will you move?: "))

                    while board[pos1] != '1':
                        print("Invalid. Try again.")
                        pos1 = int(
                            input("\nPLAYER 1: Which '1' piece will you move?: "))

                    if only3:
                        movable = True
                        print("Stage 3 for Player 1. Allowed to Fly")
                        break

                    possibleMoves = adjacentLocations(pos1)

                    for adjpos in possibleMoves:
                        if board[adjpos] == 'x':
                            movable = True
                            break
                    if movable == False:
                        print("No empty adjacent pieces!")

                userPlaced = False

                while not userPlaced:
                    newpos1 = int(input("'1' New Position is : "))

                    if newpos1 in adjacentLocations(pos1) or only3:

                        if board[newpos1] == 'x':
                            board[pos1] = 'x'
                            board[newpos1] = '1'

                            if isMill(newpos1, board):
                                userRemoved = False
                                while not userRemoved:
                                    try:
                                        printBoard(board)
                                        removepos1 = int(
                                            input("\n Mill Formed. Remove a '2' piece: "))

                                        if board[removepos1] == '2' and not isMill(removepos1, board) or (isMill(removepos1, board) and numOfPieces(board, "1") == 3):
                                            board[removepos1] = 'x'
                                            userRemoved = True
                                        else:
                                            print("Invalid Position")
                                    except Exception as e:
                                        print(str(e))
                                        print("Error while accepting input")

                            userPlaced = True
                            userMoved = True

                        else:
                            print("Invalid Position")

                    else:
                        print("Only adjacent locations in Stage 2. Try again.")

            except Exception as e:
                print(str(e))

        if(len(possibleMoves_stage2or3(board, '1')) == 0):
            print("-----------")
            print("    TIE    ")
            print("-----------")
            sys.exit()

        elif numOfPieces(board, '2') < 3:
            print("PLAYER 1 WINS")
            sys.exit()

        else:
            printBoard(board)

        # PLAYER 2 STAGE 2 MOVE

        userMoved = False
        while not userMoved:
            try:
                movable = False

                if numOfPieces(board, '2') == 3:
                    only3 = True
                else:
                    only3 = False

                while not movable:
                    pos1 = int(
                        input("\nPLAYER 2: Which '2' piece will you move?: "))

                    while board[pos1] != '2':
                        print("Invalid. Try again.")
                        pos1 = int(
                            input("\nPLAYER 2: Which '2' piece will you move?: "))

                    if only3:
                        movable = True
                        print("Stage 3 for Player 2. Allowed to Fly")
                        break

                    possibleMoves = adjacentLocations(pos1)

                    for adjpos in possibleMoves:
                        if board[adjpos] == 'x':
                            movable = True
                            break
                    if movable == False:
                        print("No empty adjacent pieces!")

                userPlaced = False

                while not userPlaced:
                    newpos1 = int(input("'2' New Position is : "))

                    if newpos1 in adjacentLocations(pos1) or only3:

                        if board[newpos1] == 'x':
                            board[pos1] = 'x'
                            board[newpos1] = '2'

                            if isMill(newpos1, board):
                                userRemoved = False
                                while not userRemoved:
                                    try:
                                        printBoard(board)
                                        removepos1 = int(
                                            input("\n Mill Formed. Remove a '1' piece: "))

                                        if board[removepos1] == '1' and not isMill(removepos1, board) or (isMill(removepos1, board) and numOfPieces(board, "2") == 3):
                                            board[removepos1] = 'x'
                                            userRemoved = True
                                        else:
                                            print("Invalid Position")
                                    except Exception as e:
                                        print(str(e))
                                        print("Error while accepting input")

                            userPlaced = True
                            userMoved = True

                        else:
                            print("Invalid Position")

                    else:
                        print("Only adjacent locations in Stage 2. Try again.")

            except Exception as e:
                print(str(e))

        if(len(possibleMoves_stage2or3(board, '2')) == 0):
            print("-----------")
            print("    TIE    ")
            print("-----------")
            sys.exit()

        elif numOfPieces(board, '1') < 3:
            print("PLAYER 2 WINS")
            sys.exit()

        else:
            printBoard(board)


if __name__ == "__main__":
    HUMAN_V_HUMAN()
