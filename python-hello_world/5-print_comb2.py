# Write a program that prints numbers from 0 to 99
for i in range(100):
    end = "" if i == 99 else ", "
    print("{:02d}{}".format(i, end), end='')

print("\n")

    
