import copy
def solution(skill, skill_trees):
    count = 0
    check = [0] * len(skill)
    for word in skill_trees:
        copyskill = list(copy.deepcopy(skill))
        check = True
        for i in word:
            if i in copyskill:
                res = copyskill[0]
                if res != i:
                    check = False
                    break
                copyskill.pop(0)
        if check: 
            count += 1
    return count
