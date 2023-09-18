import random


class BlackJack:
    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()
        self.player_playing = True
        self.dealer_playing = True

    def driver(self):
        player_choice = input("\nWould you like to play BlackJack: Yes or No? ").lower()
        while True:
            if player_choice in ('y','yes'):
                self.new_game()
                self.play_game()
                self.game_decider()
                play_again = input("\nWould you like to play again: Yes or No? ").lower()
                if play_again in ('n','no'):
                    print("\nquitting Blackjack...\n")
                    break
            elif player_choice in ('n','no'):
                print("\nquitting Blackjack...\n")
                break
         
            else:
                print("\nInvalid resposne. Try again.")

    def new_game(self):
        self.player.player_hand.clear()
        self.dealer.dealer_hand.clear()
        self.player_playing = True
        self.dealer_playing = True

    def deal_card(self, hand):
        card = self.deck.deal_card()
        hand.add_card(card)

    def show_dealer_hand(self):
        if len(self.dealer.dealer_hand) == 2:
            return self.dealer.dealer_hand[0]
        elif len(self.dealer.dealer_hand) > 2:
            return self.dealer.dealer_hand[0], self.dealer.dealer_hand[1]

    def game_decider(self):
        player_total = self.player.total()
        dealer_total = self.dealer.total()

        print(f"Dealer's Hand: {self.dealer.dealer_hand} = {dealer_total}")
        print(f"Your hand: {self.player.player_hand} = {player_total}")

        if player_total == 21:
            print("\nBlackjack! You win!\n".upper())
        elif dealer_total == 21:
            print("\nBlackjack. Dealer wins.\n")
        elif player_total > 21:
            print("\nBusted. Dealer wins.\n")
        elif dealer_total > 21:
            print("\nDealer busts! You win!\n".upper())
        elif dealer_total > player_total:
            print("\nDealer wins.\n")
        elif player_total > dealer_total:
            print("\nYou win!\n".upper())
        else:
            print("\nIt's a Draw!\n")

    def play_game(self):
        for _ in range(2):
            self.deal_card(self.player)
            self.deal_card(self.dealer)

        while self.player_playing or self.dealer_playing:
            print(f"\nDealer's Hand: {self.show_dealer_hand()} and '?'")
            print(f"Your hand: {self.player.player_hand} = {self.player.total()}")
            if self.player_playing:
                player_choice = input("\nWould you like to Hit or Stand? ").lower()
            if self.dealer.total() > 16:
                self.dealer_playing = False
            else:
                self.deal_card(self.dealer)
            if player_choice in ('s', 'stand'):
                self.player_playing = False
            elif player_choice in ('h', 'hit'):
                self.deal_card(self.player)
            else:
                print('Invalid response, hit or stand?')
            if self.player.total() >= 21:
                break
            elif self.dealer.total() >= 21:
                break


class Deck:
    def __init__(self):
        self.cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A']
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()


class Player:
    def __init__(self):
        self.player_hand = []

    def add_card(self, card):
        self.player_hand.append(card)

    def total(self):
        total = 0
        face = ['J', 'Q', 'K']
        for card in self.player_hand:
            if card in range(1, 11):
                total += card
            elif card in face:
                total += 10
            else:
                if total > 11:
                    total += 1
                else:
                    total += 11
        return total


class Dealer:
    def __init__(self):
        self.dealer_hand = []

    def add_card(self, card):
        self.dealer_hand.append(card)

    def total(self):
        total = 0
        face = ['J', 'Q', 'K']
        for card in self.dealer_hand:
            if card in range(1, 11):
                total += card
            elif card in face:
                total += 10
            else:
                if total > 11:
                    total += 1
                else:
                    total += 11
        return total


if __name__ == "__main__":
    game = BlackJack()
    game.driver()

