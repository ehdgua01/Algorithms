import itertools


class Deck:
    def __init__(self, cards):
        self._cards = cards
        self._pos = 0

    def draw(self, num):
        cards = self._cards[self._pos : self._pos + num]
        self._pos += num
        return cards

    def end_of_deck(self) -> bool:
        return self._pos >= len(self._cards)


def solution(coin, cards):
    num_of_cards_to_draw = 2
    target_numer = len(cards) + 1
    deck = Deck(cards)
    holds = set(deck.draw(len(cards) // 3))
    candidates = set()
    for answer in itertools.count(1):
        if deck.end_of_deck():
            break
        candidates.update(deck.draw(num_of_cards_to_draw))
        if check(holds, holds, target_numer):
            continue
        elif coin and check(holds, candidates, target_numer):
            coin -= 1
            continue
        elif coin > 1 and check(candidates, candidates, target_numer):
            coin -= 2
            continue
        else:
            break
    return answer


def check(left, right, target_number):
    for x in left:
        other = target_number - x
        if other in right:
            left.discard(x)
            right.discard(other)
            return True
    return False
