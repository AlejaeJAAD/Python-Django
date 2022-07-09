def main():
    # or you can do...
    # x = ('John', 'Jane', 'Seith', 'Raul', 'Jack')
    # people(*x)
    people('John', 'Jane', 'Seith', 'Raul', 'Jack')

    # or you can do...
    # x = dict(john = 'Hello', jane = 'Hi', smith = 'Hey')
    # peopleWithKeywordsArguments(**x)
    peopleWithKeywordsArguments( john = 'Hello', jane = 'Hi', smith = 'Hey')

def people(*args):
    if len(args):
        for name in args:
            print(name)
        print("\n")
    else:
        print('Nobody')

def peopleWithKeywordsArguments(**kwargs):
    if len(kwargs):
        for name in kwargs:
            print( f'{name} says {kwargs[name]}' )
        print("\n")
    else:
        print('Nobody')

if __name__ == '__main__':
    main()
