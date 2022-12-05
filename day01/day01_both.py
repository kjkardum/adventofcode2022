# read input from file  "input.txt"
# each line is a number or a blank line
# grouped lines are summed together
# part 1 answer is the maximum sum
# part 2 answer is the sum of the first 3 maximum sums
# a program should be written in one line, using stuff like lambdas, list comprehensions, generators, etc.
print((lambda c:(c[0],sum(c[:3])))(sorted(map(sum,(map(int,t.split("\n"))for t in open("input.txt").read().split("\n\n"))),reverse=True)))