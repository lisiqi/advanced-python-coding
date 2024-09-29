import getopt
import sys

filename = "test.txt"  # default values
message = "Hello"  # default values

opts, args = getopt.getopt(sys.argv[1:], "f:m:", ["filename", "message"])
print(opts)
print(args)

for opt, arg in opts:
    if opt == "-f":
        filename = arg
    elif opt == "-m":
        message = arg

with open(filename, "w") as file:
    file.write(message)

# Command: poetry run python 2_getopt.py text.txt Hello\ World
# Output:
## []  # opts
## ['text.txt', 'Hello World']  # args

# Command: poetry run python 2_getopt.py -f text.txt -m Hello\ World
# Output:
## [('-f', 'text.txt'), ('-m', 'Hello World')]  # opts
## []  # args

# Command: poetry run python 2_getopt.py -m Hello\ World
# Output:
## [('-m', 'Hello World')]  # opts
## []  # args
# Default value of filename is used

# Command: poetry run python 2_getopt.py
# Output:
## []  # opts
## []  # args
# Default values are used
