def solution(n):
    arr = []
    while True:
        if n == 0:
            break
        i = n % 3
        arr.append(i)
        n = n // 3
    
    sum = 0
    for i in range(len(arr)):
        sum += (3 ** i) * arr[len(arr) - i - 1]
    return sum
