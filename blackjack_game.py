import random


def random_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_cards(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def comparison(user_score, computer_score):
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "You lose, opponent has Blackjack 😨"
    elif user_score == 0:
        return "You win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose ☹️"
    elif computer_score > 21:
        return "Opponent went over. You win.🤩"
    elif user_score > computer_score:
        return "You win 🥳"
    else:
        return "You lose🤐"

print("Black Jack Game ♠️♥️♦️♣️")

def play_game():
    
    user_cards = []
    computer_cards = []
    end_game = False

    for _ in range(2):
        user_cards.append(random_card())
        computer_cards.append(random_card())

    while not end_game:
        user_score = calculate_cards(user_cards)
        computer_score = calculate_cards(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            end_game = True
        else:
            another_card = input("Do you want to draw another card? Type 'y' or 'n': ")
            if another_card == 'y':
                user_cards.append(random_card())
            else:
                end_game = True
            
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(random_card())
        computer_score = calculate_cards(computer_cards)
        
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(comparison(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    play_game()