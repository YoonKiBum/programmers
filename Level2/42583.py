def solution(bridge_length, weight, truck_weights):
    q = [0] * bridge_length
    count = 0
    while q:
        if len(truck_weights) > 0:
            q.pop(0)
            if sum(q) + truck_weights[0] <= weight:
                var = truck_weights.pop(0)
                q.append(var)
            else:
                q.append(0)
            count += 1
        else:
            q.pop(0)
            count += 1
    return count
