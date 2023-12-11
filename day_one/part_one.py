__author__ = 'github.com/mamamia96'

def main(input_path: str):
    
    lines: list[str]
    
    with open(input_path, "r") as f:
        lines = f.readlines()

    line_numbers: list[int] = []
    valid_chars: list[chr]  = [str(j) for j in range(10)]

    for line in lines:
        valid_nums = [ele for ele in line if ele in valid_chars]
        line_numbers.append(int(valid_nums[0] + valid_nums[-1]))
            
    return sum(line_numbers)        
    
    
        
if __name__ == '__main__':
    print(main('input.txt'))
