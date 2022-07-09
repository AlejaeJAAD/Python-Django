class Hours:
    fresh = 'I feel fresh'
    tired = 'I feel tired'

    def morning(self):
        print(self.fresh)

    def evening(self):
        print(self.tired)

def main():
    how_i_feel = Hours()
    how_i_feel.morning()
    how_i_feel.evening()

if __name__ == '__main__':
    main()