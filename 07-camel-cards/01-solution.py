FILE_PATH = 'input.txt'
with open(FILE_PATH, 'r') as file:
    lines = file.readlines()


class Hand:

    def __init__(self, line):
        (cards, bid) = line.split(' ')
        self.cards_map = {}
        self.bid = int(bid.strip())
        self.cards = cards
        self.comparable_string = (cards.replace('A', 'E')
                                  .replace('K', 'D')
                                  .replace('Q', 'C')
                                  .replace('J', 'B')
                                  .replace('T', 'A'))
        for card in cards:
            self.cards_map[card] = self.cards_map.get(card, 0) + 1

        different_cards_count = len(self.cards_map.keys())
        if different_cards_count == 1:
            self.type = 'Z_FIVE_OF_A_KIND'
        elif different_cards_count == 2:
            if 4 in self.cards_map.values():
                self.type = 'Y_FOUR_OF_A_KIND'
            else:
                self.type = 'X_FULL_HOUSE'
        elif different_cards_count == 3:
            if 3 in self.cards_map.values():
                self.type = 'W_THREE_OF_A_KIND'
            else:
                self.type = 'V_TWO_PAIRS'
        elif different_cards_count == 4:
            self.type = 'U_ONE_PAIR'
        elif different_cards_count == 5:
            self.type = 'T_HIGH_CARD'
        else:
            raise Exception("Something is wrong")

    def __str__(self):
        return self.cards


hands = [Hand(line) for line in lines]
hands.sort(key=lambda hand: (hand.type, hand.comparable_string))
sum = 0
for (index, hand) in enumerate(hands):
    sum += hand.bid * (index + 1)
print(sum)
