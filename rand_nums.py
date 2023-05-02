import random

def rand_nums():
    num_list = []
    for i in range(4):
        num_list.append(random.randint(0,9))
    print(num_list)

    return num_list


rand_nums()
