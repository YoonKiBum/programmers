def check(answer):
    for i in range(len(answer)):
        x, y, a = answer[i]
        if a == 0: # 기둥 인 경우
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            else:
                return False
        elif a == 1: # 보 인 경우
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y , 1] in answer): 
                continue
            else:
                return False
    return True

def solution(n, build_frame):
    answer = []
    for i in range(len(build_frame)):
        x, y, a, b = build_frame[i]
        if b == 1: # 설치인 경우
            answer.append([x, y, a])
            if check(answer) == False: # 조건에서 어긋난 경우
                answer.pop()
        elif b == 0: # 삭제인 경우
            answer.remove([x, y, a])
            if check(answer) == False: # 조건에서 어긋난 경우
                answer.append([x, y, a])
                
    return sorted(answer)
