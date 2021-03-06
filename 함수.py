# 입출력을 하기 전에 함수 부터 배워보자
# 함수는 쉽게 말해서 믹서기라고 생각하자. 우리는 믹서기에서 일어난 일을 설계해야한다.
# 입력을 넣어 믹서기(실행)한 후 출력의 결과를 본다고 생각하면 이해가 쉬울 것.

# 함수를 왜쓰냐?
# 똑같은 내용을 반복해서 작성하고 있는 나를 발견할때가 있는데 일르 해결해주는 것이 함수라는 녀석이다.
# 또 자신의 프로그램 흐름을 쉽게 파악하는 것이 가능하다.

# 함수의 구조
import re


def 함수명(입력변수):
    수행할 문장1
    수행할 문장2
    . . .

# 간단한 덧샘 함수를 만들어 보자


def sum(a, b):
    return a+b

# 사용해 보면?


a = 3
b = 4
c = sum(a, b)
print(c)  # ->7

# 입력값과 결과값에 따른 함수의 4가지 형태

# 1. 일반적인 함수
   def 함수명(입력변수):
        수행할 문장
        ...

        return 결과값

# 2. 입력값이 없는 함수
    def say():
        return '안녕'

    # 이런 입력값이 없는 함수는 어떻게 사용할까?

a = say()
print(a)
# 이렇게 사용한다. 출력값은 Hi

# 3. 결과값이 없는 함수
    def sum(a, b):
        print("%d %d의 합은 %d입니다." % (a,b,a+b))

    # 결과값이 없는 함수는 호출해도 돌려주는 값이 없기 때문에 다음과 같이 사용한다.

    sum(3, 4)
    # 즉, 함수이름(입력인자1, 입력인자2, ...)로 불러와서 직접 입력하게 함.
    # 7이라는 결과가 나오는데 왜 결과값이 없다고 하는가? 결과값이라는 것은 return으로만 돌려받는 값을 말한다. 위에 7이 나오는 문장은 기존처럼 하나의 수행할 문장일 뿐이다.


# 4. 입력값이 몇 개가 될지 모른다면?
# 위 같은 상황일 경우 이런게 사용하면 해결 가능하다.


    def 함수명(*입력변수):
        수행할 문장
        . . .

# 예시) 여러 개의 입력값을 받는 함수 만들기.
    def sum_many(*args):  # args라는건 입력 인자라는 뜻이고 관례적으로 사용한다. 
        sum = 0
        for i in args:
            sum = sum + i
        return sum

# 위에서 만든 sum_many라는 함수는 입력값이 몇 개이든 상관이없다. *args처럼 입력 변수명 앞에 *을 붙이면 입력값들을 전부 모아서 튜플로 만들어 주기 때문이다.
# 실행시킨다면?

result = sum_many(1, 2,3,4,5,6,7,8,9)
print(result)
  # 이런식으로 사용하자.


    #재밌게도 함수의 변수로 *args만 사용할 수 있는것은 아니다.
#예시)

def sum_mul(choice, *args):
    if choice == 'sum': # <- 입력 인수 choice에 sum을 입력받았을 때
        result = 0
        for i in args:
            result += i # <- args에 입력받은 모든 값을 더한다.
    elif choice == 'mul':  # <- 입력 인수 choice에 'mul'을 입력받았을 때
        result = 0
        for i in args:
            result *= i  # <- 다 곱해라. 
        return result

# 테스트
result = sum_mul('sum', 1,2,3,4,5)
print(result)
# 15

result = sum_mul('mul', 1,2,3,4,5)
print(result)
# 120


# 항상 기억하자 함수의 결과값은 언제나 하나임을.
    def sum_and_mul(a, b):
        return a+b, a*b
result = sum_and_mul(2, 4)
print(result)

# 엥? 결과가 하나라면서 왜 두개를 리턴하느냐? 이런 의문이 든다면 정상이다.
# 이때의 결과값은 두 가지가 아니라 (a+b,a*b)로 이루어진 하나의 튜플 값으로 나온다!!
# result = (7,12)으로 나오고 만일 이것들 2개의 결과값으로 받은 것 처럼 하고 싶다면 아래처럼 하면 된다.

sum, mul = sum_and_mul(3, 4)

#이렇게 호출하면 sum = 7, mul = 12로 나올 것이다.

