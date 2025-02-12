def solution(slice, n):
    if (n / slice - n // slice) > 0:
        answer = n // slice + 1
    else:
        answer = n // slice
    return answer