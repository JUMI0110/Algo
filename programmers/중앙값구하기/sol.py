def solution(array):
    array.sort()
    if len(array) % 2 == 0:
        pre = array[(len(array)//2)-1]
        post = array[(leㅜ(array)//2)]
        return((pre + post)/2)
    else:
        return(array[(len(array)//2)])

print(solution([1, 2, 7, 10, 11]))
print(solution([9, -1, 0]))