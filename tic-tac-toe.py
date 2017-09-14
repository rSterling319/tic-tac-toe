#Ideas for Tic-Tac-Toe GUI
#Guess a number to determine who goes first


import os

os.system('clear')

board = {'a1':' ', 'a2':' ','a3':' ', 'b1':' ', 'b2':' ','b3':' ', 'c1':' ', 'c2':' ', 'c3':' '}


def printGame():
    global board
    print("  1 2 3")
    print("a %s|%s|%s" %(board['a1'],board['a2'],board['a3']))
    print("  -----")
    print("b %s|%s|%s" %(board['b1'],board['b2'],board['b3']))
    print("  -----")
    print("c %s|%s|%s" %(board['c1'],board['c2'],board['c3']))

def validateMove(move):
    global board
    move = move.lower()
    try:
        if board[move] == ' ':
            return True
        else:
            return False
    except KeyError:
        return False

def checkWin():
    global board
    win =''
    for i in 'abc':
        for j in '123':
            win+=board[i+j]
        if win == 'XXX' or win == 'OOO':
            return True
        else:
            win =''
        win =''
    for i in '123':
        for j in 'abc':
            win+=board[j+i]
        if win == 'XXX' or win == 'OOO':
            return True
        else:
            win =''

    if board['a1']+board['b2']+board['c3'] == 'XXX' or  board['a1']+board['b2']+board['c3'] == 'OOO':
        return True

    if  board['c1']+board['b2']+board['a3'] == 'XXX' or  board['c1']+board['b2']+board['a3'] == 'OOO':
        return True

    return False

def humanVhuman():
    player1 = input("Player1: Enter your name: ")
    player2 = input("Player2: Enter your name: ")
    turns = 0
    win = False
    while(not win):
        os.system('clear')
        printGame()
        if turns %2==0:
            move = input("%s your move: " %player1)
        else:
            move = input("%s your move: " %player2)
        if validateMove(move):
            if turns % 2 == 0:
                board[move] = 'X'
            else:
                board[move]= 'O'
            turns+=1
        else:
            print("sorry, invalid move")
        win = checkWin()
        if win:
            printGame()
            if turns %2 == 0:
                os.system('clear')
                print('%s you win!' %player2)
            else:
                os.system('clear')
                print('%s you win!' %player1)
        if turns >= 9 and not win:
            os.system('clear')
            printGame()
            print("CAT")
            break


def gameLoop(option):
    global board
    board = {'a1':' ', 'a2':' ','a3':' ', 'b1':' ', 'b2':' ','b3':' ', 'c1':' ', 'c2':' ', 'c3':' '}
    if option == 1:
        os.system('clear')
        humanVhuman()
    elif option == 2:
        pass
    elif option ==3:
        pass
    else:
        pass

def printMainMenu():
    print("Tic-Tac-Toe")
    print("="*11)
    print("1) Human vs. Human")
    print("2) Human vs. AI")
    print("3) AI vs. AI")
    print("4) Quit")


option = ''
while(option != 4):
    printMainMenu()
    try:
        option = int(input("Enter your choice: "))
        if option > 0 and option < 4:
            gameLoop(option)
        else:
            if option != 4:
                os.system('clear')
                print("Choice invalid")
            else:
                os.system('clear')
                print("Good-Bye")
    except ValueError:
        os.system('clear')
        print("Choice invalid")
