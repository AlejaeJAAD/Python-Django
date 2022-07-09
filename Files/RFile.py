def main():
    f = open('lines.txt', 'r')
    # f = open('lines.txt', 'r') - Read only
    # f = open('lines.txt', 'w') - Write only (Empty files)
    # f = open('lines.txt', 'a') - Appends the data in files
    # f = open('lines.txt', 'r+') - optional + to read or write

    for line in f:
        print(line.rstrip())

if __name__ == '__main__':
    main()
