from utils import *


def AI_VS_AI(heuristic1, heuristic2):

    board = []
    for i in range(24):
        board.append("x")

    evaluation = evaluate()
    print("Stage 1")
    for i in range(9):

        printBoard(board)
        evalBoard = minimax(
            board, ai_depth, True, alpha, beta, True, heuristic1)

        if evalBoard.evaluate == float('inf'):
            print("AI Bot 1 has won!")
            exit(0)
        else:
            board = evalBoard.board

        printBoard(board)
        evalBoard = minimax(
            board, ai_depth, False, alpha, beta, True, heuristic2)

        if evalBoard.evaluate == float('-inf'):
            print("AI Bot 2 has won!")
            exit(0)
        else:
            board = evalBoard.board

    print("Stage 2")
    while True:

        printBoard(board)
        evalBoard = minimax(
            board, ai_depth, True, alpha, beta, False, heuristic1)

        if evalBoard.evaluate == float('inf'):
            print("AI Bot 1 has won!")
            exit(0)
        else:
            board = evalBoard.board

        printBoard(board)
        evaluation = minimax(
            board, ai_depth, False, alpha, beta, False, heuristic2)

        if evaluation.evaluate == float('-inf'):
            print("AI Bot 2 has won")
            exit(0)
        else:
            board = evaluation.board


if __name__ == "__main__":
    AI_VS_AI(numPiecesHeuristic, potentialMillsHeuristic)
