def solution(N, stages):
    total = len(stages)
    arr = []
    ans = []
    for i in range(1, N + 1):
        temp = stages.count(i)
        if total > 0:
            fail = temp / total
            total -= temp
            arr.append((fail, -(i)))
        else:
            arr.append((0, -(i)))
    arr.sort(reverse = True)
    
    for i in range(len(arr)):
        ans.append(-(arr[i][1]))
    return ans
