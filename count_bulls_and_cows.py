def bulls_and_cows(computer, player):
    bulls = 0
    cows = 0

    for i,j in zip(computer,player):
        if j == i:
            bulls += 1
    
    for i in player:
        if i in computer:
            cows += 1
    cows -= bulls
        
    return bulls, cows
