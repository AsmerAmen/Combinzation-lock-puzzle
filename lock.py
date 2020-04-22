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

    print('Trying', ' '.join(clues))

    possible_solutions = [str(number) for number in range(1000)]

    clue_patterns = []
    # reg_list = ['[0 - 9]' for i in range(3)]
    for clue in clues:
        right = int(clue[4])
        wrong = int(clue[6])
        digits = clue[:3]
        clue_specific_patterns = []
        if right == 0:
            pass
        if right == 1:
            if wrong == 0:
                pass
            if wrong == 1:
                for ind in range(len(digits)):
                    reg_line = ['[0-9]' for i in range(3)]
                    reg_line[ind] = digits[ind]
                    for j in range(len(digits)):
                        if j != ind:
                            clue_specific_patterns.append(['^{}{}{}$'.format(*reg_line), [digits[j]], digits])
            if wrong == 2:
                for ind in range(len(digits)):
                    reg_line = ['[0-9]' for i in range(3)]
                    reg_line[ind] = digits[ind]
                    # print(reg_line)
                    clue_specific_patterns.append(['^{}{}{}$'.format(*reg_line),
                                                   [digits[j] for j in range(len(digits)) if j != ind], digits])
        if right == 2:
            pass
        clue_patterns.append(clue_specific_patterns)

    # print(len(clue_patterns))
    # for pat in clue_patterns:
    #     print(pat)

    for clue_pattern in clue_patterns:
        possible_solutions_temp = []
        for trial_str in possible_solutions:
            for patt in clue_pattern:
                is_match = True
                if not re.compile(patt[0]).match(trial_str):
                    is_match = False
                else:
                    for digit in patt[1]:
                        # Check if correct value, wrong place exits.
                        if digit not in trial_str:
                            is_match = False
                        if trial_str.find(digit) == patt[2].find(digit):
                            is_match = False
                # print(is_match, clue_pattern)

                if is_match:
                    possible_solutions_temp.append(trial_str)
        possible_solutions = possible_solutions_temp
    print(possible_solutions)



