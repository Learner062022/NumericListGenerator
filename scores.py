from random import randrange


class ScoreGenerator:

    scores: list = []
    score = None

    def generate_scores(self, num: int):
        while len(self.scores) != num - 1:
            self.score = randrange(num)
            if self.score not in self.scores:
                self.scores.append(self.score)
