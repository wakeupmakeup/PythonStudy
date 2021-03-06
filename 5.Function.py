# 함수 (Function) 
# 함수는 반복적으로 호출해야 하는 코드의 묶음을 하나의 블럭으로 만들어 이름을 붙여 재사용률을 높인 "코드의 묶음"

'''예를 들어, 이를 닦는다를 5살짜리 아이에게 가르친다고 생각해봅시다. 그리고 안타깝게도 아이는 각 단계를 매일 하나하나 알려줘야 한다고 가정해 봅시다.
치약과 칫솔을 꺼낸다 → 치약을 칫솔에 1cm가량 바른다 → 물을 묻힌다 → 윗니를 닦는다 → 아랫니를 닦는다 → 물로 행군다.
만약, 위와 같은 과정을 매일 반복해서 알려줘야 한다면, 귀찮고 짜증나는 일이 될겁니다.
이것을 하나의 함수로 정의를 한다면 아래와 같이 될 것이며, 양치질()이라는 함수의 이름만 호출해주게 되면 :(콜론) 이후에 입력해 놓은실행 코드를 순차적으로 실행하게 됩니다.'''

def 양치질():
    치약과 칫솔을 꺼낸다.
    치약을 칫솔에 1cm가량 바른다.
    물을 묻힌다. 
    윗니를 닦는다.
    아랫니를 닦는다.
    물로 행군다.

# 내장함수 -> 파이썬에는 이미 정의된 함수들이 있다. 

print('asdas') # 괄호안의 내용을 출력하는 함수 
input() #괄호안의 사용자 입력값을 받는 함수 
float() #괄호안의 값을 float로 변환하는 함수 
int() #괄호안의 값을 int로 변환하는 함수

#함수 만들기 ->  def 라는 예약어를 사용합니다.

def greeting():
    print("안녕하세요")
#:(콜론) 뒤에 여러분들이 실행하고자하는 실행코드를 입력하는 것으로 원하는 결과를 기대할 수는 없습니다.
#여기까지는 함수를 정의하는 단계입니다.

# 호출 방법

greeting() 
#안녕하세요가 출력됨. 

#인자(Argument)
# 인자란 함수를 호출할때 전달하는 값을 말합니다. 넘겨 받는 수 또는 값이라고 생각하면 쉽게 이해할 수 있을 듯합니다. 앞서 사용했었던 print 함수에 들어가는 문자열도 인자입니다.

#매개변수(Parameters)
#매개변수는  함수가 정의된 곳에서 변수처럼 사용하는 하는 것을 말합니다.

def greeting(lang): 
    print(lang) 

greeting("안녕하세요")
# 안녕하세요가 출력됩니다. 

#반환값(Return Value)
#종종 함수는 함수가 정의된 곳에서 전달받은 매개변수를 이용해 프로그래머가 의도한 코드를 실행 한 뒤, 계산 결과인 값을 반환 할 수도 있습니다. 이와 같은 상황이라면 당연히 함수를 다른 함수의 인자로 사용 할수도 있겠지요.

def greet():
    return "안녕"

print(greet(), "Connect") #print라는 함수의 greet()라는 인자로 사용 가능.
print(greet(), "Python")

# 안녕 Connect, 안녕 Python으로 출력됩니다. 

# Multiple 매개변수 / 인자 
# 여러개의 매개변수를 받는 함수를 만들 수도 있습니다. 더하기 함수를 한번 만들어 보도록합시다.

def add(left, right): 
    return left + right + right

print(add(1,2))

# 3으로 출력됩니다. 