# class를 왜 쓸까? 
# 사실 c를 보더라도 클래스 없이 프로그램을 작성하는 것은 얼마든지 가능하다. 다만 요즘 등장하는 언어들은 
# 모두 클래스를 가지고 있는데 왜 있어야 할까? 

# 쉽게 생각해보자면 불필요한 복잡성을 없애기 위해 이용한다. 
# 뽑기 틀을 클래스라고 생각해보자. 뽑기를 한번 할때마다 뽑기 틀을 이용해서 쉽게쉽게 만든다고 생각하면 이해가 빠르다. 

# 아래와 같은 계산기 프로그램을 만든다 가정하자. 

result = 0

def add(num):
    global result
    result += num
    return result

print(add(3))
print(add(4))

# 이전에 계산된 결과값을 유지시키기 위해서 result라는 변수를 사용했다. 실행하면 다음과 같이 출력한다.

# 3
# 7 

# 만약 한 프로그램에서 2개의 계산기가 필요한 상황이 생긴다면? 
# 계산기는 각각의 결과값을 유지해야 하기 때문에 위와 같이 add함수 하나만으로는 따로 유지가 불가능하다. 
# 이러면 아래처럼 함수와 변수를 따로 만들어야 한다. 

result1 = 0
result2 = 0

def add(num):
    global result1
    result1 += num
    return result1
    #계산기 1

def add2(num):
    global result2
    result2 += num
    return result2
    #계산기 2

print(add(3))
print(add(4))
print(add2(3))
print(add2(4))

# 출력은 아래와 같이 나타난다. 
# 3
# 7
# 3
# 10 

# 지금에야 2개라 이렇게 간단하게 한거지 계속 늘어난다면? 그때마다 저렇게 함수와 변수를 추가할 것인가? 
# 나라면 gg 친다. 그래서 나온게 클래스다. 

class Carculator:
    def __init__(self):
        self.result = 0
        
    def add(self, num):
        self.result += num
        return self.result

cal1 = Carculator()
cal2 = Carculator()

# 와! 정말 간단하잖아?? 

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))

# 출력도 똑같이 나온다. 
# 클래스를 이용하면 계산기의 개수가 늘어나도 인스턴스를 생성하기만 하면 되기 때문에 함수를 사용하는 경우와 달리 매우 간단해진다. 

# 클래스의 개념으로는 다음과 같다. 
# 아까 뽑기 이야기가 나왔는데 뽑기 틀이 클래스라고 가정하면 특정 뽑기 틀 모양의 뽑기(인스턴스)가 생성된다. 
# 그것이 별모양, 하트, 구름모양마다 다른 뽑기(인스턴스)가 나오는 것이다. 

# 클래스 -> 설계 도면 
# 인스턴스 -> 클래스에 의해 만들어진 피조물 (클래스에 의해 만들어진 객체)

# 가장 간단한 클래스 구조 

class Simple: 
     pass
# 이렇게 아무런 기능이 없어도 클래스라고 할 수 있다. 
# Simple 클래스의 인스턴스를 만드는 방법은 아래와 같다. 

인스턴스만들기 = Simple()

# Simple의 결과값을 돌려받은 인스턴스만들기(변수이름)가 바로 인스턴스다. 

# 객체와 인스턴스의 차이점은? 

나비 = Cat()
# 이렇게 만들어진 나비는 객체이다. 그리고 나비라는 객체는 Cat의 인스턴스다. 
# 뭔 개소리냐고? 
# 즉, 인스턴스라는 말은 특정 객체(나비)가 어떤 클래스(Cat)의 객체인지를 관계 위주로 설명할때 사용한다. 

# 아주 쉽게 클래스 이해하기. 

# 클래스 변수
# 다음의 클래스를 봐보자. 

class Service:
    internet = "1GB"

# 위의 클래스 이름은 Service이다. 우리는 이 Service 클래스를 인터넷 서비스 제공 업체(통신사)라고 가정을 해보자. 
# 이 통신사는 가입한 고객에게만 인터넷을 제공한다. 이제 당신은 인터넷을 이용하기 위해서 가입을 해야한다. 

# 가입방법은 아래와 같다. 
myId = Service()

# 이렇게 하면 myId라는 아이디로 통신사의 Service 클래스를 이용할 수 있다. 
# myId라는 아이디로 통신사가 제공하는 정보를 얻어내자. 

myId.internet

# -> 1GB

# 아이디 이름에다가 업체가 제공하는 internet이라는 변수를 '.'(도트연산자)를 이용해서 호출하면 된다. 


# 클래스 함수 
# Service라는 이름의 통신사가 돈을 많이 벌어 새로운 서비스를 만들게 되었다. 

class Service:
    internet = "1GB"
    def sum(self, a, b):
        result = a + b
        print("%s + %s = %s입니다." %(a,b,result))

