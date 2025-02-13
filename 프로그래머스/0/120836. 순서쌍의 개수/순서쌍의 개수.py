def solution(n):
    number = []
    for i in range(1,n+1):
        if (n % i) == 0:
            number.append(i)
    answer = len(number)
    return answer