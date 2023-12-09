import config, os
input_file = os.path.join(config.root_path, 'p01', 'input.txt')


def find_all_occurrences(word, line):
    start = 0
    while start < len(line):
        pos = line.find(word, start)
        if pos == -1:  # No more occurrences
            return
        yield pos
        start = pos + 1


if __name__ == '__main__':
    with open(input_file, 'r') as file:
        number_words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        total = 0
        for line in file:
            # First collect all digits and their position
            digits = [(i, char) for i, char in enumerate(line) if char.isdigit()]

            # Second find all number words and their position. We use the index as their value.
            for word_value, word in enumerate(number_words):
                for pos in find_all_occurrences(word, line):
                    digits.append((pos, str(word_value)))

            # Sort by position
            digits = sorted(digits, key=lambda x: x[0])

            # concat first and last "digit" value to get the calibration value.
            calibration_value = int(digits[0][1] + digits[-1][1])
            total += calibration_value

            #print(line.strip(), digits, calibration_value, total)

        print("The answer to p01.b is: " + str(total))
