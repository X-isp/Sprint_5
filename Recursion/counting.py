def recursion_old(N_lst, K, cnt):
    len_N_lst = len(N_lst) 
    for _ in range(K):  # в конце цикла опрделяется выбывающий элемент
        remainder = cnt % len_N_lst
        cnt += 1
    # значение следующего человека за выбывшим:
    new_beginner = N_lst[(remainder+1) % len_N_lst]
    N_lst.remove(N_lst[remainder])  # удаляю выбывшего
    cnt = N_lst.index(new_beginner)

    item_0, item_1, item_2 = N_lst, K, cnt

    if len(item_0) == 1:
        return print(item_0[0])

    recursion_old(item_0, item_1, item_2)


def recursion(N_lst, K, cnt):
    if len(N_lst) == 1:
        return print(N_lst[0])
    
    len_N_lst = len(N_lst) 
    for _ in range(K):  # в конце цикла опрделяется выбывающий элемент
        remainder = cnt % len_N_lst
        cnt += 1
    # значение следующего человека за выбывшим:
    new_beginner = N_lst[(remainder+1) % len_N_lst]
    N_lst.remove(N_lst[remainder])  # удаляю выбывшего
    cnt = N_lst.index(new_beginner)

    recursion(N_lst, K, cnt)


if __name__ == '__main__':
    N = int(input())
    K = int(input())

    N_lst = [i for i in range(1, N+1)]
    cnt = 0

    recursion(N_lst, K, cnt)