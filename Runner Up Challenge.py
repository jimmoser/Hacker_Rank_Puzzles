#n = int(input("How many contestants? "))
arr = "2 3 4 5"
alist = [a for a in arr.split()]
aset = set(alist)
aset.remove(max(alist))
print(max(aset))