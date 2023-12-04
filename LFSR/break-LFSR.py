def leftrotate(s, d):
    tmp = s[d : ] + s[0 : d]
    return tmp

def change_letter(string, letter, index):  # note string is actually a bad name for a variable
    return string[:index] + letter + string[index+1:]

def print_binary_combinations(n):
    every_combination = []
    # Loop through all numbers from 0 to 2^n - 1
    for i in range(1 << n):
        # Convert the current number to a binary string of length n
        binary_str = format(i, '0' + str(n) + 'b')
        every_combination.append(binary_str)
    return every_combination

# take seed
seed = '01010101'
sequence = '0101010111011110'
seed_copy = '01010101'

# calculating the next bit
def get_next_bit(base_stage, taps):
    res = 0
    for i in range(0,8):
        base = int(base_stage[i])
        tap = int(taps[i])
        res = res ^ (base * tap)
    return str(res)

# generate all possible taps
every_combination = print_binary_combinations(8)

for tap in every_combination:
    success = 0
    output = ''
    seed_copy = seed
    while len(output)<16:
        output = output + seed_copy[0]
        next_bit = get_next_bit(seed_copy,tap)
        seed_copy = leftrotate(seed_copy,1)
        seed_copy = change_letter(seed_copy, next_bit, 7)
    if output == sequence:
        print('Found tap: ', tap)
        break

#Found tap -> 11100010

print('Printing the sequence generated with the above tap...')
output = ''
while len(output)<16:
    output = output + seed[0]
    next_bit = get_next_bit(seed,'11100010')
    seed = leftrotate(seed,1)
    seed = change_letter(seed, next_bit, 7)
    print(output)