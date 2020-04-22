import re
import sys


if __name__ == '__main__':

    # Getting the clues for the arguments
    clues = sys.argv[1:]

    # The regex pattern to validate the clue syntax
    pattern = re.compile('^([0-9]{3})-[0-9]-[0-9]$')

    # No clues were given:
    if len(clues) == 0:
        print('ERROR: Must provide at least one pattern of the form XYZ-R-W.')
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

    # The Solution pool initial list 0-1000
    possible_solutions = [str(number).zfill(3) for number in range(1000)]

    clue_patterns = []
    for clue in clues:
        right = int(clue[4])
        wrong = int(clue[6])
        digits = clue[:3]
        clue_specific_patterns = []

        if right == 0:
            if wrong == 0:
                reg_line = ['[0-9]' for i in range(3)]
                clue_specific_patterns.append(['^{}{}{}$'.format(*reg_line),
                                               [],
                                               [digit for digit in digits],
                                               digits])
            if wrong == 1:
                for ind in range(len(digits)):
                    reg_line = ['[0-9]' for i in range(3)]
                    for j in range(len(digits)):
                        if j != ind:
                            clue_specific_patterns.append(['^{}{}{}$'.format(*reg_line),
                                                           [digits[j]],
                                                           [digit for digit in digits],
                                                           digits])
            if wrong == 2:
                for ind in range(len(digits)):
                    reg_line = ['[0-9]' for i in range(3)]
                    clue_specific_patterns.append(['^{}{}{}$'.format(*reg_line),
                                                   [digits[j] for j in range(len(digits)) if j != ind],
                                                   [digit for digit in digits],
                                                   digits])
        if right == 1:
            if wrong == 0:
                for ind in range(len(digits)):
                    reg_line = ['[0-9]' for i in range(3)]
                    reg_line[ind] = digits[ind]
                    clue_specific_patterns.append(['^{}{}{}$'.format(*reg_line), [], [], digits])
            if wrong == 1:
                for ind in range(len(digits)):
                    reg_line = ['[0-9]' for i in range(3)]
                    reg_line[ind] = digits[ind]
                    for j in range(len(digits)):
                        if j != ind:
                            clue_specific_patterns.append(['^{}{}{}$'.format(*reg_line), [digits[j]], [], digits])
            if wrong == 2:
                for ind in range(len(digits)):
                    reg_line = ['[0-9]' for i in range(3)]
                    reg_line[ind] = digits[ind]
                    clue_specific_patterns.append(['^{}{}{}$'.format(*reg_line),
                                                   [digits[j] for j in range(len(digits)) if j != ind], [], digits])
        clue_patterns.append(clue_specific_patterns)

    # print(len(clue_patterns))
    for pat in clue_patterns:
        print(pat)

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
                        if trial_str.find(digit) == patt[3].find(digit):
                            is_match = False

                    for digit in patt[2]:
                        if len(patt[1]) == 0:
                            if digit in trial_str:
                                is_match = False
                            if trial_str.find(digit) == patt[3].find(digit):
                                is_match = False




                if is_match:
                    possible_solutions_temp.append(trial_str)
        possible_solutions = sorted(list(set(possible_solutions_temp)))
        print('\n', possible_solutions)

    if len(possible_solutions) == 0:
        print('No solutions found.')
    else:
        for index, value in enumerate(possible_solutions):
            print('*** Solution #%d is %s' % (index+1, value))



