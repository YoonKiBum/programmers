def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    count = 0
    lost = set(lost)
    reserve = set(reserve)
    temp1 = lost - reserve
    temp2 = reserve - lost
    lost = list(temp1)
    reserve = list(temp2)
    for i in range(len(lost)):
        if len(reserve) <= 0:
            break
        if lost[i] - 1 in reserve:
            reserve.remove(lost[i]-1)
            count += 1
        elif lost[i] + 1 in reserve:
            reserve.remove(lost[i] + 1)
            count += 1
    return n - (len(lost) - count)
