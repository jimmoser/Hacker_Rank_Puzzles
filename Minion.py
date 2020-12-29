string = "BANANA"
string = string.upper()
stu_pts = 0  # Initializes stu's points
kev_pts = 0  # Initializes kev's points
for letter in range(len(string)):
    if string[letter] in ['A', 'E', 'I', 'O',
                          'U']:  # If string begins with a vowel, kevin gets points for the substring
        kev_pts += len(string) - letter
    else:  # If string doesn't begin with a vowel, stuart gets points it.
        stu_pts += len(string) - letter
if stu_pts == kev_pts:
    print("Draw")
elif stu_pts > kev_pts:
    print("Stuart " + str(stu_pts))
else:
    print("Kevin " + str(kev_pts))