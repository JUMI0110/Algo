def solution(numbers):
    answer = []
    for i in numbers:
         answer.append(i * 2) # 리스트에 요소 추가 append함수 사용
    return answer

print(solution([1, 2, 3, 4, 5]))
print(solution([1, 2, 100, -99, 1, 2, 3]))