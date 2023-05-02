def input_nums():
    num_list = []
    i = 0

    while i < 4:

        a = int(input('숫자를 입력하세요'))
        
        if a >= 0 and a <= 9:
            if a not in num_list:
                num_list.append(a)
                i += 1
            else:
                print('중복된 값입니다 다시 입력해주세요')
        else:
            print('0~9까지의 숫자를 입력해주세요')
    return num_list

print(input_nums())
