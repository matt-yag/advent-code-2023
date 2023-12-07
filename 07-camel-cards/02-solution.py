FILE_PATH = 'input.txt'
with open(FILE_PATH, 'r') as file:
    lines = file.readlines()

CARDS_TO_TYPE = {
    0: lambda cards_map, jokers: 'Z___FIVE_OF_A_KIND',
    1: lambda cards_map, jokers: 'Z___FIVE_OF_A_KIND',
    2: lambda cards_map, jokers: 'Y___FOUR_OF_A_KIND' if (4 - jokers) in cards_map.values() else 'X___FULL_HOUSE',
    3: lambda cards_map, jokers: 'W___THREE_OF_A_KIND' if (3 - jokers) in cards_map.values() else 'V___TWO_PAIRS',
    4: lambda cards_map, jokers: 'U___ONE_PAIR',
    5: lambda cards_map, jokers: 'T___HIGH_CARD',
}


class Hand:

    def __init__(self, line):
        (cards, bid) = line.split(' ')
        self.bid = int(bid)
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
        self.type = CARDS_TO_TYPE[len(cards_map.keys())](cards_map, jokers_count)

    @staticmethod
    def compare(hand):
        return hand.type, hand.comparable_string


hands = [Hand(line.strip()) for line in lines]
hands.sort(key=Hand.compare)
sum = 0
for (index, hand) in enumerate(hands):
    sum += hand.bid * (index + 1)
print(sum)
