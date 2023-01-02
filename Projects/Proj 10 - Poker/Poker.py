import rx7 as rx

import itertools
from enum import Enum,auto
# from typing import NamedTuple
from dataclasses import dataclass
from collections import Counter
from typing import List
from pprint import pprint

from addict import Addict





class RANKS(Enum):
    High_Card =        auto()
    Pair =             auto()
    Two_Pairs =        auto()
    Three_of_a_kind =  auto()
    Straight =         auto()
    Flush =            auto()
    Full_House =       auto()
    Four_of_a_kind =   auto()
    Straight_Flush =   auto()


@dataclass
class Card:
    suit: str
    rank: str


class Cards():
    SUITS = list("♦♠♥♣")
    RANKS = list("23456789TJQKA")

    DECK =  list(map(lambda item: Card(item[0],item[1]) , itertools.product(SUITS,RANKS)))




def shuffle_deck(deck,n=1):
    for i in range(n):
        deck = rx.Random.shuffle(deck)
    return deck

def get_random(deck):
    card = rx.random.choose(deck)
    deck.remove(card)
    return card
def get_card(deck):
    #return deck[0]
    return deck.pop(0)


def get_rank(card):
    """Returns rank of a card"""
    return Cards.RANKS.index(card)

def compare_ranks(first,second):
    """
    This function takes 2 cards an returns the one with higher rank
    """
    if get_rank(first) > get_rank(second):
        return 1
    elif get_rank(first) < get_rank(second):
        return 2
    else:
        return 0




def get_result(hole,community):
    """
    takes 2 params:
        hole: list[card,card]
        cummunity: list[card x5]
    
    returns RESULT,ADDITION
        RESULT: RANKS.MEMBER
        ADDITION: dict
            won= "won":"card_rank"
            cr = "card_rank"

            Highcard:
                { "HCs": [*high_cards] }
            Pair:
                { won , "kickers": [*kickers] }
            Two Pairs:
                { "high_pair":cr , "low_pair":cr , "kicker":cr }
            Three of a kind:
                { won , "kickers":[*kickers] }
            Straight:
                { won }
            Flush:
                { won , HC1:cr , HC2:cr }
            Full House:
                { won3 , won2 }
            Four of a kind:
                { won , "kicker":cr }
    """

    RESULT = RANKS.High_Card
    ADDITION = {}

    ranks =  [card.rank for card in hole+community]
    suits =  [card.suit for card in hole+community]
    won   =  None
    # print(ranks)


    ranks_set_hc = sorted(ranks, key=lambda x:Cards.RANKS.index(x))[::-1]



    #] Flush Check
    suit_frequent = Counter(suits).most_common()[0]
    if suit_frequent[1] >= 5:
        RESULT = RANKS.Flush
        ADDITION["won"] = suit_frequent[0]
        ADDITION["HC1"] = ranks_set_hc[0]
        ADDITION["HC2"] = ranks_set_hc[1]

    #] Straight
    if RESULT != RANKS.Flush:
        ranks_set = sorted(list(set(ranks)), key=lambda x:Cards.RANKS.index(x)) [::-1]
        for i,nom in enumerate(ranks_set):
            new = []
            for n in range(5):
                try:
                    new.append(nom-n)
                except (TypeError):
                    x = Cards.RANKS[Cards.RANKS.index(nom)-n]
                    new.append(x)

            if new==ranks_set[i:i+5]:
                RESULT = RANKS.Straight
                ADDITION["won"] = new[0]
                # ADDITION["list"] = [card for card in new]
                break

    frequency = {item[0]:item[1] for item in Counter(ranks).most_common() if item[1] > 1}
    # print(frequency)

    #] Rest of Ranks
    if frequency:
        keys = list(frequency.keys())
        vals = list(frequency.values())
        
        # Quads
        if   vals[0] == 4:
            RESULT = RANKS.Four_of_a_kind
            # ADDITION["won"] = keys[0]
            ADDITION = {"won":keys[0]} #clearing straight:list
            for card in ranks_set_hc:
                if card != ADDITION["won"]:
                    ADDITION["kicker"] = card
                    break
        
        elif vals[0] == 3:
            # Full House
            if vals[1:]: #If there's anything remaining, means it is full house
                RESULT = RANKS.Full_House
                ADDITION = {}
                ADDITION["won3"] = sorted([i for i in keys if (frequency[i]==3)], key=(lambda x:Cards.RANKS.index(x))) [-1]
                ADDITION["won2"] = sorted([i for i in keys if (i != ADDITION["won3"])], key=lambda x:Cards.RANKS.index(x))[-1]
                if len(list(frequency.keys()))>2:
                    rx.style.print(frequency,"red")
            # skip because of Flush/Straight
            elif RESULT in (RANKS.Flush,RANKS.Straight):
                pass # only Quads and FullHouse are better than Straight/Flush
            # Triple
            else:
                RESULT = RANKS.Three_of_a_kind
                ADDITION["won"] = keys[0]
                ADDITION["kickers"] = []
                # Because there is ONLY 3 similar cards and not more
                #   (it is checked in full-house) we can check the kicker like below
                for card in sorted(ranks_set_hc, key=lambda x:Cards.RANKS.index(x)) [::-1]:
                    if card != ADDITION["won"]:
                        ADDITION["kickers"].append(card)
                ADDITION["kickers"] = ADDITION["kickers"][:2]

        elif vals[0] == 2 and (RESULT not in (RANKS.Flush,RANKS.Straight)):
            # 2 Pairs
            if vals[1:]:
                RESULT = RANKS.Two_Pairs
                freq_sorted = sorted(keys, key=lambda x:Cards.RANKS.index(x))[::-1]
                ADDITION["high_pair"] = freq_sorted[0]
                ADDITION["low_pair" ] = freq_sorted[1]
                for card in ranks_set_hc:
                    if card not in (ADDITION["high_pair"],ADDITION["low_pair"]):
                        ADDITION["kicker"] = card
                        break
            # Pair
            else:
                RESULT = RANKS.Pair
                ADDITION["won"] = keys[0]
                ADDITION["kickers"] = []
                for card in ranks_set_hc:
                    if card != ADDITION["won"]:
                        ADDITION["kickers"].append(card)
                ADDITION["kickers"] = ADDITION["kickers"][:3]

    if RESULT == RANKS.High_Card:
        ADDITION["HCs"] = []
        for card in ranks_set_hc[:5]:
            ADDITION["HCs"].append(card)


    return RESULT,ADDITION




