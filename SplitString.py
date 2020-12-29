def merge_the_tools(string, k):
    a = 0       # initializing the index of the substring
    b = k       # initializing where the slice of the substring will end
    for m in range(int(len(string)/k)):     # figures the number of substrings
        t = string[a:b]                     # slices the substring
        new_string = ""                     # initializes the new substring with no repeats
        for letter in t:
            if letter not in new_string:    # checks if a letter is already in the substring
                new_string = new_string + letter    # appends the letter to the string if its not
        a += k
        b += k
        print (new_string)

merge_the_tools("ABDCCCDEF", 3)