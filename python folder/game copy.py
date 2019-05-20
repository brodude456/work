from copy import deepcopy
import random

class Cube():

    def __init__(self):

        self.board=[[":_:",":_:",":_:"],[":_:",":_:",":_:"],[":_:",":_:",":_:"]]
        self.broj_kolona=len(self.board[0])
        self.broj_redova=len(self.board)
        self.numeros=[]
        for i in range(1,10):
            self.numeros.append(str(i))

    def check_if_wrong_for_box(self):


                rezerv_board=deepcopy(self.board)

                test_board=[]

                for i in self.board:

                    for j in i:

                        test_board.append(j)

                p=0

                for i in test_board:

                    w=0

                    for j in test_board:

                        if i==j!=":_:" and w!=p :

                            return False

                        w+=1

                    p+=1

                return True


    def delete(self):

        Choose_row=int(input("which row do you want to chooe in this box to put your numero at"))

        while True:

            if Choose_row<len(self.board):

                w=0

                for i in self.board[Choose_row]:

                    if i==":_:":

                        w+=0

                if w==len(self.board[0]):

                    Choose_row=int(input("invalid try agaaaaaaaainnniiiinnninninin"))

                else:

                    break
            else:

                Choose_row=int(input("index out of range try again"))

        Choose_column=input("Choose the column you want ot place on,but if you made a mistake click return to reapet")

        if Choose_column=="retrun":

            self.ask_to_place_numero()

        else:

            Choose_column=int(Choose_column)

            while True:

                if Choose_column<len(self.board[0]):

                    if  self.board[Choose_row][Choose_column]==":_:":

                        Choose_column=int(input("invalid try agaaaaaaaainnniiiinnninninin"))

                    else:

                        break
                else:

                    Choose_column=int(input("index out of range try again"))

        self.board[Choose_row][Choose_column]=":_:"


    def ask_to_place_numero(self):

        Choose_row=int(input("which row do you want to chooe in this box to put your numero at"))

        while True:

            if Choose_row<len(self.board):

                if  ":_:" not in self.board[Choose_row]:

                    Choose_row=int(input("invalid try agaaaaaaaainnniiiinnninninin"))

                else:

                    break
            else:

                Choose_row=int(input("index out of range try again"))

        Choose_column=input("Choose the column you want ot place on,but if you made a mistake click return to reapet")

        if Choose_column=="retrun":

            self.ask_to_place_numero()

        else:

            Choose_column=int(Choose_column)

            while True:

                if Choose_column<len(self.board[0]):

                    if  self.board[Choose_row][Choose_column]!=":_:":

                        Choose_column=int(input("invalid try agaaaaaaaainnniiiinnninninin"))

                    else:

                        break
                else:

                    Choose_column=int(input("index out of range try again"))

            self.ask_numero(Choose_row,Choose_column)

    def ask_numero(self,Choose_row,Choose_column):

        ask_numero=input("which numero do you want ot place on yout chossen place for this box M8")

        while True:

            if ask_numero in self.numeros:

                self.board[Choose_row][Choose_column]=":"+ask_numero+":"

                if  not(self.check_if_wrong_for_box()) or not(check_if_working_for_row(self,Choose_row)) or not(check_if_working_for_column(self,Choose_column)):

                    ask_numero=input("invalid try agaaaaaaaainnniiiinnninninin")

                else:

                    break
            else:

                ask_numero=input("enter a valid numero please")





cube1=Cube()
cube2=Cube()
cube3=Cube()
cube4=Cube()
cube5=Cube()
cube6=Cube()
cube7=Cube()
cube8=Cube()
cube9=Cube()

boards1=[cube1,cube2,cube3]
boards2=[cube4,cube5,cube6]
boards3=[cube7,cube8,cube9]
boards=[boards1,boards2,boards3]


def check_if_working_for_row(box,row):

    test_score=[]

    if box in boards1:

        boardsss=boards1

    elif box in boards2:

        boardsss=boards2

    else:

        boardsss=boards3

    for i in boardsss:

        for j in i.board[row]:

            test_score.append(j)

    p=0

    for i in test_score:

            w=0

            for j in test_score:

                if i==j!=":_:" and w!=p :

                    return False

                w+=1

            p+=1

    return True

