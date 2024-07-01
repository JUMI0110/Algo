def solution(n):
    #answer = sum(map(int,n.split()))
    answer = 0
    while n > 0:
        # a: 몫, b: 나머지
        a, b = divmod(n, 10)
        n = a
        answer += b
    return answer

print(solution(1234))
print(solution(930211))