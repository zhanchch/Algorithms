import random
import pprint
from sets import Set
import time
import copy

pp = pprint.PrettyPrinter(indent=4)

def edge_merge(k, v, adjacent_list):
    adjacent_list[k] = filter(lambda a: a != v, adjacent_list[k])

    for i in adjacent_list[v]:
        if i != k :
            adjacent_list[k].append(i)
            for idx, j in enumerate(adjacent_list[i]):
                if j == v:
                    adjacent_list[i][idx] = k

    del adjacent_list[v]

def RContraction(adjacent_list):
    if len(adjacent_list) == 2:
        return adjacent_list

    k = random.choice(adjacent_list.keys())
    v = random.choice(adjacent_list[k])
    edge_merge(k, v, adjacent_list)
    return RContraction(adjacent_list)

#1 2 3 4 7
#2 1 3 4
#3 1 2 4
#4 1 2 3 5
#5 4 6 7 8
#6 5 7 8
#7 1 5 6 8
#8 5 6 7

test_list = {
    "1": ["2", "3", "4", "7"],
    "2": ["1", "3", "4"],
    "3": ["1", "2", "4"],
    "4": ["1", "2", "3", "5"],
    "5": ["4", "6", "7", "8"],
    "6": ["5", "7", "8"],
    "7": ["1", "5", "6", "8"],
    "8": ["5", "6", "7"]
}

input_list = {}
with open("kargerMinCut.txt", "r") as f:
    for line in f.readlines():
        array = line.split("\t")
        input_list[array[0]] = array[1:len(array) - 1]

begin = time.time()

min_cut = 100000
for i in range(100):
    test = copy.deepcopy(input_list)
    r = RContraction(test)
    l = len(r.itervalues().next())
    if l < min_cut:
        min_cut = l
end = time.time()

print end - begin
print min_cut
