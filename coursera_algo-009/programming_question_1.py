from inversion import CountInversion

array = []

with open("IntegerArray.txt", "r") as f:
    array = [int(num) for num in f.readlines()]

sorted_array, count = CountInversion(array)

with open("result.txt", "w") as f:
    f.write(str(count))
