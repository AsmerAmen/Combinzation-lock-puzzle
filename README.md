# Objective
- There is a popular puzzle where you try to guess the combination to a lock given some clues. For our
purposes, the lock has exactly three wheels, each with values 0 through 9.
- You must provide the clues on the command line and they must be in the form XYZ-R-W where:
	- XYZ = a possible combination of 3 digits, each digit a member of the set {x ∈ Z | 0 ≤ x ≤ 9}
	- R = number of wheels that show the correct digit
in the correct place within the sequence, each digit a member of the set {1,2,3}
	- W = number of wheels that show the correct digit but
in the wrong place within the sequence, each digit a member of the set {1,2,3}
- The expectation is that you will use a brute force form of technique to solve this puzzle. Iterate through
all 1,000 possible combinations and observe which one(s) correctly meet all specified clues. Do not try to
solve this puzzle the way a human would, using logic.

- For Rules, check the instructions PDF file.

# How to run
```shell script
$ python3 lock.py 874-1-2
$ python3 lock.py 874-1-1 875-1-2
```


