# Given an image represented by a NxN matrix, where each pixel in the image
# is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

def rotateMatrix(matrix, n):
    for layer in range( n / 2):
        first = layer
        last = n - layer - 1
        for i in range(first, last):
            offset = i - first
            # save left_top
            top = matrix[first][i]

            #left -> top
            matrix[first][i] = matrix[last - offset][first]

            # bottom -> left
            matrix[last - offset][first] = matrix[last][last - offset]

            # right -> bottom
            matrix[last][last - offset] = matrix[i][last]

            # top -> right

            matrix[i][last] = top

'''
# TESTS
def print_matrix(matrix, n):
    for i in range(n):
        line = ""
        for j in range(n):
            line += str(matrix[i][j]) + " "
        print line

tests = [
        [[1, 2],
         [4, 3]],

        [[1, 2, 3],
         [8, 9, 4],
         [7, 6, 5]]
        ]

for test in tests:
    print "test case:"
    print_matrix(test, len(test))
    print "====================="
    print "after rotate:"
    rotateMatrix(test, len(test))
    print_matrix(test, len(test))
    print
'''
