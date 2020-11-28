def solution(board, moves):
    answer = [-1]
    count = 0
    for i in range(len(moves)):
        for j in range(len(board)):
            if board[j][moves[i]-1] != 0:
                answer.append(board[j][moves[i]-1])
                board[j][moves[i]-1] = 0
                break
        if len(answer) >= 3 and answer[len(answer)-1] == answer[len(answer)-2]:
            answer.pop()
            answer.pop()
            count += 2
    return count
