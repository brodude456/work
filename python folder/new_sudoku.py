import random
from copy import deepcopy

board = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]


moves=[]

def print_board(bo):

    for i in range(len(bo)):

        if i % 3 == 0 and i != 0:

            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):

            if j % 3 == 0 and j != 0:

                print(" | ", end="")


            if j == 8:

                print(bo[i][j])

            else:

                print(str(bo[i][j]) + " ", end="")

print_board(board)

def find_empty(bo):

    for i in range(len(bo)):

        for j in range(len(bo[0])):

            if bo[i][j] == 0:

                return (i, j)

    return None

def Check_row(bo,pos_c):

    p=0

    for i in bo:

        w=0

        for j in bo:

            if i[pos_c]==j[pos_c]!=0 and p!=w:

                return False

            w+=1

        p+=1

    return True

def Check_IF_VALID(bo,pos_r,pos_c):

    p=0

    for i in bo[pos_r]:

        w=1

        for j in bo[pos_r]:

            if j==i!=0 and w!=p:

                return False

            w+=1

        p+=1


        p=0

        for i in bo:

            w=0

            for j in bo:

                if i[pos_c]==j[pos_c]!=0 and p!=w:

                    return False

                w+=1

            p+=1

        return True

    box_x=pos_c//3
    box_y=pos_r//3

    test_board=[]

    for i in range(len(bo)):

        for j in range(len(bo[0])):

            if i//3==box_y and j//3==box_x:

                test_board.append(bo[i][j])

    p=0

    for i in test_board:

        w=0

        for j in test_board:

            if i==j!=0 and w!=p:

                return False

            w+=1

        p+=1

    return True

def solve():

   while True:

        find=find_empty(board)

        if not(find):

            return True

        else:

            row,column=find

        w=1

        for i in range(1,11):

            board_test=deepcopy(board)
            board_test[row][column]=i

            if Check_IF_VALID(board_test,row,column):

                board[row][column]=i
                moves.append((row,column))
                w=0
                print_board(board)

        if w==1:

            for i in range(len(moves)-1,-1,-1):

                row,column=moves[i]

                for j in range(1,11):

                    board_test=deepcopy(board)
                    board_test[row][column]=j

                    if Check_IF_VALID(board_test,row,column):

                        board[row][column]=j
                        w=0
                        print_board(board)
                        break

                if w==0:

                    break






def ask_what():

    ask_what=input("do you want to cointinue adding numeros to the board")

    while ask_what!="no" and ask_what!="yes":

        ask_what=input('enter a valid input')

    return ask_what

def ask_where():

    ask_where=int(input("which row you want m8"))

    while True:

        if ask_where<len(board):

            if 0 not in board[ask_where]:

                ask_where=int(input("try agin no 0 there m8"))

            else:

                break

        else:

            ask_where=int(input("try agsin but valiiiiiiiid"))

    ask_where_column=int(input("which column you want"))

    while True:

        if ask_where_column<len(board[0]):

            if board[ask_where][ask_where_column]!=0:

                ask_where_column=int(input("try agin no 0 there m8"))

            else:

                break

        else:

            ask_where_column=int(input("try agsin but valiiiiiiiid"))

    board_rezerva=deepcopy(board)

    ask_numero=int(input("which numero you want there m8"))

    while True:

        if ask_numero in range(1,11):

            board[ask_where][ask_where_column]=ask_numero

            if not(Check_IF_VALID(board,ask_where,ask_where_column)):

                ask_numero=int(input("try agin cant that number there m8"))

                board[ask_where][ask_where_column]=ask_numero

            else:

                break

        else:

            ask_where_column=int(input("try agsin but valiiiiiiiidkkkkkkkkkk"))

ask_whatt=True

def ask_what_general():

    inputt=input("do you want to delete or add an numero")

    while inputt!="add" and inputt!="delete" or inputt=="add" and not(find_empty(board)) or inputt=="delete" and not(check_if_can_delete()):

        inputt=inputt("please enter a valid input m8")

    if inputt=="add":

        ask_where()

    else:

        delete()

def delete():

    ask_where=int(input("which row you want m8"))

    while True:

        if ask_where<len(board):

            w=1

            for i in board[ask_where]:

                for j in range(1,11):

                    if i==j:

                        w=0
            if w!=0:

                ask_where=int(input("try agin no numero there m8"))

            else:

                break

        else:

            ask_where=int(input("try agsin but valiiiiiiiid"))

    ask_where_column=int(input("which column you want"))

    while True:

        if ask_where_column<len(board[0]):

            if 0 == board[ask_where][ask_where_column]:

                ask_where_column=int(input("try agin no 0 there m8"))

            else:

                break

        else:

            ask_where_column=int(input("try agsin but valiiiiiiiid"))

    board_rezerva=deepcopy(board)

    board[ask_where][ask_where_column]=0

def check_if_can_delete():

     for i in board:

         for r in i:

             for j in range(1,11):

                 if r==j:

                     return True
     return False

ask_whattt="yes"

while ask_whattt=="yes":

    ask_what_general()

    print_board(board)

    ask_whattt= ask_what()

solve()

print_board(board)






