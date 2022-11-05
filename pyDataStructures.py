#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))

#!/usr/bin/python3
def element_at(my_list, idx):
    if idx >= 0 and idx < (len(my_list)):
        return(my_list[idx])
    else:
        return(None)

#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx >= 0 and idx < (len(my_list)):
        my_list[idx] = element
        return(my_list)
    else:
        return(my_list)

#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for i in range(len(my_list.reverse())):
        print("{:d}".format(my_list[i]))

#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list[:]
    if idx >= 0 and idx < len(my_list):
        new_list[idx] = element
        return(new_list)
    else:
        return(my_list)

#!/usr/bin/python3
def no_c(my_string):
    for i in range(len(my_string)):
        if my_string[i] == 'c' or my_string[i] == 'C':
            my_string = my_string.del[i]
            return(my_string)
        else:
            return(my_string)

