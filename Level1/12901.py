def solution(a, b):
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ans = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    index = a - 1 
    day = b - 1
    
    sum = 0
    for i in range(index):
        sum += month[i]
    sum += day
    sum = sum % 7
    return ans[sum]
