num_a = input()  
num_b = input() 

def mix(num_a, num_b):
    mixed = []
    for a, b in zip(str(num_a), str(num_b)):
        mixed.append(a)
        mixed.append(b)
    return mixed

def calc(mixed):
    while len(mixed) > 2:
        new_num = []
        for i in range(len(mixed) - 1):
            new_num.append(str((int(mixed[i]) + int(mixed[i+1])) % 10))
        mixed = new_num
    return ''.join(mixed)



mixed = mix(num_a, num_b)
calced = calc(mixed)
print(calced)