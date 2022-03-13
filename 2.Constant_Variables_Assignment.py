''' (아는 내용들은 최대한 간결하게)
    상수 
    상수는 값이 변하지 않는다 
'''

print(123) #123으로 출력, 123이 상수임. 
print(98.6) #98.6으로 출력, 98.6이 상수임. 
print("안녕하세요") #안녕하세요로 출력, 이것이 상수임. 

#변수 

x = 12.2 
print(x) #12.2가 출력 
y = 14 
x = 100 
print(x) #100이 출력됨. 

'''x, y 는 메모리에 할당된 변수의 이름임
= 는 할당자이며 같다는 뜻이 아님. 특정 값을 넣어주는 역할을 한다.(화살표) 


변수의 이름을 정하는 규칙. 
1. 반드시 문자 또는 underscore(_)로 시작한다. (숫자로 시작x) 
2. 문자와 숫자 underscore(_)를 포함할 수 있다. 
3. 읽는 사람이 읽기 편하게 설정하자. '''

#최악의 경우 
fasfdsfsadf = 35 
asdfsdfasjkaw = 12.50 
zxcvzxza = asdfsdfasjkaw * fasfdsfsadf
print(zxcvzxza)

#나쁨 
a = 35.0 
b = 12.50 
c = a * b
print(c) 

#좋음 
hours = 35.0 
rate = 12.50 
pay = hours * rate
print(pay)

#할당문 -> 대입문은 오른쪽 표현의 결과를 왼쪽의 변수에 저장하는 것으로 구성됨. 

x = 0.6
x = 3.9 * x * (1-x)
print(x) #0.936 출력됨. 

x = 3.9 * x*(1-x)
print(x) #0.2336256으로 출력됨. 
