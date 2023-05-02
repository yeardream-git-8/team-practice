def input_nums():
    num_list = []
    i = 0

    while i < 4:

        a = int(input('숫자를 입력하세요'))
        
        if a >= 0 and a <= 9:
            num_list.append(a)
            print(i)
            i += 1
        else:
            print('0~9까지의 숫자를 입력해주세요')
    return num_list

print(input_nums())
