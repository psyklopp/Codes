def change_letter(string, letter, index):  # note string is actually a bad name for a variable
    return string[:index] + letter + string[index+1:]

def leftrotate(s, d):
    tmp = s[d : ] + s[0 : d]
    return tmp

def calculate_next_bit(s1,s2):
    if s1 == s2:
        return str(0)
    else: 
        return str(1)

s = '100001'
output = ''
print('starting state: ', s)
for i in range(0,100):
    next_bit = calculate_next_bit(s[0],s[1])
    output = output + s[0]
    s=leftrotate(s,1)
    s = change_letter(s, next_bit, 5)
    print(s, '-', 'added to right most - XOR of taps:', next_bit, ' | Sequence -> ', output)
    if s == '100001': 
        print('Period: ',i+1)
        ans = output[:36]
        print('The generated sequence: ',ans)
        break

