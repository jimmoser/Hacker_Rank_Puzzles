sock_list = list(ar.split())   # Takes the string of socks and splits it into a list.
sock_set = set(sock_list)   # Creates a set of the different colors in the collection
sock_dict = dict.fromkeys(sock_set, '')  # Initializes a dictionary with unique colors as keys

for color in sock_set:  # Counts the number of each color sock in the collection
    sock_dict[color] = sock_list.count(color)

print(sock_dict)

total_pairs = 0     # intialize the total number of whole pairs

for color in sock_set:      # Calculates the number of whole pairs in the collection.
    new_pairs = sock_dict[color]//2
    total_pairs += new_pairs

print(total_pairs)
