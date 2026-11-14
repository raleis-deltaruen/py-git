import sys
line_count = 0

if len(sys.argv) > 2:
    print("Too many arguments given")
    sys.exit()
    
try:

    with open(sys.argv[1]) as file:
        for line in file:
            line_count += 1
            if line.startswith("#") or line == "\n":
                line_count -= 1
    print(line_count)

except FileNotFoundError:
    print("File does not exist")
except IndexError:
    print("File name not given")