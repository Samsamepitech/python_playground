def my_count_words(lst):

    from collections import Counter
    count = Counter(lst)

    print(dict(count))