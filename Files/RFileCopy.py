def main():

    infile = open('lines.txt', 'r')
    outfile = open('lines-copy.txt', 'w')

    for line in infile:
        print(line.rstrip(), file = outfile)
        print('.', end = '', flush = True)

    outfile.close()
    print('\ndone.')

if __name__ == '__main__':
    main()