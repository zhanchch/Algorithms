def two_sum(h_table, t):
    for i in h_table:
        j = t - i
        if j != i and j in h_table:
            return True

    return False

def prob_two_sum(h_table):
    # [-10000, 10000]
    count = 0
    for i in range(-10000,10001):
        if two_sum(h_table, i):
            count = count + 1
    return count

#test_files = ["100.txt", "1000.txt", "10000.txt", "100000.txt"]
#test_files = ["test_Q1_01.txt", "test_Q1_02.txt"]
test_files = ["algo1-programming_prob-2sum.txt"]

for filename in test_files:
    h = {}
    with open(filename, "r") as f:
        for line in f:
            i = int(line)
            h[i] = True

    print prob_two_sum(h)
