import random

def drawBoard(board):

    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])

    print('-----------')

    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
   
    print('-----------')

    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])

def inputPlayerLetter():
    letter = ''
    while not(letter=='X' or letter=='O'):
        print('Do you want to be X or O?')
        letter = input().upper()
    if letter=='X':
        return ['X','O']
    else:
        return ['O','X']

def whoGoesFirst():
    x = random.randint(0,1)
    if x == 0:
        return 'Player'
    else:
        return 'Computer'

 
def isSpaceFree(board,move):
    return board[move]==''

def getPlayerMove(board):
    move = ''
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board,int(move)):
        print("What is your next move?")
        move = input()
    return int(move)

def makeMove(board,letter,move):
    board[move] = letter

def isWinner(board,letter):
    return ((board[7] == letter and board[8] == letter and board[9] == letter) or
    (board[4] == letter and board[5] == letter and board[6] == letter) or
    (board[1] == letter and board[2] == letter and board[3] == letter) or
    (board[1] == letter and board[4] == letter and board[7] == letter) or
    (board[2] == letter and board[5] == letter and board[8] == letter) or
    (board[3] == letter and board[6] == letter and board[9] == letter) or
    (board[1] == letter and board[5] == letter and board[9] == letter) or
    (board[3] == letter and board[5] == letter and board[7] == letter))

def isBoardFull(board):
    for i in range(1,10):
        if isSpaceFree(board,i):
            return False
    return True

def chooseRandomMoveFromList(board,movesList):
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board,i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
            return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board,computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    for i in range(1, 10):
        copy = [x for x in board]
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
        if isWinner(copy, computerLetter):
            return i
    
    for i in range(1, 10):
        copy = [x for x in board]
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
        if isWinner(copy, playerLetter):
            return i
    
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move
    
    if isSpaceFree(board, 5):
        return 5
    
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')




#----------------------Main-------------------
print("Welcome to Tic-Tac-Toe")

while True:
    board = ['']*10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print("The",turn,"will go first")
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'Player':
            drawBoard(board)
            move = getPlayerMove(board)
            makeMove(board,playerLetter,move)
            if isWinner(board,playerLetter):
                drawBoard(board)
                print("Congratulations!! You have won the game")
                gameIsPlaying = False
            else:
                if isBoardFull(board):
                    drawBoard(board)
                    print("The game is a tie")
                    break
                else:
                    turn = 'Computer'
        else:
            move = getComputerMove(board,computerLetter)

            makeMove(board,computerLetter,move)
            if isWinner(board,computerLetter):
                drawBoard(board)
                print("The Computer has beaten you! You Lose the game")
                gameIsPlaying = False
            else:
                if isBoardFull(board):
                    drawBoard(board)
                    print("The game is a tie")
                    break
                else:
                    turn = 'Player'
    if not playAgain():
        break
