#  How to make a script dynamic!
def argument(argv=[]):
    count = 1
    if len(argv) == 1:
        print("{} argument:".format(len(argv)))
        for i in argv:
            print("{}: {}".format(count, i))
    elif len(argv) == 0:
        print(".")
    else:
        print("{} arguments:".format(len(argv)))
        for i in argv:
        
            print("{}: {}".format(count, i))
            count +=1


if __name__ == "__main__":

    print(argument([]))
