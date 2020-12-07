def balanced(p):
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        elif p[i] == ')':
            count -= 1
        if count == 0:
            return i
        
def correct(u):
    count = 0
    for i in range(len(u)):
        if u[i] == '(':
            count += 1
        elif u[i] == ')':
            count -= 1
        if count < 0:
            return False
    return True
 
def solution(p):
    if p == '':
        return p
    answer = ''
    
    index = balanced(p)
    u = p[:index + 1]
    v = p[index + 1:]
    
    if correct(u):
        return (u + solution(v))
    else:
        answer += '('
        answer += solution(v)
        answer += ')'
        u = list(u)
        u = u[1:-1]
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += ''.join(u)
        return answer
