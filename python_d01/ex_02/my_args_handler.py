def my_args_handler(*args):

    count = 1
    concat = ""
    for i in args:
        if count < len(args):
            concat += i + ','
        else:
            concat += i
        count +=1


    return concat
    return count
