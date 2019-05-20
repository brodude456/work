from copy import deepcopy
from random import randint

broj_kolona=7
broj_redova=6

board=[[":_:",":_:",":_:",":_:",":_:",":_:",":_:"],[":_:",":_:",":_:",":_:",":_:",":_:",":_:"],[":_:",":_:",":_:",":_:",":_:",":_:",":_:"],[":_:",":_:",":_:",":_:",":_:",":_:",":_:"],[":_:",":_:",":_:",":_:",":_:",":_:",":_:"],[":_:",":_:",":_:",":_:",":_:",":_:",":_:"]]

def print_te(board):
    for i in board:
        print(i)

def move_down(board):

    board=board
    for i in range(broj_redova-1):
        for j in range(broj_kolona):
            for i in range(broj_redova-2,-1,-1):
                if board[i+1][j]==":_:":
                    board[i+1][j],board[i][j]=board[i][j],board[i+1][j]

    return board

def choose_who():

    inputt=input("enter who you want to go first")
    alovbles=["me","you","flip a coin"]

    while inputt.lower() not in alovbles:
        inputt=input("invalid answer try again admin")

    if inputt.lower()=="me":
        covjek,racunar=" x "," o "

    elif inputt.lower()=="you":
        covjek,racunar="  o "," x "
    else:
        if randint(0,1)==0:
             covjek,racunar=" x "," o "
        else:
            covjek,racunar=" o "," x "

    return covjek,racunar

def all_possible_wins(broj_kolona,broj_redova):
    list_of=[]
    list_of_2=[]
    list_of_3=[]
    list_of_4=[]

    for i in range(broj_redova):
        for j in range(broj_kolona-3):
            list_of.append([i,j,j+1,j+2,j+3])


    for j in range(broj_kolona):
        for i in range(broj_redova-3):
            list_of_2.append([i,i+1,i+2,i+3,j])

    for j in range(broj_kolona-3):
        for i in range(broj_redova-3):
            list_of_3.append([i,i+1,i+2,i+3,j,j+1,j+2,j+3])

    for j in range(3,broj_kolona):
        for i in range(broj_redova-3):
            list_of_4.append([i,i+1,i+2,i+3,j,j-1,j-2,j-3])


    return list_of,list_of_2,list_of_3,list_of_4


def check_if_won(board,user,list_of,list_of_2,list_of_3,list_of_4):
    board=board
    user=user

    for i in list_of:

        if board[i[0]][i[1]]==board[i[0]][i[2]]==board[i[0]][i[3]]==board[i[0]][i[4]]==user:
            return True

    for i in list_of_2:

        if board[i[0]][i[4]]==board[i[1]][i[4]]==board[i[2]][i[4]]==board[i[3]][i[4]]==user:
            return True

    for i in list_of_3:

        if board[i[0]][i[4]]==board[i[1]][i[5]]==board[i[2]][i[6]]==board[i[3]][i[7]]==user:
            return True

    for i in list_of_4:

        if board[i[0]][i[4]]==board[i[1]][i[5]]==board[i[2]][i[6]]==board[i[3]][i[7]]==user:
            return True

    return False

