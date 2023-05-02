import random

def rand_nums():
    num_list = []

    for i in range(4):
        num = random.randint(0,9)
        while num in num_list:
            num = random.randint(0,9)
        num_list.append(num)

    return num_list


print(rand_nums())
