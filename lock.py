import re
import sys


if __name__ == '__main__':

    # Getting the clues for the arguments
    clues = sys.argv[1:]

    # The regex pattern to validate the clue syntax
    pattern = re.compile('^([0-9]{3})-[0-9]-[0-9]$')

    # No clues were given:
    if len(clues) == 0:
        print('ERROR: no clues given.')
        exit(0)

    # Validate the clues
    for clue in clues:
        # validate the XYZ-R-W syntax
        if not pattern.match(clue):
            print('ERROR: invalid argument: %s' % clue)
            exit(0)
        # Validate R&W for internal consistency
        if int(clue[4])+int(clue[6]) > 3:
            print('ERROR: invalid argument: %s' % clue)
            exit(0)










