import copy
def turn(key, m):
    turn_key = [[0]*m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            turn_key[i][j] = key[m-j-1][i]            
    return turn_key

def check(array):
    num = len(array) // 3 
    for i in range(num, num *2):
        for j in range(num, num *2):
            if array[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    
    array = [[0]*(n*3) for _ in range(n*3)]
    for i in range(n):
        for j in range(n):
            array[i+n][j+n] = lock[i][j]
    
    copy_key = copy.deepcopy(key)
    for i in range(4):
        copy_key = turn(copy_key, m)
        for i in range(n*2):
            for j in range(n*2):
                for a in range(m):
                    for b in range(m):
                        array[a+i][b+j] += copy_key[a][b]
                if check(array):
                    return True
                for a in range(m):
                    for b in range(m):
                        array[a+i][b+j] -= copy_key[a][b]
    return False
                    