def how_to_win(board,user,list_of,list_of_2,list_of_3,list_of_4):
    board=board
    user=user

    for i in list_of:

        if board[i[0]][i[1]]==board[i[0]][i[2]]==board[i[0]][i[3]]==user and board[i[0]][i[4]]==":_:":

            if i[0]==len(board)-1:
                board[i[0]][i[4]]=user
                return board

            elif board[i[0]+1][i[4]]!=":_:":
                board[i[0]][i[4]]=user
                return board

        elif board[i[0]][i[1]]==board[i[0]][i[2]]==board[i[0]][i[4]]==user and board[i[0]][i[3]]==":_:":

            if i[0]==len(board)-1:
                board[i[0]][i[3]]=user
                return board

            elif board[i[0]+1][i[3]]!=":_:":
                board[i[0]][i[3]]=user
                return board

        elif board[i[0]][i[1]]==board[i[0]][i[3]]==board[i[0]][i[4]]==user and board[i[0]][i[2]]==":_:":

            if i[0]==len(board)-1:
                board[i[0]][i[2]]=user
                return board

            elif board[i[0]+1][i[2]]!=":_:":
                board[i[0]][i[2]]=user
                return board

        elif board[i[0]][i[2]]==board[i[0]][i[3]]==board[i[0]][i[4]]==user and board[i[0]][i[1]]==":_:":

            if i[0]==len(board)-1:
                board[i[0]][i[1]]=user
                return board

            elif board[i[0]+1][i[1]]!=":_:":
                board[i[0]][i[1]]=user
                return board

    for i in list_of_2:

        if board[i[0]][i[4]]==board[i[1]][i[4]]==board[i[2]][i[4]]==user and board[i[3]][i[4]]==":_:" :

            if i[3]==len(board)-1:
                board[i[3]][i[4]]=user
                return board

            elif board[i[3]+1][i[4]]!=":_:":
                board[i[3]][i[4]]=user
                return board

        elif board[i[0]][i[4]]==board[i[1]][i[4]]==board[i[3]][i[4]]==user and board[i[2]][i[4]]==":_:" :

            if i[2]==len(board)-1:
                board[i[2]][i[4]]=user
                return board

            elif board[i[2]+1][i[4]]!=":_:":
                board[i[2]][i[4]]=user
                return board

        elif board[i[0]][i[4]]==board[i[2]][i[4]]==board[i[3]][i[4]]==user and board[i[1]][i[4]]==":_:" :

            if i[1]==len(board)-1:
                board[i[1]][i[4]]=user
                return board

            elif board[i[1]+1][i[4]]!=":_:":
                board[i[1]][i[4]]=user
                return board

        elif board[i[1]][i[4]]==board[i[2]][i[4]]==board[i[3]][i[4]]==user and board[i[0]][i[4]]==":_:":

            if i[0]==len(board)-1:
                board[i[0]][i[4]]=user
                return board

            elif board[i[0]+1][i[4]]!=":_:":
                board[i[0]][i[4]]=user
                return board


    for i in list_of_3:

        if board[i[0]][i[4]]==board[i[1]][i[5]]==board[i[2]][i[6]]==user and board[i[3]][i[7]]==":_:" :

            if i[3]==len(board)-1:
                board[i[3]][i[7]]=user
                return board

            elif board[i[3]+1][i[7]]!=":_:":
                board[i[3]][i[7]]=user
                return board

        elif board[i[0]][i[4]]==board[i[1]][i[5]]==board[i[3]][i[7]]==user and board[i[2]][i[6]]==":_:" :

            if i[2]==len(board)-1:
                board[i[2]][i[6]]=user
                return board

            elif board[i[2]+1][i[6]]!=":_:":
                board[i[2]][i[6]]=user
                return board

        elif board[i[0]][i[4]]==board[i[2]][i[6]]==board[i[3]][i[7]]==user and board[i[1]][i[5]]==":_:" :

            if i[1]==len(board)-1:
                board[i[1]][i[5]]=user
                return board

            elif board[i[1]+1][i[5]]!=":_:":
                board[i[1]][i[5]]=user
                return board

        elif board[i[1]][i[5]]==board[i[2]][i[6]]==board[i[3]][i[7]]==user and board[i[0]][i[4]]==":_:" :

            if i[0]==len(board)-1:
                board[i[0]][i[4]]=user
                return board

            elif board[i[0]+1][i[4]]!=":_:":
                board[i[0]][i[4]]=user
                return board

    for i in list_of_4:

        if board[i[0]][i[4]]==board[i[1]][i[5]]==board[i[2]][i[6]]==user and board[i[3]][i[7]]==":_:" :

            if i[3]==len(board)-1:
                board[i[3]][i[7]]=user
                return board

            elif board[i[3]+1][i[7]]!=":_:":
                board[i[3]][i[7]]=user
                return board

        elif board[i[0]][i[4]]==board[i[1]][i[5]]==board[i[3]][i[7]]==user and board[i[2]][i[6]]==":_:" :

            if i[2]==len(board)-1:
                board[i[2]][i[6]]=user
                return board

            elif board[i[2]+1][i[6]]!=":_:":
                board[i[2]][i[6]]=user
                return board

        elif board[i[0]][i[4]]==board[i[2]][i[6]]==board[i[3]][i[7]]==user and board[i[1]][i[5]]==":_:" :

            if i[1]==len(board)-1:
                board[i[1]][i[5]]=user
                return board

            elif board[i[1]+1][i[5]]!=":_:":
                board[i[1]][i[5]]=user
                return board

        elif board[i[1]][i[5]]==board[i[2]][i[6]]==board[i[3]][i[7]]==user and board[i[0]][i[4]]==":_:" :

            if i[0]==len(board)-1:
                board[i[0]][i[4]]=user
                return board

            elif board[i[0]+1][i[4]]!=":_:":
                board[i[0]][i[4]]=user
                return board

    return board

