import config, os
input_file = os.path.join(config.root_path, 'p02', 'input.txt')


# return game_id and list of tuples for each drawn cube
def parse_line(line):

    # why doesn't this function work in global file scope?
    def flatten(list):
        return [item for sublist in list for item in sublist]

    def parse_draw(draw):
        return [cube.split(" ") for cube in draw.split(", ")]

    game, draws = line.split(": ")
    game_id = int(game[5:])
    draws = [parse_draw(draw) for draw in draws.strip().split("; ")]
    cubes = flatten(draws)
    return (game_id, cubes)


if __name__ == '__main__':
    possible = {"red": 12, "green": 13, "blue": 14}
    with open(input_file, 'r') as file:
        total = 0
        for line in file:
            valid_game = True
            game_id, cubes = parse_line(line)
            # print(game_id, cubes)
            for amount, color in cubes:
                if int(amount) > possible[color]:
                    valid_game = False
                    break
            if valid_game:
                total += game_id

        print("The answer to p02.a is: " + str(total))