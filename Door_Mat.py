# Create a door mat that is N x M wide where M is 3 time N
n_m_string = input("What are the dimensions? (smaller dimension first) ")
a = n_m_string.split()
n, m = int(a[0]), int(a[1])
dec_rows_num = (n-1)//2
pretty = '.|.'
for i in range(dec_rows_num):
    middle_design = (2 * i + 1) * pretty
    print(middle_design.center(m, '-'))
print("WELCOME".center(m, '-'))
for i in range(dec_rows_num):
    other_design = (2 * (dec_rows_num - i) - 1) * pretty
    print(other_design.center(m, '-'))