from fractions import Fraction
from typing import List


class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def dfs(cards: List[Fraction]) -> bool:
            n = len(cards)
            if n == 1:
                return cards[0] == 24
            for i, x in enumerate(cards):
                for j in range(i + 1, n):
                    y = cards[j]
                    candidates = [x + y, x - y, y - x, x * y]
                    if y:
                        candidates.append(x / y)
                    if x:
                        candidates.append(y / x)
                    new_cards = cards[:j] + cards[j + 1:]
                    for res in candidates:
                        new_cards[i] = res
                        if dfs(new_cards):
                            return True
            return False
        return dfs([Fraction(x) for x in cards])
