# type 
# 우리가 연산하고자 하는 데이터의 타입에 따라 동일한 연산자를 사용하더라도 다른 결과를 가져 옵니다.

ddd = 1 + 4 
print(ddd)

eee = '안녕'+ '하세요'
print(eee) #안녕 하세요로 출력함. 

# eee = eee + 1
# 문자열 타입과 정수형 타입을 더하려 했기 때문에 에러가 발생함. 파이썬은 타입에 민감함. 

type(eee) #class 'str' 문자열 클레스 타입
type(1) #정수 클레스 타입. 

# 타입변환
# 변환시키고 싶은 타입 형식으로 감싸주면 타입이 바뀐다. 

i = 42
type(i) #Int type 
f = float(i) #float type으로 출력 
print(f) #42.0으로 출력함   
type(f) #float 타입. 

sval = '123'
type(sval) #str 타입 
# print(sval + 1) #str 타입 
# print(sval + 1) # 문자열과 int를 더한 것이므로 오류다. 

ival = int(sval) 
type(ival) #int 타입 
print(ival + 1) #int 타입 간 연산이기에 가능. 124로 출력됨. 

# 입력 받기. 
# 입력은 input()으로 받을 수 있다. 

nam = input('넌 누구니?')
print('환영합니다', nam) #input에 입력값 값이 출력