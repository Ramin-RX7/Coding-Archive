import rx7 as rx
from dataclasses import dataclass


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









import flet as ft

def Bet_GUI(players,community):
    def main(page):
    

        page.title = "Poker"
        page.vertical_alignment = ft.MainAxisAlignment.CENTER

        pot = 0
        active_players = {player:True for player in players}

        def get_actives(actives):
            return [player for player in actives if actives[player]==True]

        current_bet = 0
        stage = 0  #0:Pre-Flop 1:Flop 2:Turn 3:"River" 4:"Final"
        c = {}


        ft_texts = []        

        ft_active_players = ft.Text("")
        ft_texts.append(ft_active_players)
        page.add(ft_active_players)
        ft_bets_n_pot = ft.Text("")
        ft_texts.append(ft_active_players)
        page.add(ft_active_players)
        
        ft_input_text = ft.Text("")
        ft_texts.append(ft_input_text)
        # page.add(ft_input_text)

        # ft_input = ft.TextField(hint_text="", width=300, visible=False)

        def clear_page():
            for ft_text in ft_texts:
                ft_text.value = ""
            page.update()
        
        while True:
            # tf_active_players.value = ""

            for player in get_actives(active_players):
                # if active_players[player] != True:   continue
                clear_page()
                rx.cls()
                rx.style.print(stage,"red")
                rx.style.print(c,'red')

                print(active_players)
                ft_active_players.value = str(active_players)

                t = ""
                for p in get_actives(active_players):
                    # if active_players[p]:
                        print(f"{p}:{p.bet}  ", end="")
                        t += f"{p}:{p.bet}  "
                print(f"|   Pot: {pot}")
                ft_bets_n_pot.value = t+f"|   Pot: {pot}"
                page.update()
                
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
                # option = rx.io.selective_input(f"{player}> ", options_dict)
                print(f"{player}> ")

                ft_input_text.value = f"{player}> "
                selected = False
                option = None
                def submit_option(page:ft.Page):
                    option = options_dropdown.value
                    submit_btn.visible = False
                    options_dropdown.visible = False
                    selected = True
                submit_btn = ft.ElevatedButton(text="Submit", on_click=submit_option,)
                options_dropdown = ft.Dropdown(
                    width=100,
                    options=[ft.dropdown.Option(option) for option in options],
                )
                submit_btn.visible = True
                options_dropdown.visible = True
                ft_input_text.visible = True
                page.add(options_dropdown,submit_btn)
                while submit_btn.visible:
                    rx.sleep(1)
                    print(selected)
                selected = False
                page.update()

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





            page.update()

            break

    ft.app(target=main)

   # port=8550  view=ft.WEB_BROWSER







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



Bet_GUI(Players,[])