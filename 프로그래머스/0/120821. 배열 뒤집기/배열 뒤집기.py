def solution(num_list):
    answer = num_list.copy()
    for i in range(len(num_list)):
        answer[(len(num_list)-1)-i] = num_list[i]
    return answer