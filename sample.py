from ability_score_array import AbilityScoreArray

class Sample:
    """ Class to represent a sample of ability score arrays """

    def __init__(self):
        """ Generate a sample of ability score arrays. """
        SAMPLE_SIZE = 1000000
        total_wholes = 0
        total_sixths = 0
        for index in range(SAMPLE_SIZE):
            ability_score_array = AbilityScoreArray(True)
            wholes, sixths = ability_score_array.average()
            total_wholes += wholes
            total_sixths += sixths
        average = (total_wholes + (total_sixths / 6)) / SAMPLE_SIZE
        print(average)

if __name__ == '__main__':
    sample = Sample()
