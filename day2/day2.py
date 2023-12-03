
def get_input(path):
    with open(path, 'r') as f:
        data = []
        for line in f:
            data.append(line.strip())
    return data

#12 red cubes, 13 green cubes, and 14 blue cubes

def part_one(input):
    game_count = 0

    red = 12
    green = 13
    blue = 14
    
    for line in input:
        valid = True

       
        game = int(line.split(':')[0].split(' ')[1])
        rounds = line.split(':')[1].split(';')

        for index, round in enumerate(rounds):
            marbles = round.split(',')
            for marble in marbles:
                val = marble.split(' ')
                num = int(val[1])
                color = val[2]

                if((color == 'red' and num > red) or (color == 'green' and num>green) or (color=='blue' and num>blue)):
                    valid = False
            
        if valid:
            game_count += game
    
    print(f'Part One Answer: --- {game_count} ---')


def part_two(input):
    total = 0

    for line in input:
        color_dict = {'red': 0, 'blue': 0, 'green':0}

       
        game = int(line.split(':')[0].split(' ')[1])
        rounds = line.split(':')[1].split(';')

        for round in rounds:
            marbles = round.split(',')
            for marble in marbles:
                val = marble.split(' ')
                num = int(val[1])
                color = val[2]

                if num>color_dict[color]:
                    color_dict[color] = num
            
        power = color_dict['red']*color_dict['blue']*color_dict['green']
        total += power

    print(f'Part Two Answer: --- {total} ---')


p = get_input('day2.txt')
part_one(p)
part_two(p)
