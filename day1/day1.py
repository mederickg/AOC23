def get_input(path):
    with open(path, 'r') as f:
        data = []
        for line in f:
            data.append(line.strip())
    return data

def day_one(input):
    total = 0
    for line in input:
        nums = []
        for letter in line:
            if letter in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                nums.append(letter)
        leng = len(nums)-1
        first = nums[0]
        last = nums[leng]
        val = int(first+last)
        total += val
    
    print(f'Part One Answer: --- {total} ---')

def day_two(input):
    total = 0
    writen = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    for line in input:
        nums = {}
        for index, letter in enumerate(line):
            if letter in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                nums[index] = int(letter)
        
        for num in writen.keys():
            if num in line:
                findex = line.find(num)
                lindex = line.rfind(num)

                if findex == lindex:
                    nums[findex]= writen[num]
                else:
                    nums[findex]= writen[num]
                    nums[lindex]= writen[num]
        
        indexes = list(nums.keys())
        mini = min(indexes)
        maxi = max(indexes)

        first = nums[mini]
        last = nums[maxi]

        final = int(str(first)+str(last))

        total += final
        
    print(f'Part Two Answer: --- {total} ---')     


p = get_input('day1.txt')
day_one(p)
day_two(p)