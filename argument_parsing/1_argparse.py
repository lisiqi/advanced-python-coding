import argparse

# Create the parser
parser = argparse.ArgumentParser(
    description="A script that demonstrates optional arguments."
)

# Add positional arguments
parser.add_argument(
    "filename",
    nargs="?",
    type=str,
    default="myfile.txt",
    help="The name of the file to write to",
)
parser.add_argument(
    "message",
    nargs="?",
    type=str,
    default="Hello World again",
    help="The message to write to the file",
)

# Add optional arguments
parser.add_argument(
    "--verbose", "-v", action="store_true", help="Increase output verbosity"
)
parser.add_argument(
    "--repeat", "-r", type=int, default=1, help="Number of times to repeat the message"
)
parser.add_argument(
    "--encoding", "-e", type=str, default="utf-8", help="File encoding (default: utf-8)"
)

# Parse the arguments
args = parser.parse_args()

# Access the arguments
filename = args.filename
message = args.message
verbose = args.verbose
repeat = args.repeat
encoding = args.encoding

if verbose:
    print(f"Writing to {filename} with encoding {encoding}")

with open(filename, "w", encoding=encoding) as file:
    for _ in range(repeat):
        file.write(message + "\n")

if verbose:
    print(f"Finished writing {repeat} times to {filename}")

# Command: poetry run python 1_argparse.py myfile.txt "Hello World" -v -r 3 -e utf-8
# Output:
## Writing to myfile.txt with encoding utf-8
## Finished writing 3 times to myfile.txt

# Command: poetry run python 1_argparse.py -v -r 5
# Output:
## Writing to myfile.txt with encoding utf-8
## Finished writing 5 times to myfile.txt
# default values of filename and message are used
