# Poker hands
# https://projecteuler.net/problem=54
# 29/05/2025

'''
0# High Card: Highest value card.
1# One Pair: Two cards of the same value.
2# Two Pairs: Two different pairs.
3# Three of a Kind: Three cards of the same value.
4# Straight: All cards are consecutive values.
5# Flush: All cards of the same suit.
6# Full House: Three of a kind and a pair.
7# Four of a Kind: Four cards of the same value.
8# Straight Flush: All cards are consecutive values of same suit.
9# Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
'''

def get_value(card):
    
    card_values = {
    "T" : 10,
    "J" : 11,
    "Q" : 12,
    "K" : 13,
    "A" : 14
    }

    try:
        value = int(card[0])
    except ValueError:
        value = card_values[card[0]]
            
    return value


def order_hand(hand):
    values = []
    
    for card in hand:
        values.append(get_value(card))
    
    carta_valor = dict(zip(hand, values))

    #Deepseek
    hand = sorted(hand, key=lambda x: carta_valor.get(x, len(hand)), reverse=True)

    return hand


def rank(hand):
    hand = order_hand(hand)

    # The rank of the hand is either Royal Flush, Straight flush or Flush.
    if is_same_suit(hand):

        for i in range(len(hand) - 1):
            if get_value(hand[i]) - get_value(hand[i+1]) == 1:
                royal_straight = True
            else:
                royal_straight = False
                break
        # The rank of the hand is either Royal Flush or Straight flush.
        highest_card = get_value(hand[0])
        if royal_straight:
            # The rank of the hand is Royal Flush.
            if get_value(hand[0]) == 14:
                return [9, highest_card]
            # The rank of the hand is Straight flush.
            else:
                return [8, highest_card]
        # The rank of the hand is Flush.
        else:
            return [5, highest_card]

    # The rank of the hand is either Four of a kind, Full house, Straight, Three of a kind, Two pairs, One pair or High card.
    else:
        # There are patterns to recognize the hand based on the differences in an ordered hand, we are looking for differences equal to 0.
        card_difference = []
        for i in range(len(hand) - 1):
            card_difference.append( get_value(hand[i]) - get_value(hand[i+1]) )
        
        # IA: Zero pattern for hand
        indices = [i for i, x in enumerate(card_difference) if x == 0]

        # Zeroes are found in the following patterns, note that straight and flush are excluded.
        four_kind = [[0,1,2], [1,2,3]]
        full_house = [[0,2,3], [0,1,3]]
        three_kind = [[0,1], [1,2], [2,3]]
        two_pairs = [[0,2], [0,3], [1,3]]
        one_pair = [[0], [1], [2], [3]]

        for combination in four_kind:
            if indices == combination:
                highest_card = get_value(hand[combination[0]])
                return [7, highest_card]
        
        for combination in full_house:
            if indices == combination:
                highest_card = get_value(hand[combination[0]])
                return [6, highest_card]
        
        for combination in three_kind:
            if indices == combination:
                highest_card = get_value(hand[combination[0]])
                return [3, highest_card]
        
        for combination in two_pairs:
            if indices == combination:
                highest_card = get_value(hand[combination[0]])
                return [2, highest_card]
        
        for combination in one_pair:
            if indices == combination:
                highest_card = get_value(hand[combination[0]])
                return [1, highest_card]
        
        # The rank of the hand is either Straight or High card.
        highest_card = get_value(hand[0])
        if card_difference == [1,1,1,1]:
            return [4, highest_card]
        else:
            return [0, highest_card]
        

def is_same_suit(hand):
    if hand[0][1] == hand[1][1] == hand[2][1] == hand[3][1] == hand[4][1]:
        return True
    else:
        return False


player1 = []
player2 = []

with open("./db/poker.txt", "r") as f:
    player1_wins = 0

    for line in f:
        line = line.split()

        player1 = line[:5]
        player2 = line[5:]

        player1_result = rank(player1)
        player2_result = rank(player2)

        if player1_result[0] > player2_result[0]:
            player1_wins += 1
        elif player1_result[0] == player2_result[0] and player1_result[1] > player2_result[1]:
            player1_wins += 1

print(player1_wins)