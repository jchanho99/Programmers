# lv.1 pcce 9
# def solution(board, h, w):
#     n = len(board)
#     count = 0
#     dh, dw = [0, 1, -1, 0], [1, 0, 0, -1]

#     for i in range(4):
#         h_check, w_check = h+dh[i], w+dw[i]
#         if (0 <= h_check < n) and (0 <= w_check < n) and (board[h][w] == board[h_check][w_check]):
#             count += 1
    
#     return count


# lv.1 pcce 10
# def solution(data, ext, val_ext, sort_by):
#    data_table = {"code":0, "date":1, "maximum":2, "remain":3}
#    sort_data = [d for d in data if d[data_table[ext]] <= val_ext]
#    sort_data.sort(key=lambda x:x[data_table[sort_by]])

#    return sort_data


# lv.2 FedEx
def solution(order):
    # 1. order 첫 순서와 컨테이너 첫 숫자가 안맞으면 stack에 할당한다.
    #   맞으면 answer += 1
    # 2. 반복:
    #   order 첫 순서와 컨테이너 숫자와 stack pop과 안맞으면 컨테이너 숫자를 다시 stack에 할당한다.
    #   맞으면 order는 그 다음 순서로, 컨테이너면 그 다음 순서로, stack이면 pop
    # 3. 마지막 컨테이너와 stack이 안맞으면 return -1

    stack = []
    available = 0
    container_num = 1

    # 1.
    if order[0] != container_num:
        stack.append(container_num)
        container_num += 1
    else:
        container_num += 1
        available += 1    

    for i in range(1, len(order)):    
        # 3. OUT condition
        if i == (len(order)-1) and (order[i]!= container_num or order[i] != stack[-1]):
            break

        # 2.
        if order[i] == stack[-1]:
            available += 1
            stack.pop()
        elif order[i] == container_num:
            container_num += 1
            available += 1
        else:
            stack.append(container_num)
            container_num += 1

    return available

order = [4,3,1,2,5]	
print(solution(order))