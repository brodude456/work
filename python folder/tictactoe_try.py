from copy import deepcopy

def check_if_won(board):
    posiible=[[0,1,2],[0,3,6],[0,4,8],[2,4,6,],[1,4,7],[2,5,8],[3,4,5],[6,7,8]]
    for x in posiible:
        if board[x[0]]==" O " and board[x[1]]==" O " and board[x[2]]==" O ":
            return  True
    return False

def to_win(board):
    posiible=[[0,1,2],[0,3,6],[0,4,8],[2,4,6,],[1,4,7],[2,5,8],[3,4,5],[6,7,8]]
    for x in posiible:
        if board[x[0]]==" x " and board[x[1]]==" x " and board[x[2]]==":_:":
            board[x[2]]=" x "
        elif board[x[0]]==" x " and board[x[1]]==":_:" and board[x[2]]==" x ":
            board[x[1]]=" x "
        elif board[x[0]]==":_:" and board[x[1]]==" x " and board[x[2]]==" x ":
            board[x[0]]=" x "
        else:
            continue

        break

    return board

def how_not_to_lose(board):
    posiible=[[0,1,2],[0,3,6],[0,4,8],[2,4,6,],[1,4,7],[2,5,8],[3,4,5],[6,7,8]]
    for x in posiible:
        if board[x[0]]==" O " and board[x[1]]==" O " and board[x[2]]==":_:":
            board[x[2]]=" x "
            break
        elif board[x[0]]==" O " and board[x[1]]==":_:" and board[x[2]]==" O ":
            board[x[1]]=" x "
            break
        elif board[x[0]]==":_:" and board[x[1]]==" O " and board[x[2]]==" O ":
            board[x[0]]=" x "
            break


    return board



def print_te(board):
    print(board[0],board[1],board[2])
    print(board[3],board[4],board[5])
    print(board[6],board[7],board[8])


import random
table=[":_:",':_:',":_:",
       ":_:",':_:',":_:",
       ":_:",':_:',":_:"]

print('wlecom to tic tac toe ')
bla=0
while True:

    if bla==0 and ":_:" in table:
        while True:
            numero=random.randint(0,8)


            if table[numero]==':_:':
                table[numero]=' x '
                break



    if ":_:" not in table:
        break

    print_te(table)
    answer_3=int(input("enter a numero between 0 to 10 excluding those two numeros two add o on the board"))

    while table[answer_3-1]!=":_:":
        answer_3=int(input("your entry wasnt valid please try again"))

    table[answer_3-1]=" O "

    if check_if_won(deepcopy(table)):
        print("you won this time but you will not be so lucky next time")
        print(":( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :(")

        break

    if ":_:" not in table:
        print("its a tie ")
        break

    new_table=how_not_to_lose(deepcopy(table))


    print(table)
    winning_table=to_win(deepcopy(table))
    print(table)
    print(new_table,"TABELA")

    if winning_table!=table:
        table=winning_table
        print_te(table)
        print("haha i won")
        print(":) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :)")
        break

    elif new_table!=table:
        table=new_table
        bla=1

    else:
        bla=0

print_te(table)






