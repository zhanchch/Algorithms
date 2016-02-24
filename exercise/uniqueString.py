# 1.1 Implement an algorithm to determine if a string has all unique characters.
#     What if you can not use additional data structures?

# case sensitive, do not use additional data structure
def uniqueString(string_input):
    char_count = [0] * 256

    for char in string_input:
        i = ord(char)

        if(char_count[i] > 0):
            return False
        else:
            char_count[i] = 1

    return True

# any characters, use python dictionary
def uniqueString1(string_input):

    char_dict = {}

    for char in string_input:
        if(char in char_dict):
            return False
        else:
            char_dict[char] = True

    return True


test_string = '123f(-asd'

print(uniqueString(test_string))
print(uniqueString1(test_string))
