def main():
    game = ['Rock', 'Paper', 'Scissors', 'Lizar', 'Spock'] #list

    #access individual item in list
    print(game[1])

    #slice
    print(game[1:3])

    #using step
    print(game[1:5:2])

    #search a list
    i = game.index('Paper')
    print(game[i])

    #append items
    game.append(('Computer'))

    #insert at position
    game.insert(0, 'Computer')

    #remove an item from the end of the list
    x = game.pop()
    print(x)

    #remove from particular indes
    game.pop(3)

    #delete from index
    del game[3]

    #remove by slice
    del game[1:5]

    #join a list
    print(', '.join(game))

    #get count of list item
    print(len(game))
    print("\n")

    #tuple cannot be appended

    #LIST COMPRENENSIVE
    seq = range(11)
    seq2 = [x * 2 for x in seq]
    print("Normal list")
    print_list2(seq)
    print("\n")
    print("Multiplied by 2 list")
    print_list2(seq2)
    print("\n")

def print_list(o):
    for i in o:
        print(i, end = ' ', flush = True)

def print_list2(o):
    for x in o:
        print(x, end = ' ')
        print()

if __name__ == '__main__':
    main()