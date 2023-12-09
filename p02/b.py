import config, os
input_file = os.path.join(config.root_path, 'p01', 'input.txt')


with open(input_file, 'r') as file:
    total = 0
    print("The answer to p02.a is: " + str(total))