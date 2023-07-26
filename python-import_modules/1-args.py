#  How to make a script dynamic!
# import sys

# # Get the number of arguments
# num_args = len(sys.argv) - 1
# arg = sys.argv
# def argument(arg):
#     count = 1
#     if len(arg) == 1:
#         print("{} argument:".format(num_args))
#         for i in arg:
#             print("{}: {}".format(count, i))
#     elif len(arg) == 0:
#         print(".")
#     else:
#         print("{} arguments:".format(num_args))
#         for i in arg:
        
#             print("{}: {}".format(count, i))
#             count +=1


# if __name__ == "__main__":
    
import sys

if __name__ == "__main__":
    # Get the number of arguments (excluding the script name)
    num_args = len(sys.argv) - 1

    # Print the number of arguments and "argument(s)", followed by a colon or period depending on whether there are arguments
    if num_args == 0:
        print("0 arguments.")
    else:
        print("{} argument{}:".format(num_args, "s" if num_args != 1 else ""))

        # Print each argument with its position
        for i, arg in enumerate(sys.argv[1:], start=1):
            print("{}: {}".format(i, arg))


