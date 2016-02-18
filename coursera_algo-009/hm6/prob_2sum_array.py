def binary_search(a, x, lo=0, hi=None):
    hi = hi or len(a)
    med = (hi - lo) / 2


def prob_two_sum(h):
    # [-10000, 10000]
    count = 0
    for i in h:
        if i <

#test_files = ["100.txt", "1000.txt", "10000.txt", "100000.txt"]
test_files = ["test_Q1_01.txt", "test_Q1_02.txt"]
#test_files = ["algo1-programming_prob-2sum.txt"]

for filename in test_files:
    h = []
    with open(filename, "r") as f:
        for line in f:
            i = int(line)
            h.append(i)

    h = sorted(h)
    print prob_two_sum_array(h)

