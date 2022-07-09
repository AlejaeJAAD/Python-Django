def main():
    for i in inclusive_range(5,50,5):
        print(i, end = ' ')
    print()

def inclusive_range(*args):
    numargs = len(args)
    start = 0
    step = 1

    #Initialize parameters
    if numargs < 1:
        raise TypeError(f'Expected atleast 1 argument {numargs}')
    elif numargs == 1:
        stop = args[0]
    elif numargs == 2:
        (start, stop) = args
    elif numargs == 3:
        (start, stop, step) = args
    else:
        raise TypeError(f'Expected atleast 3 arguments got, {numargs}')

    #generator
    i = start
    while i <= stop:
        yield  i
        i = i + step

if __name__ == '__main__':
    main()