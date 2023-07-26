#  How to make a script dynamic!
# def argument(argv=[]):
#     count = 1
#     if len(argv) == 1:
#         print("{} argument:".format(len(argv)))
#         for i in argv:
#             print("{}: {}".format(count, i))
#     elif len(argv) == 0:
#         print(".")
#     else:
#         print("{} arguments:".format(len(argv)))
#         for i in argv:
        
#             print("{}: {}".format(count, i))
#             count +=1


# if __name__ == "__main__":

#     print(argument([]))


#!/usr/bin/env python3
import sys

# Get the number of arguments
num_args = len(sys.argv) - 1

# Print the number of arguments and "argument(s)" with a newline
print("{} argument{}.".format(num_args, "s" if num_args != 1 else ""))
    
# Print each argument on a separate line
for i, arg in enumerate(sys.argv[1:], start=1):
    print("{}: {}".format(i, arg))
