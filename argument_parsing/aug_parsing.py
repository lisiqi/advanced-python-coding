import sys

# Usage: poetry run python aug_parsing.py filename "message"


def myfunction(*args, **kwargs):
    print(args)
    print(kwargs)


myfunction(1, 2, 3, 4, 5, name="John", age=20)

print(
    sys.argv
)  # argv[0] is the name of the script, argv[1] is the first argument, argv[2] is the second argument, etc.

filename = sys.argv[1]
message = sys.argv[2]

with open(filename, "w") as file:
    file.write(message)
