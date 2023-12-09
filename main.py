import sys

# Run advent of code puzzle
def run_puzzle(nr):
    print("Running puzzle", nr)
    exec(open(f"p{nr}/a.py").read())
    exec(open(f"p{nr}/b.py").read())


if __name__ == '__main__':
    nr = str(sys.argv[1]).zfill(2)
    run_puzzle(nr)
