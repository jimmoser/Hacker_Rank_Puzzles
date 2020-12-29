N = int(input())
working_list = []
for _ in range(N):
    alist = input().split()
    if alist[0] == 'insert':
        working_list.insert(int(alist[1]), int(alist[2]))
    elif alist[0] == 'print':
        print(working_list)
    elif alist[0] == 'remove':
        working_list.remove(int(alist[1]))
    elif alist[0] == 'append':
        working_list.append(int(alist[1]))
    elif alist[0] == 'sort':
        working_list.sort()
    elif alist[0] == 'pop':
        working_list.pop(int(alist[1]))
    elif alist[0] == 'reverse':
        working_list.reverse()