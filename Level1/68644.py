from itertools import combinations

def solution(numbers):
    answer = []
    for combination in combinations(numbers, 2):
        x = int(combination[0])
        y = int(combination[1])
        answer.append(x+y)
    answer = set(answer)
    answer = list(answer)
    answer.sort()
    return answer
