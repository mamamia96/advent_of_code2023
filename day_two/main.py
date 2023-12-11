__author__ = 'github.com/mamamia96'

import re

def main(input_path: str):
                    
    color_test = [
        12, #red
        13, #green
        14  #blue
        ]
    
    part_one_answer = 0
    part_two_answer = 0
    
    lines: list[str]
    
    with open(input_path, "r") as f:
        lines = f.readlines()
        
    for line in lines:
        tokens = re.split(':|;', line)
        color_dict = {
            'red':   0,
            'green': 0,
            'blue':  0
        }
        
        for i in range(1, len(tokens)):

            handful = re.split(',', tokens[i])
            
            for j in range(len(handful)):
                split_hand = re.split(' ', handful[j].strip())
                if color_dict.get(split_hand[1]) < int(split_hand[0]):
                    color_dict[split_hand[1]] = int(split_hand[0])
        
        if color_dict.get('red') <= color_test[0] and\
        color_dict.get('green') <= color_test[1] and\
        color_dict.get('blue') <= color_test[2]:
            
            game_id = int(re.split(' ', tokens[0])[1])
            part_one_answer = part_one_answer + game_id

        if color_dict.get('red') < 1: color_dict['red'] = 1
        if color_dict.get('green') < 1: color_dict['green'] = 1
        if color_dict.get('blue') < 1: color_dict['blue'] = 1

        part_two_answer = part_two_answer + (color_dict.get('red') * color_dict.get('green') * color_dict.get('blue'))
    return part_one_answer, part_two_answer

if __name__ == '__main__':
    part_one, part_two = main('input.txt')
    
    print(f'PART ONE: {part_one}\nPART TWO: {part_two}')
