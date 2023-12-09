import config, os
input_file = os.path.join(config.root_path, 'p01', 'input.txt')


if __name__ == '__main__':
    with open(input_file, 'r') as file:
        total = 0
        for line in file:
            digits = [char for char in line if char.isdigit()]
            calibration_value = int(digits[0] + digits[-1])
            total += calibration_value
            #print(digits[0], digits[-1], calibration_value)
        print("The answer to p01.a is: " + str(total))