# 클래스가 업그레이드 되어 이제 업체에 가입한 모든 사람들이 더하기 서비스를 제공받을 수 있게 됐다. 이용 방법은 아래와 같다. 
# 회원이 아니라면 먼저 서비스에 가입하자. 

myId2 = Service()

# 다음에 새로운 서비스를 이용한다. 

myId2.sum(1,1)

# 1 + 1 = 2입니다. 

# self는 뭔가요?
# 통신사 입장에서 생각해보자. 통신사는 오직 가입한 사람들에게만 서비스를 제공하고 싶어한다. 이를 위해 그들은 더하기 서비스에 가입했는지 여부를 확인하기 위한 장치를 추가했다. 
# 그게 self 이다. 

# 누군가 이 업체의 서비스를 이용하고 싶다고 요청했을때 이 사람이 가입을 했는지 안했는지 알아보기위해 sum 함수의 첫 번째 입력값으로 self라 한것이다. 아래 처럼 이렇게 했다고 쳐보자 

UnknownID = Service() 
UnknownID.sum(1,1)

# 이렇게 하면 UnknownId라는 사람이 이 통신사의 sum이라는 서비스를 이용하겠다고 요청한 것이다. 

# 앞에서 봤듯이 통신사는 sum함수의 첫 번째 입력값을 통해 가입 여부를 판단했다. 다시 sum 함수를 보면 

def sum(self, a, b):
    result = a + b
    print("%s + %s = %s입니다." %(a,b,result))

# 위의 sum 함수는 첫 번째 입력값으로 self라는 것을 받고 그 다음부터 특정값을 받는다. 입력으로 받는 입력 인수의 개수가 총 3개이다. 
# 그래서 myId라는 아이디를 가진 사람은 다음처럼 sum 함수를 이용해야 한다. 

myId.sum(myId,1,1)
# sum 함수는 첫 번째 입력값을 가지고 가입한 사람인지 아닌지를 판단한다. 따라서 첫 번째 입력 인수로 myId라는 아이디를 주면 sum함수는 myId라는 아이디가 이미 가입 되어 있는 것을 
# 확인 한 후 서비스를 제공할 것이다. 

# 이전에 아래 처럼 self를 사용하지 않고 짧게 사용한 것을 확인할 수 있는데 왜그럴까? 

myId.sum(1,1)

# 위에 처럼 호출이 발생하면 self는 호출 시 이용했던 인스턴스(myId라는 아이디)로 바뀌게 된다. 그래서 myId.sum(myId,1,1)가 아닌 myId.sum(1,1)이 가능해진다. 
# 알아서 바뀌지 쓰지를 않은것임. 


# 정확히 self가 뭔데?? 

# 통신사는 자신의 서비스를 이용해주는 고마움의 표시로 이름 출력 서비스를 제공해 주기로 마음 먹었다. 그래서 다시 Service 클래스를 또 한번 업그레이드 했다. 

# 사용자에게 이름을 입력받아 더하기 서비스를 제공할 때 앞부분에 그 이름을 넣어준다. 

class Service:
    internet = "1GB"
    def setname(self, name):
        self.name = name
    def sum(self,a,b):
        result = a+b
        print("%s님 %s + %s = %s입니다." %(self.name, a, b, result))

# 그리고 바뀐 점과 이름 출력 서비스의 사용법에 대해서 다음처럼 이용할 수 있다. 

# 먼저 통신사에 가입해야한다. 

myId = Service()

# 그 후 myId라는 아이디를 가진 사람이 자신의 이름은 김태경이라고 알려준다. 
myId.setname("김태경") 

# 더하기 서비스를 이용한다. 
myId.sum(1,1)

# 이제 부터 myId라는 아이디를 가진 사람의 이름은 항상 "김태경"이 된다. 
# 그리고 self는 호출할때 자동으로 인스턴스의 이름으로 똑같이 바뀐다는걸 인지하자. 

# _init_ 이란 뭘까? 
# 통신사의 가입자 수가 눈에 띄게 많아지기 시작했다고 치자. 
# 그 만큼 사용자들의 오류보고가 많아 지게 됐는데 그 오류는 다음과 같았다. 

stupidPerson = Service()
stupidPerson.sum(1,1)

# 위와 같이 입력하면 자꾸 오류가 발생한다는 것이다. 그 때마다 통신사에선 myId.setname("이름")같은 이름을 넣어주는 과정이 빠졌기 때문에
# 오류가 발생한다고 공지사항에도 명시했었지만 계속해서 이런 오류가 나온다는 것이 귀찮아지기 시작했다. 
# 그래서 다음과 같은 아이디어를 냈다. 
# 지금까지는 별 다른 과정없이 바로 아이디를 부여해주는 방식이었지만 이번엔 사용자 이름을 받아야지만 아이디를 부여받을 수 있게 하면 
# 굳이 setname()을 안해도 되는 상황을 만들 수 있다. 그렇게 할 수 있게하는 방식이 _init_이다. 