def Compare_Results(player1_result:list, player2_result:list):
    """
    Gets 2 params that each are generated by Get_Result
    Return 1 if player 1 is winner
    And 2 if player 2 is winner
    0 only if it's split.
    """
    res1, addition_1 = player1_result
    res2, addition_2 = player2_result
    
    if player1_result[0].value > player2_result[0].value:
        return 1
    elif player1_result[0].value < player2_result[0].value:
        return 2
    
    # else:

    if res1 == RANKS.High_Card:
        for i in range(7):
            winner_by_kicker = compare_ranks(addition_1["HCs"][i], addition_2["HCs"][i])
            if winner_by_kicker:
                return winner_by_kicker            
        else:
            return 0


    if res1 == RANKS.Pair:
        if  winner_by_pair := compare_ranks(addition_1["won"], addition_2["won"]):
            return winner_by_pair

        for i in range(3):
            if  winner_by_kicker := compare_ranks(addition_1["kickers"][i], addition_2["kickers"][i]):
                return winner_by_kicker            
        return 0


    if res1 == RANKS.Two_Pairs:
        """
        for type_ in ("high_pair","low_pair","kicker"):
            if  winner := compare_ranks(addition_1[type_], addition_2[type_]):
                return winner
        print("split")
        return 0
        """
        if  winner_h_pair := compare_ranks(addition_1["high_pair"], addition_2["high_pair"]):
            # rx.style.print(addition_1["high_pair"],'red')
            return winner_h_pair
        if winner_l_pair := compare_ranks(addition_1["low_pair"], addition_2["low_pair"]):
            # rx.style.print(addition_1["low_pair"],'red')
            return winner_l_pair
        if winner_by_kicker := compare_ranks(addition_1["kicker"], addition_2["kicker"]):
            # rx.style.print(addition_1["kicker"],'red')
            return winner_by_kicker
        print("split")
        return 0


    if res1 == RANKS.Three_of_a_kind:
        if  winner_by_triple := compare_ranks(addition_1["won"], addition_2["won"]):
            return winner_by_triple
        for i in range(2):
            if  winner_by_kicker := compare_ranks(addition_1["kickers"][i], addition_2["kickers"][i]):
                return winner_by_kicker            
        return 0



    if res1 == RANKS.Straight:
        return  compare_ranks(addition_1["won"], addition_2["won"])  


    if res1 == RANKS.Flush:
        for type_ in ("HC1","HC2"):
            if  winner := compare_ranks(addition_1[type_], addition_2[type_]):
                return winner
        return 0


    if res1 == RANKS.Full_House:
        for type_ in ("won3","won2"):
            if  winner := compare_ranks(addition_1[type_], addition_2[type_]):
                return winner
        return 0


    if res1 == RANKS.Four_of_a_kind:
        for type_ in ("won","kicker"):
            if  winner := compare_ranks(addition_1[type_], addition_2[type_]):
                return winner
        return 0




