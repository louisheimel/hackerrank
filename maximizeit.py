# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
lists = []
for line in sys.stdin:
    lists += line

input_rows = ''.join(lists).split('\n')
input_rows = list(map(lambda x: list(map(int, x.split(' '))), input_rows))
lists = list(map(lambda x: x[1:], input_rows[1:])) + [[None]]

def flatten(*arr):
    result = []
    for i in range(len(arr)):
        if isinstance(arr[i], list):
            for j in range(len(arr[i])):
                result += [arr[i][j]]
        else:
            result += [arr[i]]
    return result

def permute(*lst):
    result = []
    secondToLast = lst[-2]
    last = lst[-1]
    if (isinstance(last[0], list)):
        for i in range(len(secondToLast)):
            for j in range(len(last)):
                result += [flatten([secondToLast[i]] + last[j])]
    else:
        for i in range(len(secondToLast)):
            result += [flatten([secondToLast[i]] + last)]
    if (len(lst) > 2):
        return permute(*lst[0:-2],result)
    else:
        return list(map(lambda x: x[0:-1], result))

def score(lst, m):
    totalScore = 0
    for i in range(len(lst)):
        totalScore += lst[i]**2
    return totalScore % m

m = input_rows[0][1]
permutations = permute(*lists)
highScore = 0
for i in range(len(permutations)):
    if score(permutations[i], m) > highScore:
        highScore = score(permutations[i], m)
print(highScore)