def how_not_to_lose(board,user,list_of,list_of_2,list_of_3,list_of_4,computer):
    board=board
    user=user
    computer=computer

    for i in list_of:

        if board[i[0]][i[1]]==board[i[0]][i[2]]==board[i[0]][i[3]]==user and board[i[0]][i[4]]==":_:" :

            if i[0]==len(board)-1:
                board[i[0]][i[4]]=computer
                return board

            elif board[i[0]+1][i[4]]!=":_:":
                board[i[0]][i[4]]=computer
                return board

        elif board[i[0]][i[1]]==board[i[0]][i[2]]==board[i[0]][i[4]]==user and board[i[0]][i[3]]==":_:" :

            if i[0]==len(board)-1:
                board[i[0]][i[3]]=computer
                return board

            elif board[i[0]+1][i[3]]!=":_:":
                board[i[0]][i[3]]=computer
                return board

        elif board[i[0]][i[1]]==board[i[0]][i[3]]==board[i[0]][i[4]]==user and board[i[0]][i[2]]==":_:" :

            if i[0]==len(board)-1:
                board[i[0]][i[2]]=computer
                return board

            elif board[i[0]+1][i[2]]!=":_:":
                board[i[0]][i[2]]=computer
                return board

        elif board[i[0]][i[2]]==board[i[0]][i[3]]==board[i[0]][i[4]]==user and board[i[0]][i[1]]==":_:":

            if i[0]==len(board)-1:
                board[i[0]][i[1]]=computer
                return board

            elif board[i[0]+1][i[1]]!=":_:":
                board[i[0]][i[1]]=computer
                return board

    for i in list_of_2:

        if board[i[0]][i[4]]==board[i[1]][i[4]]==board[i[2]][i[4]]==user and board[i[3]][i[4]]==":_:" :

            if i[3]==len(board)-1:
                board[i[3]][i[4]]=computer
                return board

            elif board[i[3]+1][i[4]]!=":_:":
                board[i[3]][i[4]]=computer
                return board

        elif board[i[0]][i[4]]==board[i[1]][i[4]]==board[i[3]][i[4]]==user and board[i[2]][i[4]]==":_:" :

            if i[2]==len(board)-1:
                board[i[2]][i[4]]=computer
                return board

            elif board[i[2]+1][i[4]]!=":_:":
                board[i[2]][i[4]]=computer
                return board

        elif board[i[0]][i[4]]==board[i[2]][i[4]]==board[i[3]][i[4]]==user and board[i[1]][i[4]]==":_:" :

            if i[1]==len(board)-1:
                board[i[1]][i[4]]=computer
                return board

            elif board[i[1]+1][i[4]]!=":_:":
                board[i[1]][i[4]]=computer
                return board

        elif board[i[1]][i[4]]==board[i[2]][i[4]]==board[i[3]][i[4]]==user and board[i[0]][i[4]]==":_:" :

            if i[0]==len(board)-1:
                board[i[0]][i[4]]=computer
                return board

            elif board[i[0]+1][i[4]]!=":_:":
                board[i[0]][i[4]]=computer
                return board


    for i in list_of_3:

        if board[i[0]][i[4]]==board[i[1]][i[5]]==board[i[2]][i[6]]==user and board[i[3]][i[7]]==":_:" :

            if i[3]==len(board)-1:
                board[i[3]][i[7]]=computer
                return board

            elif board[i[3]+1][i[7]]!=":_:":
                board[i[3]][i[7]]=computer
                return board

        elif board[i[0]][i[4]]==board[i[1]][i[5]]==board[i[3]][i[7]]==user and board[i[2]][i[6]]==":_:" :

            if i[2]==len(board)-1:
                board[i[2]][i[6]]=computer
                return board

            elif board[i[2]+1][i[6]]!=":_:":
                board[i[2]][i[6]]=computer
                return board

        elif board[i[0]][i[4]]==board[i[2]][i[6]]==board[i[3]][i[7]]==user and board[i[1]][i[5]]==":_:" :

            if i[1]==len(board)-1:
                board[i[1]][i[5]]=computer
                return board

            elif board[i[1]+1][i[5]]!=":_:":
                board[i[1]][i[5]]=computer
                return board

        elif board[i[1]][i[5]]==board[i[2]][i[6]]==board[i[3]][i[7]]==user and board[i[0]][i[4]]==":_:" :

            if i[0]==len(board)-1:
                board[i[0]][i[4]]=computer
                return board

            elif board[i[0]+1][i[4]]!=":_:":
                board[i[0]][i[4]]=computer
                return board

    for i in list_of_4:

        if board[i[0]][i[4]]==board[i[1]][i[5]]==board[i[2]][i[6]]==user and board[i[3]][i[7]]==":_:" :

            if i[3]==len(board)-1:
                board[i[3]][i[7]]=computer
                return board

            elif board[i[3]+1][i[7]]!=":_:":
                board[i[3]][i[7]]=computer
                return board

        elif board[i[0]][i[4]]==board[i[1]][i[5]]==board[i[3]][i[7]]==user and board[i[2]][i[6]]==":_:" :

            if i[2]==len(board)-1:
                board[i[2]][i[6]]=computer
                return board

            elif board[i[2]+1][i[6]]!=":_:":
                board[i[2]][i[6]]=computer
                return board

        elif board[i[0]][i[4]]==board[i[2]][i[6]]==board[i[3]][i[7]]==user and board[i[1]][i[5]]==":_:" :

            if i[1]==len(board)-1:
                board[i[1]][i[5]]=computer
                return board

            elif board[i[1]+1][i[5]]!=":_:":
                board[i[1]][i[5]]=computer
                return board

        elif board[i[1]][i[5]]==board[i[2]][i[6]]==board[i[3]][i[7]]==user and board[i[0]][i[4]]==":_:" :

            if i[0]==len(board)-1:
                board[i[0]][i[4]]=computer
                return board

            elif board[i[0]+1][i[4]]!=":_:":
                board[i[0]][i[4]]=computer
                return board
        


    return board

