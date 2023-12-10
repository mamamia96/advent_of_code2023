__author__ = 'github.com/mamamia96'

import re

def main(input_path: str):
    
    num_dict = {
        'one'  : '1',
        'two'  : '2',
        'three': '3',
        'four' : '4',
        'five' : '5',
        'six'  : '6',
        'seven': '7',
        'eight': '8',
        'nine' : '9'
    }
    
    lines: list[str]
    
    with open(input_path, "r") as f:
        lines = f.readlines()

    line_numbers: list[int] = []
    valid_chars: list[chr]  = [str(j) for j in range(10)]
    valid_words: list[str]  = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i in range(len(lines)):
        valid_nums = [(j, lines[i][j]) for j in range(len(lines[i])) if lines[i][j] in valid_chars]
        
        for word in valid_words:
            finds = [m.start() for m in re.finditer(word, lines[i])]
            for f in finds:
                valid_nums.append((f, num_dict.get(word)))
            
        valid_nums.sort(key=lambda x : x[0])
            
        if len(valid_nums) <= 1: print(valid_nums)
        line_numbers.append(
            int(valid_nums[0][1] + valid_nums[-1][1])
            )    
            
    return sum(line_numbers)        

if __name__ == '__main__':
    print(main('input.txt'))