class Service:
    internet = "1GB"
    def _init_(self, name):
        self.name = name
    def sum(self, a, b):
        result = a + b
        print("%s님 %s + %s = %s입니다." %(self.name, a,b,result))

# 위의 service 클래스를 이전의 클래스와 비교해 보면 바뀐 부분은 단 한가지. setname함수의 이름이 _init_으로 변했다! 
# 바뀐 부분의 의미는 다음과 같다. 

# "인스턴스를 만들 때 항상 실행된다."

# 즉, 아이디를 부여받을때 항상 실행된다는 말이다. 그래서 이제는 이 통신사에 가입하려면 다음과같이 입력해야 한다. 

myId = Service("김태경")

# 자신의 이름과 같이 입력해야 가입이 되는 것이다. 
# 간단히 정리하자면 다음과 같다. 

myId = Service()
myId.setname("김태경")
myId.sum(1,1)

# 을 

myId = Service("김태경")
myId.sum(1,1)

# 으로 간단하게 쓸 수 있게 됐다. 

# 굳이 이야기 형식으로 편집한 것은 내가 처음에 클래스 공부할때 이해가 안간 경험이 생각나 쉽게 풀어썼다. 
# myId = Service()로 해서 생성된 myId를 아이디라고 했는데 이것이 바로 인스턴스라고 불리는 것을 잊지말자. 


# 클래스의 구조

class 클래스이름[(상속클래스이름)]:
    클래스변수1
    클래스변수2
    ...

    클래스변수N


    def 클래스함수1(self,[인수1, 인수2, 인수N]):
        수행할문장1
        수행할문장2
        ...

    def 클래스함수2(self,[인수1, 인수2, 인수N]):
        수행할문장1
        수행할문장2
        ...
    
    def 클래스함수N(self,[인수1, 인수2, 인수N]):
        수행할문장1
        수행할문장2
        ...

# 사칙연산 클래스 만들기.
# 사칙연산을 하는 붕어빵 틀을 만들어보자. 

# 클래스를 만들기 전에 무엇이 필요한지 한번 생각해보는게 좋다. 

# 사칙연산 -> 두 숫자를 입력받기(인자)
# 나누기 기능 
# 더하기 기능
# 빼기 기능
# 곱하기 기능 

# 앞서 말한 통신사 가입과 똑같다. 객체를 생성하자. 

ex = fourCal()

# 그런 다음 사칙연산을 위한 데이터를 입력받게 만들자. 

ex.setdata(1,2)

# 클래스 등록과 두 데이터를 입력 받았으니 각각 연산을 해보자 

print(ex.sum())
print(ex.mul())
print(ex.div())
print(ex.sub())

# 사칙연산이 완성됐다. 이렇게 작동하게 만드는 것이 목표다. 
# 클래스 구조를 파악하면서 만들어 보자. 

class fourCal:
    def setdata(self,first,second):
        self.first = first
        self.second = second
    
    def sum(self, first, second):
        result = self.first + self.second
        return result
    
    def sub(self, first, second):
        result = self.first - self.second
        return result

    def mul(self, first, second):
        result = self.first * self.second
        return result

    def div(self, first, second):
        result = self.first / self.second
        return result

# 동작함을 확인하려면? 

a = fourCal()
b = fourCal()
a.setdata(4,1)
b.setdata(7,2)

a.sum()
a.sub()
a.mul()
a.div()

b.sum()
b.sub()
b.mul()
b.div()

# 정상적으로 작동한다! 



# 이번엔 여행 클래스를 만들어 보자 

# 어디로 여행갔니?

class tripKim:
    lastname = "김"
    def setname(self, name):
        self.fullname = self.lastname + Name

    def trip(self, location):
        print("%s, %s여행을 가다." %(self.fullname, location))

me = tripKim()
me.setname("태경")
me.trip("서울")

# 김태경, 서울여행을 가다. 

# init을 이용한 초깃값 설정해보기. 
# 위에서 tirpKim이라는 클래스를 이용해서 인스턴스를 만들었다. 그리고 이를 또 이용해서 setname을 활용했다. 그렇다면 아래와 같이 이렇게 한다면 어떻게 나올까? 

me = tripKim()
me.trip("서울")

# 이러면 오류가 나는데 setname()함수가 실행되지 않아서 생기는 오류다. 아까 통신사 문제 처럼 일일히 입력하지 않아도 자동으로 만들어 지게끔 하는 것이다 _init_ 이다. 
# 이것으로 다시 작성해보면 다음과 같아진다. 

class tripKim:
    lastname = "김"
    def __init__(self, name): # setname을 __init__으로 바꿨다. 
        self.fullname = self.lastname + Name

    def trip(self, location):
        print("%s, %s여행을 가다." %(self.fullname, location))

# 이렇게 바뀐 후 아래와 같이 입력하면 오류가 나는데 그 이유는 이제 알겠지만 클래스 등록과 동시에 값을 넣지 않아서 생기는 문제다. 

me = tripKim() # 오류남. 

me = tripKim("태경") # 이렇게 해야함 

