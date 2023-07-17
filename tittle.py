def split_string(string):
    # Splitting based on space delimiter
    list_string = string.split(' ')
    return list_string

def join_string(list_string):

    string = '.'.join(list_string)
    return string
def join_string(list_string):

    string = string.title(list_string)
    return string

string = 'This is a cat'
# Splitting a string
list_string = split_string(string)
print("After Splitting: ",list_string)

# Join list of strings into one
res_string = join_string(list_string)
print("After joining: ",res_string)
