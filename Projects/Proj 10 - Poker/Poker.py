import rx7 as rx

import itertools
from enum import Enum,auto
# from typing import NamedTuple
from dataclasses import dataclass
from collections import Counter
from typing import List
from pprint import pprint






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




def get_side_result(rank,cards,addition):
    """

    """
    RESULT = []
    ranks =  [card.rank for card in cards]

    if (rank is RANKS.Full_House):
        if len(list(won.keys())) >= 3:
            threes = [i for i in sorted(list(won.keys()),key=lambda x:RANKS.index(x)) if won[i]==3]
            three = max(threes)
            twos = [i for i in sorted(list(won.keys()),key=lambda x:RANKS.index(x))]
            twos.remove(three)
            two = max(twos)
            addition["triple"] = three
            addition["pair"]   = two   
        else:
            print("fullhouse !")
            print(won)
            exit()

    elif (rank is RANKS.Two_Pairs):
        # check if there are 2 or more pairs and sort them
        sortd = sorted(won, key=lambda x:RANKS.index(x)) [::-1]
        RESULT.append(sortd[0])
        RESULT.append(sortd[1])

        for card in sorted(ranks, key=lambda x:RANKS.index(x)) [::-1]:
            if card not in (sortd[0],sortd[1]):
                RESULT.append(card)
                break

    return addition







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
                { won , "kicker":cr }
            Straight:
                { won }
            Flush:
                { won , HC1:cr , HC2:cr }
            Full House:
                { won3 , won2 }
            Four of a kind:
                { won }
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
    if suit_frequent[1] == 5:
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

        elif vals[0] == 3:
            # Full House
            if vals[1:]: #If there's anything remaining, means it is full house
                RESULT = RANKS.Full_House
                # ADDITION["won3"],ADDITION["won2"] = get_fullhouse(frequency)
                ADDITION = {}
                ADDITION["won3"] = keys[0]
                ADDITION["won2"] = keys[1]
            # skip because of Flush/Straight
            elif RESULT in (RANKS.Flush,RANKS.Straight):
                pass # only Quads and FullHouse are better than Straight/Flush
            # Triple
            else:
                RESULT = RANKS.Three_of_a_kind
                ADDITION["won"] = keys[0]
                # Because there is ONLY 3 similar cards and not more
                #   (it is checked in full-house) we can check the kicker like below
                for card in sorted(ranks_set_hc, key=lambda x:Cards.RANKS.index(x)) [::-1]:
                    if card != ADDITION["won"]:
                        ADDITION["kicker"] = card
                        break

        elif vals[0] == 2 and (RESULT not in (RANKS.Flush,RANKS.Straight)):
            # 2 Pairs
            if vals[1:]:
                RESULT = RANKS.Two_Pairs
                if False: #len(vals) > 2:
                    ADDITION["high_pair"],ADDITION["low_pair"]  = get_2pairs(frequency)
                else:
                    ADDITION["high_pair"] = keys[0]
                    ADDITION["low_pair"] = keys[1]
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

    if RESULT == RANKS.High_Card:
        ADDITION["HCs"] = []
        for card in ranks_set_hc:
            ADDITION["HCs"].append(card)


    return RESULT,ADDITION




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

        for i in range(5):
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
            rx.style.print(addition_1["high_pair"],'red')
            return winner_h_pair
        if winner_l_pair := compare_ranks(addition_1["low_pair"], addition_2["low_pair"]):
            rx.style.print(addition_1["low_pair"],'red')
            return winner_l_pair
        if winner_by_kicker := compare_ranks(addition_1["kicker"], addition_2["kicker"]):
            rx.style.print(addition_1["kicker"],'red')
            return winner_by_kicker
        print("split")
        return 0


    if res1 == RANKS.Three_of_a_kind:
        for type_ in ("won","kicker"):
            if  winner := compare_ranks(addition_1[type_], addition_2[type_]):
                return winner
        return 0


    if res1 == RANKS.Straight:
        return  compare_ranks(addition_1["won"], addition_2["won"])  


    if res1 == RANKS.Flush:
        for type_ in ("won","HC1","HC2"):
            if  winner := compare_ranks(addition_1[type_], addition_2[type_]):
                return winner
        return 0


    if res1 == RANKS.Full_House:
        for type_ in ("won3","won2"):
            if  winner := compare_ranks(addition_1[type_], addition_2[type_]):
                return winner
        return 0


    if res1 == RANKS.Four_of_a_kind:
        return compare_ranks(addition_1["won"], addition_2["won"])





@dataclass
class Player:
    name:str
    cards  = ...  #: List[Card]
    result = RANKS.High_Card
    credit = 100

    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name

    def __hash__(self):
        x = "".join([str(ord(letter)) for letter in list(self.name)])
        return int(x)

class Players(Enum):
    player1 = Player("Ramin")
    player2 = Player("Kia")











PLAY = True
while PLAY:

    rx.cls()

    Deck = shuffle_deck(Cards.DECK,3)
    community = [get_card(Deck) for _ in range(5)]
    print("".join(sorted([i.rank for i in community])), "".join([i.suit for i in community]))
    print()

    Round_Dict = {}
    #] Deal Hole Cards
    for player in Players:
        # print(player)

        player.value.cards = [get_card(Deck),get_card(Deck)]
        print([i.rank for i in player.value.cards],[i.suit for i in player.value.cards])

        player.value.result = get_result(player.value.cards, community)
        print(player.value.result[0].name, player.value.result[1])


        Round_Dict[player.value] = [player.value.cards, player.value.result]
        
        print()


    pprint(Compare_Results(Round_Dict[Players.player1.value][1], Round_Dict[Players.player2.value][1]))
        
    break

pprint(Compare_Results(Round_Dict[Players.player1.value][1], Round_Dict[Players.player2.value][1]))



# print(Round_Dict)

# print("\n")
# print(Deck[:7])
# print(Deck)