def making_a_random(computer,board):
    board=board
    computer=computer
    spot=randint(0,broj_kolona-1)
    while board[0][spot]!=":_:":
        spot=randint(0,broj_kolona-1)

    board[0][spot]=computer
    board=move_down(board)
    return  board

def make_human_choose(board,human_figure):
    board=board
    inputt=int(input("which column you want to chose to place your move on"))
    while inputt>len(board[0])-1 or inputt<len(board[0])*-1 or board[0][inputt]!=":_:":
        inputt=int(input("thats in valid please try again"))
    board[0][inputt]=human_figure
    board=move_down(board)
    return board

move=" x "

list1,list2,list3,list4=all_possible_wins(broj_kolona,broj_redova)

input1111="yes"

computer_wins=0
human_wins=0

print_te(board)

while input1111.lower()=="yes":

    board=[[":_:",":_:",":_:",":_:",":_:",":_:",":_:"],[":_:",":_:",":_:",":_:",":_:",":_:",":_:"],[":_:",":_:",":_:",":_:",":_:",":_:",":_:"],[":_:",":_:",":_:",":_:",":_:",":_:",":_:"],[":_:",":_:",":_:",":_:",":_:",":_:",":_:"],[":_:",":_:",":_:",":_:",":_:",":_:",":_:"]]

    human,racunar=choose_who()

    while True:

        if human==move:

            board=make_human_choose(board,human)
            if check_if_won(board,human,list1,list2,list3,list4)==True:
                print_te(board)
                print("you won byeee")
                human_wins+=1
                break
            move=racunar

            if ":_:" not in board[0] and ":_:" not in board[1] and ":_:" not in board[2] and ":_:" not in board[3] and ":_:" not in board[4] and ":_:" not in board[5]:
                print("its a tie")
                break

            print_te(board)

        if racunar==move:

            new_not_losing=how_not_to_lose(deepcopy(board),human,list1,list2,list3,list4,racunar)
            wining_table=how_to_win(deepcopy(board),racunar,list1,list2,list3,list4)

            if wining_table!=board:
                board=how_to_win(deepcopy(board),racunar,list1,list2,list3,list4)
                print_te(board)
                print("i won byeee")
                computer_wins+=1
                break

            elif new_not_losing!=board:
                board=how_not_to_lose(board,human,list1,list2,list3,list4,racunar)
                print("ha not gona let you win sucker")

            else:
                board=making_a_random(racunar,board)
                print_te(board)

            if ":_:" not in board[0] and ":_:" not in board[1] and ":_:" not in board[2] and ":_:" not in board[3] and ":_:" not in board[4] and ":_:" not in board[5]:
                print("its a tie")
                break

            print_te(board)

            move=human

    input1111=input("do you want to reapet")
    while input1111.lower()!="yes" and input1111.lower()!="no":
        input1111=input("do you want to reapet")

if computer_wins>human_wins:
    print("thanks for playing i have"+str(computer_wins)+ "wins and you have" + str(human_wins) + "wins so i win")

elif computer_wins<human_wins:
    print("thanks for playing i have"+str(computer_wins)+ "wins and you have" + str(human_wins) + "wins so you win")

else:
     print("thanks for playing i have"+str(computer_wins)+ "wins and you have" + str(human_wins) + "wins its a tie")
