def main():

    people = {
        'John': 'Hi',
        'Jane': 'Hello',
        'Smith': 'Hey'
    }

    for k in people.keys():
        print(k)

    for v in people.values():
        print(v)

    people['Joe'] = 'Hola'

    print_dict(people)

def print_dict(o):
    for x in o:
        print(f'{x}: {o[x]}')

if __name__ == '__main__':
    main()