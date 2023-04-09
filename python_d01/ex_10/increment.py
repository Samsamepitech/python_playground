def increment(lst):

  for i in range(len(lst)):

    if type(lst[i]) == int:

        lst[i] += 1

    return lst