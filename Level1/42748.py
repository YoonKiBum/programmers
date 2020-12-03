def solution(array, commands):
    n = len(commands)
    answer = []
    for i in range(n):
        start, end, count = commands[i]
        temp = array[start-1:end]
        temp.sort()
        answer.append(temp[count-1])
        
    return answer
