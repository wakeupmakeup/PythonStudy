# 상속은 말그대로 물려받는걸 말하는데 클래스에도 이런 개념을 적용할 수 있다. 
# 어떤 클래스를 만들 때 다른 클래스의 기능을 물려 받을 수 있게끔 하는 것이다. 

class tripKim:
    lastname = "김"
    def setname(self, name):
        self.fullname = self.lastname + name

    def trip(self, location):
        print("%s, %s여행을 가다." %(self.fullname, location))


# tripSomeone이라는 클래스를 만든다고 해보자. 

class tripSomeone(tripKim):
    lastname = "etc..."
    

# 앞서 tripKim이라는 클래스를 그대로 가져왔고 lastname을 ect... 으로만 고쳤을뿐 아무것도 하지 않았다. 
# 하지만 기능은 똑같이 물려받았기 때문에 사용이 가능하다. 
# __init__ 매서드와 trip메서드를 구형하지 않더라도 완전히 동일하게 동작할 수 있다.

# 메서드 오버라이딩. 
# 상속받을 대상인 클래스의 메서드와 이름은 같지만 그 행동을 다르게 해야 할 때가 있다. 그때 사용하는게 이것이다. 
# 예를 들어서 trip이라는 함수의 출력값을 더 추가한다면 이렇게 하는 것이다. 

class tripsomeone(tripKim):
    lastname = "etc..."
    def trip(self, location, day):
        print("%s, %s여행 %d일을 갑니다." %(self.fullname, location, day))

# trip 함수를 다르게 설정하고 싶으면 동일한 이름의 trip 함수를 tripSomeone 클래스 내에서 다시 구현하면된다. 
# 이렇게 메서드 이름을 동일하게 다시 구현하는 것을 메서드 오버라이딩이라고 한다. 

# 연산자 오버로딩
# 연산자 오버로딩이란 연산자를 객체끼리 사용할 수 있게 하는 기법이다. 오버로딩을 하면 다음과 같이 동작하도록 만들 수 있다. 

me = tripKim("태경")
someone = tripSomeone("etc")
me + someone # 이 부분인데 동작 방법은 아래에 나와있다. 

# trip.py 

class tripKim:
    lastname = "김"
    def __init__(self, name):
        self.fullname = self.lastname + Name

    def trip(self, location):
        print("%s, %s여행을 가다." %(self.fullname, location))
    
    def love(self, other):
        print("%s, %s 사랑에 빠졌다." %(self.fullname, other.fullname))
    
    def __add__(self, ohter):   #연산자 오버로딩 사용
        print("%s, %s 결혼했네" %(self.fullname, other.fullname))

class tripSomeone(tripKim):
    lastname = "etc"
    def trip(self, location, day):
        print("%s, %s여행 %d일 갑니다." %(self.fullname, location, day))

# 실행하면 다음과 같이 나온다. 
# 김태경, etcetc 사랑에 빠졌다. 
# 김태경, etcetc 결혼했네 
# 위에 호출부처럼 + 로 한다면 __add__로 했던 것이 튀어나온다. 

# 지금까지 배운것으로 하나의 클래스를 만들어보자. 

# 스토리는 다음과 같다. 

# 김태경은 서울에 놀러 가고
# 이상형은 우연히 4일간 서울에 놀러간다. 
# 둘은 사랑에 빠져서 결혼하게 된다. 
# 그러다 싸우고 바로 이혼하게 됐다. 

class tripTK:
    lastname = "김"
    def __init__(self, name):   # 초깃값 설정
        self.fullname = self.lastname + name
    
    def travel(self, location):
        print("%s, %s여행을 가다" %(self.fullname, location))

    def love(self, other):
        print("%s, %s사랑에 빠지다" %(self.fullname, other.fullname))

    def __add__(self, other):
        print("%s, %s와 결혼하다" %(self.fullname, other.fullname))     #연산자 오버로딩
    
    def __sub__(self, other):
        print("%s, %s와 이혼하다" %(self.fullname, other.fullname))     #연산자 오버로딩

    def fight(self, other):
        print("%s, %s와 싸우다" %(self.fullname, other.fullname))

class tripSome(tripTK): # 상속
    lastname = "이"
    def travel(self, location, day): # 메소드 오버라이딩 
        print("%s, %s로 %d일 만큼 여행을 가다" %(self.fullname, location, day))

# 호출부

kim = tripTK("태경")

mylove = tripSome("상형")

kim.travel("서울")

mylove.travel("서울",4)

kim.love(mylove)

kim + mylove

kim.fight(mylove)

kim - mylove






