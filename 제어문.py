# 제어문은 if, while, for 문 등등이다. 기본적인 것들은 최대한 빨리 넘어갈 예정이다. 
# 주로 형식만으로 짧게 리뷰할 것. 

# if 



if 조건문:
    수행할 문장1 
    수행할 문장2
    ... 

else:
    수행할 문장A
    수행할 문장B 
    ...

    # 기본적 형식은 이렇다. 파이썬에서 조심할 것은 들여쓰기를 잘해야한다는 것 정도. 다른 언어와는 다르게 잘못쓰면 오류난다. 
    # 서로의 공백이 달라도 오류가 난다. SpaceBar or Tap인데 둘중 아무거나 사용하고 혼용해서 쓰지는 말자. 
    # 비교연산자 같은 경우는 사용할 줄 안다고 취급하고 넘어간다. 

# x in s, x not in s 
# 파이썬에서 제공하는 재밌는 조건문이다. 안에 있느냐 없느냐로 참 거짓을 나눈다. 

    1 in [1,2,3]    # 1이 [1,2,3]안에 있습니까? 
    # -> 참 

    1 not in [1,2,3] # 1이 [1,2,3]안에 없습니까? 
    # -> 거짓 

# elif 
# 첫 문장에서 ~~가 거짓이고 다음문장이 참이라면 ~~ 
# 예시 

    pocket = ['돈', '핸드폰']

    card = 1

    if 돈 in pocket:
        print("택시타자")
    elif card: 
        print("버스타자")
    else:
        print("걍 걸어가")

# elif는 개수에 제한 없이 사용할 수 있다. 


# while 문 
# 아래는 while문의 기본적 구조다. 

    while 조건문: 
        수행할 문장1 
        수행할 문장2
        수행할 문장3 
        ... 

# 예시 

    treeHit = 0
    while treeHit < 10:
            treeHit = treeHit + 1
            print("나무를 %d번 찍었습니다." % treeHit)
            if treeHit == 10:
                print("나무 넘어가니 조심해!!!")



# 자판기 프로그램 만들기 

coffee = 10
while True: #무한 반복
    money = int(input("돈을 넣어주세요"))
    if money == 300: 
        print("커피를 드리겠습니다.")
        coffee = coffee - 1
    elif money > 300:
        print("거스름돈 %d와 커피를 드리겠습니다." &(money-300))
        coffee = coffee -1

    else: 
        print("금액이 맞지 않습니다. 다시 시도해 주십시오")
        print("남은 커피의 양은 %d 입니다" % coffee)

    if not coffee:
        print("모두 떨어졌습니다. 판매를 종료합니다.")
        break # while문 탈출

    # 만약 조건에 맞지 않을 경우 continue를 사용하면 처음으로 돌아간다. 



# for문 
# while과는 다르게 for문은 특정 구간에서 돌릴때 사용한다. 
# 아래는 기본 구조이다. 

    for 변수 in 리스트(or 튜플, 문자열):
        수행할 문장1
        수행할 문장2
         . . . 


# 합/불합으로 알아보는 for문 예시 

    marks = [90,25,60,70,50]
    number = 0
    for mark in mark:   # 위에 리스트 값을 순서대로 marks에 대입한다. 
        number += 1 # 학생 번호 하나하나 증가

        if marks > 70:
            print("축하합니다. %d 학생은 합격입니다." % number)
        else: 
            print("아쉽게도 %d 학생은 합격하지 못했습니다" % number)

# 만약 불합격 학생들은 배제하고 싶으면 if문 끝에 continue를 쓰면 된다. 

# for문과 자주 쓰이는 range함수 
# for문은 숫자 리스트를 자동으로 만들어 주는 range라는 함수와 자주 쓰인다. 

a = range(10)
print(a) 
# -> 0,1,2,3,4,5,6,7,8,9 -> range(0,10)

# (첫 숫자, 끝 숫자)에서 끝 숫자는 포함되지 않는다. 
# 그럼 어떻게 쓰이는 건데? 

sum = 0
for i in range(1,11):
     sum += 1
print(sum)

# -> 55 

# 리스트안에 for문 포함하기 
a = [1,2,3,4]
result = [] 
for num in a: 
    result.append(num*3)

print(result)
# -> [3,6,9,12]


