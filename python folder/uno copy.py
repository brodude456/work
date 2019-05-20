import random
import copy

class Card():

    def __init__(self,number,couler):

        self.number=number
        self.color=couler

    def show_card(self):

        print (self.number , self.color)

specal_cards=[Card(50,"Draw_four"),Card(20,"Draw_two")]

class Deck():

    def __init__(self):

        self.cards=[]
        self.cards_rc=[]

    def give_cards(self,how_much,player):
        if len(self.cards)<how_much:
                self.recycle_cards()

        for i in range(how_much):
            player.cards.append(self.cards[0])
            self.cards.remove(self.cards[0])

    def recycle_cards(self):

        if not(len(self.cards)<1):

            cards_toad=[self.cards_rc[0:len(self.cards_rc)-len(self.cards)]]

        elif len(self.cards)<1:

             cards_toad=[self.cards_rc[0:len(self.cards_rc)-1]]

        random.shuffle(cards_toad)

        for i in cards_toad:

            self.cards.append(i)
            self.cards_rc.remove(i)


    def shufle(self):

        random.shuffle(self.cards)

    def show_rc(self):

       self.cards_rc[-1].show_card()

    def restart(self,How_much,players):

        for i in self.cards_rc:
            self.cards.append(i)
            self.cards_rc.remove(i)

        self.shufle()
        for player in players:
            self.give_cards(How_much,player)

        for i in range(1):
            self.cards_rc.append(self.cards[0])
            self.cards.remove(self.cards[0])

class Player():

    def __init__(self,name):

        self.name=name
        self.cards=[]
        self.wins=0

    def play(self,deck_object):

        playing_card=input("which card do you want to play your cards are:"+self.name)

        for i in self.cards:
            i.show_card()

        numero,color=playing_card.split("-")
        while Card(numero,color) not in self.cards or numero!=deck_object.cards_rc[-1].number and color!=deck_object.cards_rc[-1].color and color!="Draw_four" and color!="Draw_two":

            playing_card=input("thats invalid please try again niBBa")
            numero,color=playing_card.split("-")

            if color=="Chosee_color":
                numero=50
            couler=input("whidh couler do you want to choose")
            while couler not in ["red","yellow","green","blue"]:
                couler=input("whidt couler do you want to choose")

        deck_object.cards_rc.append(Card(numero,color))
        self.cards.remove(Card(numero,color))

    def  play_card(self,deck_object):

        print(self.name)
        if deck_object.cards_rc[-1] not in specal_cards:

            for i in self.cards:

                if i.number==deck_object.cards_rc[-1].number or i.color==deck_object.cards_rc[-1].color or i in specal_cards or i.color=="Choose couler" :

                    self.play(deck_object)

                return True

            print("you have no maching card so you need to draw 2 cards:)")
            deck_object.give_cards(2,self)

            for i in self.cards:

                if i.number==deck_object.cards_rc[-1].number or i.color==deck_object.cards_rc[-1].color or i in specal_cards or i.color=="Choose couler" :

                    self.play(deck_object)


        elif deck_object.cards_rc[-1]==Card(50,"Draw_four") or deck_object.cards_rc[-1]==Card(50,"Draw_two"):

            if Card(50,"Draw_four") not in self.cards and Card(50,"Draw_two") not in self.cards:

                w=0

                for i in range(len(deck_object.cards_rc)-1,-1,-1):

                    if deck_object.cards_rc[i]==Card(50,"Draw_four"):

                        w+=4

                    elif deck_object.cards_rc[i]==Card(50,"Draw_two"):

                        w+=2

                    elif deck_object.cards_rc[i]!=Card(50,"Draw_four") and deck_object.cards_rc!=Card(50,"Draw_two"):

                        break

                print("now you need to pull"+str(w)+"many cards because you dont have a draw card to counter your oppponent(OOoof)")

                deck_object.give_cards(w,self)

            else:

                playing_card=input("which card do you want to play your cards are:")

                for i in self.cards:
                    i.show_card()

                numero,color=playing_card.split("-")
                while Card(numero,color) not in self.cards or color!="Draw_four" and color!="Draw_two":

                    playing_card=input("thats invalid please try again niBBa")
                    numero,color=playing_card.split("-")

                deck_object.cards_rc.append(Card(numero,color))
                self.cards.remove(Card(numero,color))

deck=Deck()

coulers=["red","blue","yellow","green"]
for i in range(1,10):
    for j in coulers:
        deck.cards.append(Card(i,j))

special_but_less=["skip","reverse"]

for i in special_but_less:
    for j in coulers:
        deck.cards.append(Card(i,j))


reapet_hmmm="yes"

while reapet_hmmm.lower()=="yes":

    players=[]

    number_of_players=int(input("how many players you want"))

    for i in range(number_of_players):

        input222=input("whats your"+str(i)+"player name gonna be")
        players.append(Player(input222))

    deck.restart(7,players)

    indexx=0

    direction=0

    while True:

        deck.show_rc()
        players[indexx].play_card(deck)

        if not(players[0].cards):

            print(players[indexx].name+"won")
            players[indexx].wins+=1

            break

        elif len(players[indexx].cards)==1:

            print("uno for player"+players[indexx].name)

        if indexx==len(players)-1:

            indexx=0

        elif indexx==0 and direction ==-1:
            indexx=len(players)-1

        if deck.cards_rc[-1].number=="Skipp":

            indexx+=direction*2


        elif deck.cards_rc[-1].number=="Reverse":

            direction *= -1

        indexx+=direction

    reapet_hmmm=input("do you want to reapet (hmmmmmmm:))")

    while reapet_hmmm.lower()!="yes" or reapet_hmmm.lower()!="no":


        reapet_hmmm=input("do you want to reapet (hmmmmm:()")




