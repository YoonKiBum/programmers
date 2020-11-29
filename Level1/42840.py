# https://programmers.co.kr/learn/courses/30/lessons/42840
def solution(answers):
    answer = []
    people_1 = [1, 2, 3, 4, 5] * 2000
    people_2 = [2, 1, 2, 3, 2, 4, 2, 5] * 2000
    people_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    num_of_1 = 0; num_of_2 = 0; num_of_3 = 0
    
    for i in range(len(answers)):
        if answers[i] == people_1[i]:
            num_of_1 += 1
        if answers[i] == people_2[i]:
            num_of_2 += 1
        if answers[i] == people_3[i]:
            num_of_3 += 1
    
    temp = [(num_of_1,1), (num_of_2,2), (num_of_3,3)] 
    temp.sort(reverse = True)
    temp.append((-1, -1))
    
    for i in range(3):
        if temp[i][0] != temp[i+1][0]:
            answer.append(temp[i][1])
            answer.sort()
            return answer
        elif temp[i][0] == temp[i+1][0]:
            answer.append(temp[i][1])
    answer.sort()
    return answer

