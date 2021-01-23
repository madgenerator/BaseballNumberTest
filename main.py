import random

  # 정답 숫자 생성 3개 : 1~9사이 모두 다를것
answer=[0,0,0]
answer[0]=random.randint(1,9) 

'''
1. answer2를 만든다
2. answer1과 answer2가 같은가?
3. 같으면 다시 answer2를 만든다
4. answer1과 answer2가 다를때까지 무한 반복
'''
answer[1]=random.randint(1,9) #1.answer2를 만든다
while(answer[0] == answer[1]): #2.answer1과 answer2가 같은가?
  answer[1]=random.randint(1,9) #3. 다시 answer2를 만든다
  
'''
1. answer3를 만든다
2. answer3과 answer1 또는 answer2가 같은가?
3. 같으면 다시 answer3를 만든다
4. answer3가 answer1과 answer2가 다를때까지 무한 반복
'''

answer[2]=random.randint(1,9) 
while(answer[2]==answer[0] or answer[2]==answer[1]):
  answer[2]=random.randint(1,9) 

# 정답 숫자 Print
# print(answer[0], answer[1], answer[2])

while(True):
  #사용자에게 숫자 3개 입력 받아서 변수에 넣기
  userinput = input("3개의 서로 다른 숫자를 입력하세요:")

  #사용자 입력을 3개의 숫자로 분리
  userAnswer=[0,0,0]

  userAnswer[0] = int(userinput[0])
  userAnswer[1] = int(userinput[1])
  userAnswer[2] = int(userinput[2])

  #print(userAnswer[0],userAnswer[1],userAnswer[2])

  #정답과 비교해서 Strike / Ball /Out 결과 Print
  strikeCount=0
  ballCount=0
  outCount=0

  if(answer[0]==userAnswer[0]):
    strikeCount=strikeCount+1
  elif(answer[1]==userAnswer[0] or answer[2]==userAnswer[0]):
    ballCount=ballCount+1
  else:
    outCount=outCount+1

  if(answer[1]==userAnswer[1]):
    strikeCount=strikeCount+1
  elif(answer[0]==userAnswer[1] or answer[2]==userAnswer[1]):
    ballCount=ballCount+1
  else:
    outCount=outCount+1

  if(answer[2]==userAnswer[2]):
    strikeCount=strikeCount+1
  elif(answer[0]==userAnswer[2] or answer[1]==userAnswer[2]):
    ballCount=ballCount+1
  else:
    outCount=outCount+1

  print(strikeCount,"STRIKE")
  print(ballCount,"BALL")
  print(outCount,"OUT")

  if(strikeCount==3):
    print("정답!! 당신의 승리!! ")
    break
  else:
    print("땡! 다시한번 도전!!")



