def solution(price):
    answer = 0
    if price >= 500000:
        answer = price - (price * 0.2)
    elif 500000 > price >= 300000:
        answer = price - (price * 0.1)
    elif 300000 > price >= 100000:
        answer = price - (price * 0.05) 
    else:
        answer = price  
    return int(answer)

print(solution(150000))
print(solution(100010))
print(solution(580000))
print(solution(80000))
