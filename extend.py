def multiplier(*arg):
    iterator = iter(arg)
    iterate = next(iterator)


    for number in iterator:
        iterate *= number

    return iterate