# 그럼 반대로 이렇게 한다면?

    def sum_and_mul2(a, b):
        return a+b
        return a*b

result = sum_and_mul2(3, 4)
print(result)

# 결론 부터 말해보자면 어리석다. 먼저 return 값 즉, 결과값은 반드시 하나이기 때문에 a*b에 해당하는 return은 실행되지 않는다.
# 즉 함수는 return을 만나는 순간 결과값을 돌려준 다음 함수를 빠져나간다.(끝난다)
# 이 특성을 이용해서 특정 상황이었을 때 함수를 빠져나가는 법이 있다.

   def say_me(me):
        if me == '바보'
        return
    print("나의 별명은 %s입니다" % me)

# return이 있으니 결과값이 있는거네요?
# 아니다. 틀렸다.
# 위의 함수는 입력값으로 me라는 변수를 받아서 문자열을 출력한다. 이 함수 역시 리턴값은 없다.
# 문자열을 출력한다는 것과 리턴값이 있다는 것은 전혀 다른 말이다. 혼동하지 말자! 함수의 리턴값은 오로지 return문에 의해서만 생성된다.
# 바보라는 값이 들어오면 문자열을 출력하지 않고 함수를 즉시 빠져나간다.


# 입력인수에 초깃값 미리 설정하기
# 아까와는 다른 형태로 함수의 인수를 전달하는 방법이다. 인수에 초깃삾을 미리 설정하여 주는 경우다. 

    def say_myself(name, old, man = True):
        print("나의 이름은 %s입니다." %name)
        print("나이는 %d살입니다." %old)
        if man:
            print("남자입니다.")
        else:
            print("여자입니다.")
        
# man = True 처럼 미리 인수를 넣어준경우를 볼 수 있다. 항상 변하는 것이 아닐 경우 이런식으로 미리 설정하면 유용하다. 
# say_myself 함수는 다음처럼 사용이 가능하다.

say_myself("김이름", 25)
say_myself("김이름", 25, True)

# 위에 두 함수는 같은 출력값을 보여준다. 첫번째로는 성별을 입력하지 않았지만 자동으로 True값으로 초기 설정이 되어있다. 
# True를 False로 바꾸면 남자가 아닌 여자로 바뀔 것이다. 


# 주의 사항 !!!
# 아래 와 같은 코드를 봐보자. 

    def say_myself(name, man=True, old):
    print("나의 이름은 %s입니다." %name)
    print("나이는 %d 살입니다." %old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

# 이런식으로 순서가 봐뀐다면 아래처럼 값을 넣으면 되는거 아닐까? 

say_myself("김이름", 25)

# name에는 김이름이 들어갈 것이다. 하지만 27을 파이썬이 man변수냐 old냐 둘중 정하지 못할 것이다. 그리고 오류가 난다. 
# 즉 초기화 시키고 싶다면 항상 맨 뒤에 위치시키는 것을 잊지 말자! 


# 함수 안에서 선언된 변수의 효력 범위

a = 1 
def vartest(a):
    a += 1

vartest(a)
print(a)

# 이 프로그램을 실행 시키면 당연하게 2가 출력 되어야 할 것 같지만 1이 출력된다. 
# 그 이유는 함수 안에서 새로 만들어진 변수는 '함수 안에서만' 사용되는 '함수만의 변수'이기 때문이다. 
# 쉽게말하면 밖에 나와있는 a와 함수 안에서의 a는 다르다. 


# 그러면 서로는 불가침 영역이라는 말인데 이를 이요해서 프로그램을 만들수는 없는건가? 
# 두가지를 이용하면된다. 

# 1.return 이용하기 
    a = 1
    def vartest(a): 
        a += 1
        return a
a = vartest(a) 
print(a) 


# 2. global 이용하기. 

    a = 1
    def vartest():
        global a
        a += 1 

vartest()
print(a)

# global이 뭔데? 
# global a 를 기준으로 말하자면 함수 밖의 a 변수를 직접 사용하겠다는 뜻이다. 
# 하지만 사용하지 않는 것이 좋은데 함수는 독립적으로 존재하는 것이 좋기 떄문이다. 외부 변수에 종속적인 함수는 그다지 좋은 함수가 아니다. 
# 결론. return을 자주 이용하자~ 