@dataclass
class Player:
    name:str
    credit = 100

    cards  = ...  #: List[Card]
    result = ...
    bet = 0

    def __str__(self):  return self.name
    def __repr__(self): return self.name

    def __hash__(self):
        x = "".join([str(ord(letter)) for letter in list(self.name)])
        return int(x)


Players = list()
def Add_Player(name):
    Players.append(Player(name))
    return Players[-1]

player1 = Add_Player("Ramin")
player2 = Add_Player("Kia")
player3 = Add_Player("AmirReza")
player4 = Add_Player("Ghazale")
player5 = Add_Player("Amir")




def Bet(players,community):
    pot = 0
    active_players = {player:True for player in players}

    def get_actives(actives):
        return [player for player in actives if actives[player]==True]

    current_bet = 0
    stage = 0  #0:Pre-Flop 1:Flop 2:Turn 3:"River" 4:"Final"
    c = {}
    while True:
        for player in get_actives(active_players):
            # if active_players[player] != True:   continue
            rx.cls()

            rx.style.print(stage,"red")
            rx.style.print(c,'red')

            print(active_players)
            for p in get_actives(active_players):
                # if active_players[p]:
                    print(f"{p}:{p.bet}  ", end="")
            print(f"|   Pot: {pot}")

            if player.credit+player.bet <= current_bet:
                options = ["all-in","fold"]
            else:
                if current_bet: 
                    options = ["call","raise","fold"]
                else:
                    options = ["bet","check","fold"]

            print(f"\nCurrent Bet:  {current_bet}$")
            for i,option in enumerate(options,1):
                print(f"    {i}) {option}")
            options_dict = {str(i+1):options[i] for i in range(len(options))}
            option = rx.io.selective_input(f"{player}> ", options_dict)

            if option == "check": pass
            elif option == "call":
                player.credit += player.bet
                player.credit -= current_bet
                player.bet += current_bet
            elif option == "bet":
                bet = int(rx.io.wait_for_input("Amount: "))
                player.credit    -=  bet
                player.bet +=  bet
                current_bet = bet
            elif option == "raise":
                bet = int(rx.io.wait_for_input("Amount: "))
                player.credit    -= bet
                player.bet += bet
                current_bet = bet
            elif option == "fold":
                pot += player.bet
                player.bet = 0
                active_players[player] = False
            elif option == "all-in":
                pass


            c = set([player.bet for player in get_actives(active_players)])
            if len(c) == 1:
                for player in active_players:
                    player.bet = 0
                pot += current_bet*len([player.bet for player in get_actives(active_players)])
                current_bet = 0

        if len(get_actives(active_players)) == 1:
            stage = 4

        if not current_bet:
            if stage == 4:
                print("end")
                break
            else:
                stage += 1
            rx.terminal.run("pause")













ROUND_NOM = 0
PLAY = True
while PLAY:
    ROUND_NOM += 1
    rx.cls()

    Deck = shuffle_deck(Cards.DECK,3)
    community = [get_card(Deck) for _ in range(5)]
    print("".join(sorted([i.rank for i in community])), "".join([i.suit for i in community]))
    print()

    Round_Dict = {}
    #] Deal Hole Cards
    for player in Players:
        # print(player)

        player.cards = [get_card(Deck),get_card(Deck)]
        print([i.rank for i in player.cards],[i.suit for i in player.cards], end="  |  ")

        player.result = get_result(player.cards, community)
        print(player.result[0].name, player.result[1])


        Round_Dict[player] = {"cards":player.cards, "result":player.result}

        print()


    """
    draw = []
    last_winner = Players[0]
    for i,player in enumerate(Players[1:],1):
        a = Compare_Results(Round_Dict[last_winner]["result"], Round_Dict[player]["result"])
        if a==1:
            pass
            # print(player)
        elif a==2:
            last_winner = player
            draw.clear()
            # print(last_winner)
        elif a==0:
            draw.append(player)
    
    print(last_winner)
    print(draw)
    """
    Bet(Players,community)
    # res = Compare_Results(Round_Dict[player1]["result"], Round_Dict[player2]["result"])
    # if RANKS.Four_of_a_kind  in  (Round_Dict[Players.player1][1][0],Round_Dict[Players.player2][1][0]): break


    break





# print(ROUND_NOM)
# pprint(res)



# print(Round_Dict)

# print("\n")
# print(Deck[:7])
# print(Deck)
