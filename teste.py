import random
import os
from time import sleep

deck = ['A', 'K', 'Q', 'J', 10, 9, 8, 7, 6, 5, 4, 3, 2]*16


def deal(deck):
    cards = []
    for i in range(2):
        random.shuffle(deck)
        card = deck.pop()
        cards.append(card)
    return cards

def playAgain():
#    if len(deck) < 20:
        play_again = input("O baralho tem menos de 20 cartas! Quer embaralhar de novo? [ S | N ]\n").lower()
        if play_again == 's':
#            dealer_cards = []
#            player_cards = []
            start()

            
        else:
            exit()

def soma(cards):
    soma = 0

    for card in cards:
        if card == "J" or card == "Q" or card == "K":
            soma +=10
        elif card == "A":
            if soma >= 11:
                soma+=1
            else:
                soma+=11
        else:
            soma+=card
    return soma

def hit(cards):
    card = deck.pop()
    cards.append(card)
    return cards

def clear():

    if os.name == 'posix':
        os.system("clear")

def results(dealer_cards, player_cards):            
    clear()
    print(f'A mão  do dealer é {dealer_cards} (soma: {soma(dealer_cards)})')
    print("")
    print(f'Sua mão é de {player_cards} (soma: {soma(player_cards)})')

def blackJack(dealer_cards, player_cards):
    if soma(player_cards) == 21:
        print(player_cards)
        print("WINNER WINNER, CHICKEN DINNER! PARABÉNS, VOCÊ GANHOU COM UM BLACK JACK.")
        print("-=-"*30)
        playAgain()


    elif soma(dealer_cards) == 21:
        print(dealer_cards)
        print("Que pena, você perdeu! Mais sorte na próxima.")
        print("-=-"*30)
        playAgain()

def compare(dealer_cards, player_cards):


    if soma(player_cards) > 21:
        print(results(dealer_cards, player_cards))
        print("Que pena, você perdeu! Mais sorte na próxima.")
        print("-=-"*30)
    elif soma(dealer_cards ) > soma(player_cards) and soma(dealer_cards) < 21:
        print(results(dealer_cards, player_cards))
        print("Que pena, você perdeu! Mais sorte na próxima.")
        print("-=-"*30)
    elif soma(dealer_cards) > 21:
        print(results(dealer_cards, player_cards))
        print("Parabéns, você ganhou! a Banca estourou.")
        print("-=-"*30)
    elif soma(player_cards) > soma(dealer_cards) and soma(player_cards) < 21:
        print(results(dealer_cards, player_cards))
        print("Parabéns, você ganhou!")
        print("-=-"*30)


def start():
    choice = 0
    clear()
    print("---------------------BEM VINDO AO BLACKJACK DO BREJO!! ---------------------\n")
    player_cards = deal(deck)
    dealer_cards = deal(deck)

    while choice != 's':
        print(f'O dealer mostra a carta {dealer_cards[0]} e esconde a outra!')
        print("")
        print(f'Você tem {player_cards} (Soma: {soma(player_cards)})')
        if blackJack(dealer_cards, player_cards):
            blackJack(dealer_cards, player_cards)
        else:
            choice = input(f'''
Você quer:
C = Comprar
P = Parar
S = Sair
''').lower()
        clear()
        if choice == 'c':
            hit(player_cards)
            while soma(dealer_cards) < 17:
                hit(dealer_cards)
            compare(dealer_cards, player_cards)
            playAgain()
            choice = input(f'''
Você quer:
C = Comprar
P = Parar
S = Sair
''').lower()

                
        elif choice == 'p':
            while soma(dealer_cards) < 17:
                hit(dealer_cards)
            compare(dealer_cards, player_cards)
            playAgain()

        elif choice == 's':
            print("bye")
            exit()
    
if __name__ == "__main__":
    start()


