def main():
    try:
        #x = int('Hello')
        x = 5/0
    except ValueError:
        print("Dont add string to an integer")
    except ZeroDivisionError:
        print("Dont divide by 0")
    except:
        print("Unknown error")
    else:
        print(x)

if __name__ == '__main__':
    main()