def check_if_working_for_column(box,column):

    test_score=[]

    if box in boards1:

        for i in boards:

            for j in i[boards1.index(box)].board:

                test_score.append(j[column])

        p=0

        for i in test_score:

                w=0

                for j in test_score:

                    if i==j!=":_:" and w!=p :

                        return False

                    w+=1

                p+=1

        return True

    elif box in boards2:

        for i in boards:

            for j in i[boards2.index(box)].board:

                test_score.append(j[column])

        p=0

        for i in test_score:

                w=0

                for j in test_score:

                    if i==j!=":_:" and w!=p :

                        return False

                    w+=1

                p+=1

        return True


    elif box in boards3:

        for i in boards:

            for j in i[boards3.index(box)].board:

                test_score.append(j[column])

        p=0

        for i in test_score:

                w=0

                for j in test_score:

                    if i==j!=":_:" and w!=p :

                        return False

                    w+=1

                p+=1

        return True




def ask_what_general():

    inputt=int(input("which box do you want to work with"))

    if inputt<3:

        box=boards1[inputt]

    elif inputt<6:

        box=boards2[inputt-3]

    else:

        box=boards3[inputt-6]

    inputt2=input("what do you want to do with the board")

    while inputt2!="delete" and inputt2!="ADD_numero" or inputt2=="delete" and if_cant_delete(box) or inputt2=="ADD_numero" and if_cant_add(box):

        inputt2=input("invaliiiii i i i i i  i  iiiid try againninininin")

    if inputt2=="delete":

        box.delete()

    elif inputt2=="ADD_numero":

        box.ask_to_place_numero()

def if_cant_delete(box):

    test_board=[]

    for i in box.board:

        for j in i:

            test_board.append(j)

    r=0

    for i in box.numeros:

        if ":"+i+":" not in test_board:

            r+=1

    if r==len(box.numeros):

        return True

    return False

def if_cant_add(box):


    test_board=[]

    for i in box.board:

        for j in i:

            test_board.append(j)


    if ":_:" not in test_board:

        return True

    return False

def print_entere_board():

    p=0

    for r in range(len(boards)):

        for i in range(len(cube1.board)):

            for j in boards[r]:

                for f in j.board[i]:

                    print(f,end="")

            print("  ")



print("welcome to sudoku")

print_entere_board()

def Generate_random_sudoku_board():

    inputt=int(input("how many clues for sudoku you want"))

    while inputt>26 or inputt<5:

        inputt=int(input("invalid try again"))

    for i in range(inputt):

        random_boxs_index=random.randint(0,len(boards)-1)

        random_boxs=boards[random_boxs_index]

        boards[random_boxs_index]=random_boxs

        random_box_index=random.randint(0,len(random_boxs)-1)

        random_1_Box=random_boxs[random_box_index]

        random_boxs[random_box_index]=random_1_Box

        Test_board=[]

        for i in random_1_Box.board:

            for j in i:

                Test_board.append(j)

        while ":_:" not in Test_board :

            random_box_index=random.randint(0,len(random_boxs)-1)

            random_1_Box=random_boxs[random_box_index]

            Test_board=[]

            for i in random_1_Box.board:

                for j in i:

                    Test_board.append(j)

        random_row=random.randint(0,len(cube1.board)-1)

        while ":_:" not in random_1_Box.board[random_row]:

            random_row=random.randint(0,len(cube1.board)-1)

        random_column=random.randint(0,len(cube1.board[0])-1)

        while random_1_Box.board[random_row][random_column]!=":_:":

             random_column=random.randint(0,len(cube1.board[0])-1)

        random_numero=random.choice(cube1.numeros)

        Test_board3=deepcopy(random_1_Box)

        random_1_Box.board[random_row][random_column]=":"+random_numero+":"

        while not(random_1_Box.check_if_wrong_for_box) or not(check_if_working_for_row(random_1_Box,random_row)) or not(check_if_working_for_column(random_1_Box,random_column)):

            random_1_Box=Test_board3

            random_numero=random.choice(cube1.numeros)

            random_1_Box.board[random_row][random_column]=":"+random_numero+":"

        boards[random_boxs_index][random_box_index]=random_1_Box

    print("   ")

    print_entere_board()



Do_you_want_to_repeat="yes"

while Do_you_want_to_repeat.lower()=="yes":

    Generate_random_sudoku_board()

    while True:

        ask_what_general()

        print_entere_board()

        g=0

        for i in boards:

            for j in i:

                if if_cant_add(j):

                    g+=1

        if g==len(boards1)*len(boards):

            print("bravoo youuuuu wooon brttt bye have a great time")
            break

    Do_you_want_to_repeat=input("DO you ant to reapet")

    while Do_you_want_to_repeat.lower()!="yes" and Do_you_want_to_repeat.lower()!="no":

        Do_you_want_to_repeat=input("invaliiiid try again")













































































