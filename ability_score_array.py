from ability_score import AbilityScore

class AbilityScoreArray:
    """ Class to represent six ability scores """

    def __init__(self, reroll_if_too_low):
        """ Generate 6 ability scores. """
        # The "reroll_if_too_low" argument determines whether
        # the player should reroll if the ability score
        # array (before racial adjustments) are too low.
        too_low = True
        while too_low:
            self.scores = []
            for index in range(6):
                self.scores.append(AbilityScore())
            if reroll_if_too_low:
                too_low = self.too_low()
            else:
                too_low = False

    def too_low(self):
        """ Determine whether this array is too low. An array is
            defined as "too low" if the total modifiers are 0 or
            less, or if the highest score is 13 or lower. """
        highest_score = 0
        total_modifiers = 0
        for ability_score in self.scores:
            if ability_score.score > highest_score:
                highest_score = ability_score.score
            total_modifiers += ability_score.modifier()
        return ((total_modifiers <= 0) or (highest_score <= 13))

    def average(self):
        """ Determine the average of the 6 scores. This
            average is expressed as the "whole" portion and
            the remainder number of sixths as the modulus. """
        sum = 0
        for score in self.scores:
            sum += score.score
        whole_portion = sum // 6
        remainder = sum % 6
        return (whole_portion, remainder)

    def print(self):
        """ Print the scores (used for debugging purposes). """
        for score in self.scores:
            score.print()
