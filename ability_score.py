from random import randint

class AbilityScore:
    """Class to represent one ability score """

    def __init__(self):
        """ Roll 1d6 4 times and take the best
            3 to generate an ability score. """

        # First roll 1d6 4 times.
        rolls = []
        for index in range(4):
            rolls.append(randint(1, 6))

        # Then add the 3 highest.
        self.score = 0
        lowest = 6
        for roll in rolls:
            self.score += roll
            if roll < lowest:
                lowest = roll
        self.score -= lowest
        
    def modifier(self):
        """ Based on the score, determine the modifier. """
        return self.score // 2 - 5

    def print(self):
        """ Print the score (used for debugging purposes). """
        print(self.score)
