from random import randint
from copy import deepcopy
broj_kolona=4
broj_redova=4

board=[[":_:",":_:",":_:",":_:",],[":_:",":_:",":_:",":_:",],[":_:",":_:",":_:",":_:",],[":_:",":_:",":_:",":_:",]]
def move(board,way):
    board=deepcopy(board)
    way=way

    reversedd=[]

    for i in range(0,len(board)):
        reversedd.append(i)

        reversedd.reverse()

    if broj_kolona<broj_redova:

        bigger=broj_redova

    else:

        bigger=broj_kolona

    for k in range(0,bigger-1):

        if way=="up":
            for j in range(broj_kolona):
                for i in range(1,broj_redova):
                    if board[i-1][j]==":_:":
                        board[i-1][j],board[i][j]=board[i][j],board[i-1][j]


        elif way=="down":
            for j in range(broj_kolona):
                for i in range(broj_redova-2,-1,-1):
                    if board[i+1][j]==":_:":
                        board[i+1][j],board[i][j]=board[i][j],board[i+1][j]

        elif way=="left":
            for i in range(broj_redova):
                for j in range(1,broj_kolona):
                    if board[i][j-1]==":_:":
                        board[i][j-1],board[i][j]=board[i][j],board[i][j-1]

        elif way=="right":
            for i in range(broj_redova):
                for j in range(broj_kolona-2,-1,-1):
                    if board[i][j+1]==":_:":
                        board[i][j+1],board[i][j]=board[i][j],board[i][j+1]


    return  board

def print_te(board):
    for i in board:
        print(i)

def make_a_random_numero(board,broj_kolona,broj_redova):

    mat=deepcopy(board)
    BROJ_KOLONA=broj_kolona
    BROJ_REDOVA=broj_redova
    initial_num = 2

    if randint(1,10)<=3:
        initial_num = 4


    random_row  = randint(0,BROJ_REDOVA-1)
    random_column = randint(0,BROJ_KOLONA-1)

    while mat[random_row][random_column]!=":_:":
            random_row=randint(0,BROJ_REDOVA-1)
            while ":_:" in mat[random_row] and mat[random_row][random_column]!=":_:":
                random_column=randint(0,BROJ_KOLONA-1)


    mat[random_row][random_column] =":{}:".format(str(initial_num))

    return mat

def check_if_numero_coliding(board,way):

    board=deepcopy(board)
    way=way

    if way=="up":
            for j in range(broj_kolona):
                for i in range(1,broj_redova):
                    if board[i-1][j]==board[i][j]!=":_:":
                        board[i-1][j]=":{}:".format(str(int(board[i][j][1:-1])*2))
                        board[i][j]=":_:"
                        board=move(board,way)


    elif way=="down":
            for j in range(broj_kolona):
                for i in range(broj_redova-2,-1,-1):
                    if board[i+1][j]==board[i][j]!=":_:":
                        board[i+1][j]=":{}:".format(str(int(board[i][j][1:-1])*2))
                        board[i][j]=":_:"
                        board=move(board,way)

    elif way=="left":
            for i in range(broj_redova):
                for j in range(1,broj_kolona):
                    if board[i][j-1]==board[i][j]!=":_:":
                        board[i][j-1]=":{}:".format(str(int(board[i][j][1:-1])*2))
                        board[i][j]=":_:"
                        board=move(board,way)

    elif way=="right":
            for i in range(broj_redova):
                for j in range(broj_kolona-2,-1,-1):
                    if board[i][j+1]==board[i][j]!=":_:":
                        board[i][j+1]=":{}:".format(str(int(board[i][j][1:-1])*2))
                        board[i][j]=":_:"
                        board=move(board,way)

    return board

z=0
print_te(board)

while True:

    if z==0:
        print("                                                ")
        board=make_a_random_numero(board,broj_kolona,broj_redova)

    print_te(board)

    if ":_:" not in board[0] and ":_:" not in board[1] and ":_:" not in board[1] and ":_:" not in board[2] and ":_:" not in board[3] and board==check_if_numero_coliding(board,"up") and board==check_if_numero_coliding(board,"down") and board==check_if_numero_coliding(board,"right") and board==check_if_numero_coliding(board,"left"):
        print("game over")
        break

    alavobles=["up","down","right","left"]
    inputt=input("which way do you want to go")

    while inputt not in alavobles:
        inputt=input("not a valid answer try again")

    if board!=move(board,inputt):
        board=move(board,inputt)
        z=0
    elif board==move(board,inputt):
        z=1
    board=check_if_numero_coliding(board,inputt)

