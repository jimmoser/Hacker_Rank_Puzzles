# Enter your code here. Read input from STDIN. Print output to STDOUT
S = "BANANA"
vowels = ['A', 'E', 'I', 'O', 'U']
a = 0
b = 0
for i, c in enumerate(S):
    if c in vowels:
        b += len(S) - i
        print("VOW:" + str(c))
        print("Kevin: " + str(b))
        print('\n')
    else:
        a += len(S) - i
        print("CON:" + str(c))
        print("Stuart: " + str(a))
        print('\n')
if a == b:
    print("Draw")
elif a > b:
    print('Stuart {}'.format(a))
else:
    print('Kevin {}'.format(b))

