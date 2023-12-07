FILE_PATH = 'input.txt'
with open(FILE_PATH, 'r') as file:
    lines = file.readlines()


class Hand:

    def __init__(self, line):
        (cards, bid) = line.split(' ')
        self.bid = int(bid.strip())
        self.comparable_string = (cards
                                  .replace('A', 'E')
                                  .replace('K', 'D')
                                  .replace('Q', 'C')
                                  .replace('J', '0')
                                  .replace('T', 'A'))

        cards_map = {}
        for card in cards.replace('J', ''):
            cards_map[card] = cards_map.get(card, 0) + 1

        jokers_count = 5 - len(cards.replace('J', ''))
        different_cards_count = len(cards_map.keys())
        if different_cards_count <= 1:
            self.type = 'Z___FIVE_OF_A_KIND'
        elif different_cards_count == 2:
            if (4 - jokers_count) in cards_map.values():
                self.type = 'Y___FOUR_OF_A_KIND'
            else:
                self.type = 'X___FULL_HOUSE'
        elif different_cards_count == 3:
            if (3 - jokers_count) in cards_map.values():
                self.type = 'W___THREE_OF_A_KIND'
            else:
                self.type = 'V___TWO_PAIRS'
        elif different_cards_count == 4:
            self.type = 'U___ONE_PAIR'
        elif different_cards_count == 5:
            self.type = 'T___HIGH_CARD'
        else:
            raise Exception("Something is wrong")


hands = [Hand(line) for line in lines]
hands.sort(key=lambda hand: (hand.type, hand.comparable_string))
sum = 0
for (index, hand) in enumerate(hands):
    sum += hand.bid * (index + 1)
print(sum)
