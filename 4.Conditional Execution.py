#if문 

x = 5 

if x < 10: # if는 예약어이며, 컴퓨터는 if 다음에 나오는 조건문의 True, False를 판단하게 됩니다. 
    print("작음")# 만약 True인 경우 :(콜론) 아래로 들여쓰기 된 부분을 실행하게 됩니다. 
                       #여기서는 작음이 출력되겠죠
# 비교 연산자는 아는 내용이니 패스 

# 들여쓰기(indentation) -> 파이썬은 들여쓰기를 엄격하게 생각한다. 

x = 5
if x < 10:
#print('smaller')

#위에 코드와 다른점이 없어보이는데 왜 오류가 날까? 이유는 들여쓰기를 하지 않았기 때문. 
#통상 들여쓰기는 탭한번 혹은 스페이스 4번이다. 

#단일 if문 -> 조건문이 참인 경우에만 미리 입력해 놓은 실행코드를 실행하게 됩니다.

# if else 문 -> 첫번째 if문의 조건이 거짓인 경우 else문 이하의 실행코드가 실행됩니다.

 x = 11 

if x < 10:
    print("Smaller")
else:
    print("bigger")

# 11 < 10 은 거짓. 그래서 bigger가 출력. 들여쓰기 명심할것! 

# 다중 분기 (Multi-way decisions) -> 프로그래머의 필요에 의해 조건문들을 추가할 수 있습니다. 

y = 21 

if y < 2:
    print('small')
elif y < 10:
    print('medium')
elif y < 20: 
    print('big')
elif y < 40:
    print('large')
elif y < 100:
    print('huge')
else : 
    print('개쩐다')

# large가 출력된다. 


# try / execpt 
# 파이썬에서는 발생할 수 있는 error에 대해서 프로그래머가 미리 대처를 할 수 있도록 하였습니다. 이는 try / except로 가능합니다.

astr = "123"

try:
    print("hello")
    isInt = int(astr)
    print("world")
except: isInt = "Integer로 변환할 수 없습니다."

print('Doen', isInt)

#hello
#world
#Done 123이 순서대로 출력됨. 