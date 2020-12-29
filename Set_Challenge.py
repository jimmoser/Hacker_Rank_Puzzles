first_num = input("How many in the first set? ")
first_list = input("Numbers in the first set: ")
second_num = input("How many in the second set? ")
second_list = input("Numbers in the second set: ")
first_set = set(first_list.split(" "))
second_set = set(second_list.split(" "))
total = len(first_set.union(second_set))
print(total)

# Hacker Rank, best way to do it!
_, a = input(), set(input().split())
_, b = input(), set(input().split())
print(len(a.union(b)))
