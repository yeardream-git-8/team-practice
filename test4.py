# 4. 10번 내로 정답 맞추기 
## 10턴이 지나도 정답을 맞추지 못하면 정답을 공개하고 Game Over 메시지를 출력한다.

cnt = 0
while cnt<11:
  if (): #틀렸을 때 다시 수행하는 함수 
    continue
    cnt+= 1
  
  if reply == answer:
    print(answer, "정답입니다")
    break
  else : 
    print("GAME OVER \n 정답 = ", answer)
    

def requestion() : #다시 묻기 
  while True:
    q = input("다시 시작하시겠습니까? \n [1] 다시시작 / [0] 중단")
    if q = 1:
    # 성구님 코드 
    elif q = 2:
      break
    else : 
      print("잘못 입력하셨습니다.")
      continue    

#10턴이 지나도 정답을 맞추지 못하면 정답을 공개하고 Game Over 메시지를 출력한다.
#플레이어가 정답을 맞추거나 Game Over가 되면, 다시 처음부터 게임을 시작할지 종료할지 물어본다.
#이때 플레이어가 1을 입력하면 처음부터 게임을 다시 시작하고 0을 입력하면 게임을 종료한다(그 외의 입력에는 에러를 출력하고 다시 물어본다)
