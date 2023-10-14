from random import randrange
from typing import Optional

class ScoreGenerator:

    def generate_scores(self, num: int) -> Optional[list[int]]:
        scores: list[int] = []
        if num >= 2:
            while len(scores) != num:
                score = randrange(num)
                if score not in scores:
                    scores.append(score)
                    return scores
        else:
            return