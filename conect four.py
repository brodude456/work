from copy import deepcopy
import random

broj_kolona=7
broj_redova=6

board=[[":_:",":_:",":_:",":_:",":_:",":_:",":_:"],[":_:",":_:",":_:",":_:",":_:",":_:",":_:"],[":_:",":_:",":_:",":_:",":_:",":_:",":_:"],[":_:",":_:",":_:",":_:",":_:",":_:",":_:"],[":_:",":_:",":_:",":_:",":_:",":_:",":_:"],[":_:",":_:",":_:",":_:",":_:",":_:",":_:"]]

list_of_filled=[0,0,0,0,0,0,0]

def win(racunarakacompter,list1,list2,list3,list4):

    for i in range(len(list_of_filled)):

        board[len(board)-list_of_filled[i]-1][i]=racunarakacompter
        if check_if_won(racunarakacompter,list1,list2,list3,list4) and len(board)-list_of_filled[i]!=0:
            print_te(board)
            print("ya lez go i won ,b b b b bitconeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeect")
            return True
        else:
            board[len(board)-list_of_filled[i]-1][i]=":_:"

    return False

def print_te(board):

    for i in board:

        print(i)

    print("         ")

def how_not_to_lose(racunarakacomputer,human,list1,list2,list3,list4):

    for i in range(len(list_of_filled)):

        board[len(board)-list_of_filled[i]-1][i]=human
        if check_if_won(human,list1,list2,list3,list4) and len(board)-list_of_filled[i]!=0:
            board[len(board)-list_of_filled[i]-1][i]=racunarakacomputer
            list_of_filled[i]+=1
            print("haha you tought i was gonna let you win sucker")
            return True
        else:
            board[len(board)-list_of_filled[i]-1][i]=":_:"

    return False

def making_a_random(racunar):

    spots_that_can_be_choosed=[]

    for i in range(len(list_of_filled)):

        if list_of_filled[i]<len(board):

            spots_that_can_be_choosed.append(i)

    spot=random.choice(spots_that_can_be_choosed)

    board[len(board)-list_of_filled[spot]-1][spot]=racunar
    list_of_filled[spot]+=1

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


def check_if_won(user,list_of,list_of_2,list_of_3,list_of_4):

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

def make_human_choose(board,human_figure):

    board=board

    inputt=int(input("which column you want to chose to place your move on"))

    while inputt>len(board[0])-1 or inputt<len(board[0])*-1 or list_of_filled[inputt]==len(board):

        inputt=int(input("thats in valid please try again"))

    board[len(board)-list_of_filled[inputt]-1][inputt]=human_figure

    list_of_filled[inputt]+=1



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

            make_human_choose(board,human)
            if check_if_won(human,list1,list2,list3,list4)==True:
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

            new_not_losing=how_not_to_lose(racunar,human,list1,list2,list3,list4)
            wining_table=win(racunar,list1,list2,list3,list4)

            if new_not_losing==False and wining_table==False:
                making_a_random(racunar)
                print_te(board)

            elif wining_table:
                break

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
