# 피자 7조각으로 나눠주는 피자집. n명이 먹으려면 몇 판?
def solution(n):
    answer = 0
    if n > 7:
        if n % 7:
            answer = (n // 7) + 1
        else:
            answer = n // 7
    else:
        answer = 1
    return answer

print(solution(7))
print(solution(1))
print(solution(14))