# 튜플 자료형
# 튜플이 뭔데? -> 보자기 안에 여러 구슬이 들어있는 것이라 생각하자.
# 튜플은 리스트와 비슷하지만 리스트가 제공하는 생성, 삭제, 수정이 불가능하다.

t1 = ()
t2 = (1,)
t3 = (1,2,3)
t4 = 1,2,3
t5 = ('a','b',('ab', 'cd'))
# 튜플의 다양한 모습이다. 튜플안에 튜플이 들어 갈 수도 있다.
# 그리고 t2를 보면 리스트와 다른점이 요소 하나만 가질때 반드시 끝에 ,를 해야한다.

# 튜플을 왜 쓸까? 리스트는 값의 수정과 생성이 가능하지만 튜플은 그렇지 않다고 배웠다. 그러면 해당 값이 변하지 않기를 바라거나 값이 바뀔까
# 걱정이 들때 튜플을 사용하자

# 변하지 않는다는데 수정과 삭제는 어떻게 하나?
# -> 답은 불가능하다. 시도하면 오류창이 뜬다.

# 인덱싱, 슬라이싱, 더하기(+), 곱하기(*)

# 1. 인덱싱하기

t1 = (1,2,'a','b')
print(t1[0])
# -> 1
print(t1[3])
# -> 'b'

# 2. 슬라이싱하기
t1 = (1,2,'a','b')
t1[1:] # 1부터 끝까지
print(t1[1:])
# -> (2, 'a', 'b')


# 3. 튜플 더하기
t2 = (3,4)
t1 + t2
print(t1 + t2)
# -> (1,2,'a','b',3,4)

# 4. 튜플 곱하기
t2 * 3
print(t2 * 3)
# -> (3, 4, 3, 4, 3, 4)

# 딕셔너리 자료형
# 딕셔너리. 사전이라는 뜻인가? 이게 뭔지 알아보자
# 사람은 누구든지 이름, 생일등등 연관되는 정보가 있다. 이름 = 김태경 이런 것 처럼. 일르 대응관계라고 한다.
# 그리고 이 대응관계를 나타내는 자료형이 있는데 이를 연관 배열 혹은 해시라고 한다. 이런 자료형을 딕셔너리라고 한다.
# 딕셔너리는 Key와 Value라는 것을 한 쌍으로 갖는 자료형이다. 예를들어 야구 = "BaseBall" 이런 것 처럼.

# 딕셔너리는 리스트나 튜플처럼 순차적으로 요소값을 구하지 않고 앞서 말한 Key를 통해서 값을 얻는다.

# 만드는 방법.
# 아래는 기본적인 딕셔너리의 모습이다.
# {Key1: Value1, Key2: Value2, Key3: Value3 ...}
# 키와 값이 {}으로 둘러싸여 있다. 각 요소는 쉼표(,)로 구분되어 진다.

dic = {'name': 'pey', 'phone': '01031051111', 'birth': '1111'}
#위에 요소들은 각각 대응한다.
# name = pey
# phone = 01031051111
# brith = 1111

# 아래 예시는 Key로 정수값 1, 값으로 '안녕'이라는 문자열을 사용한 예이다.

a = {1:'안녕'}

# 또한 값에 리스트도 넣을 수 있다.

b = {'a':[1,2,3]}

# 딕셔너리 쌍 추가, 삭제하기.

# 추가

a = {1:'안녕'}
a[2] = 'b' # <- {2:'b'} 쌍 추가
print(a)
# -> {1: '안녕', 2: 'b'}

a['name'] = 'pey'  # <- {'name':'pey'} 쌍 추가.
print(a)
# -> {1: '안녕', 2: 'b', 'name': 'pey'}

a[3] = [1,2,3] # <- {3:[1,2,3]}쌍 추가.
print(a)
# -> {1: '안녕', 2: 'b', 'name': 'pey', 3: [1, 2, 3]}






