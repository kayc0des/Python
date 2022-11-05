def no_c(my_string):
    for i in range(len(my_string)):
        if my_string[i] == 'h' or my_string[i] == 'H':
            my_string = my_string.remove(i)
            print(my_string)
        else:
            return(my_string)

greetings = "Hello"

no_c("greetings")