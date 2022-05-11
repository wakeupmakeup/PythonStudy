# 일반적으로 입력을 받을 때는 사용자가 직접 입력하는 방식을 사용했고
# 출력할때는 모니터 화면에 출력하는 방식으로 프로그래밍해 왔지만 이제는 파일을 통한 입출력을 해보자. 

# 파일 생성하기. 
# 다음 소스 코드를 에디터로 작성해서 저장한 후 실행하면 다음과 같이 나온다. 
f = open("새파일.txt", 'w')
f.close() 

# 파일 객체 = open(파일 이름, 파일 열기 모드)
# 파일을 생성하기 위해서 유리는 open이라는 파이썬 내장 함수를 사용했다. 파일 열기 모드에는 다음과 같은 것들이 있다. 

# r - 읽기모드 : 파일을 읽기만 할 때 사용 
# w - 쓰기모드 : 파일에 내용을 쓸 때 사용
# a - 추가모드 : 파일의 마지막에 새로운 내용을 추가할 때 사용

# 파일을 쓰기 모드로 열게 되면 해당 파일이 이미 존재할 경우 원래 있던 내용이 모두 사라지고, 해당 파일이 존재하지 않으면 새로운 파일이 생성된다. 
# 위의 예에서는 디렉터리에 파일이 없는 상태에서 새파일.txt 쓰기 모드인 'w'로 열었기 때문에 새파일.txt 라는 이름의 새로운 파일이 현재 디렉터리에 생성된다. 

f = open("C:/Python/새파일.txt", 'w')
f.close()

# 위의 예에서 f.close()는 열려 있는 파일 객첼르 닫아 주는 역할을 한다.
# 사실 안써도 자동으로 닫아주긴 하지만 직접 닫아주는게 좋다. 

# 파일을 쓰기 모드로 열어 출력값 적기 

# writedata.py
f = open("C:/Python/새파일.txt", 'w')
for i in range(1,11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)  # <- data를 파일 객체 f에 써라. 
f.close()

# 밑에 프로그램과 위에 프로그램을 비교한다면 차이점을 알 수 있다. 

for i in range(1,11):
    data = "%d번째 줄입니다." %i
    print(data)

# 밑에 프로그램은 프롬프트에서 출력이 되지만 위에는 새파일이라는 이름의 메모장 파일에서 출력된다. 

# 프로그램 외부에 저장된 파일을 읽는 여러 가지 방법. 

# 1. readline() 함수 이용하다. 

f = open("C:Pytohn/새파일.txt", 'r')
line = f.readline()
print(line)
f.close()

# readline()이 뭔데요? 
# 위 예는 f.open으로 파일을 읽기 모드로 연 후에 readline()으로 파일의 첫 번째 줄을 읽어 출력하는 경우다. 
# 만약 모든 라인을 읽어서 화면에 출력하고 싶다면? 

f = open("C:/Python/새파일.txt", 'r')
while True:
    line = readline()
    if not line:
        break
    print(line)
f.close()

# while True라는 무한 루프를 이용해서 한 줄씩 읽는 것을 쭉 유지시킨다. 만약 더 읽을 것이 없다면 break 하게 끔 만들었다. 
# 이런 것도 있다. 

while 1: 
    data = input() 
    if not data:
        break
    print(data)

# 2. readlines() 이용하기. 

f = open("C:\Python\새파일.txt", 'r')
lines = f.readlines()
for line in lines: 
    print(line)
f.close() 

#readlines() 함수는 파일의 모든 라인을 읽어서 각각의 줄을 요소로 갖는 리스트로 반환한다. 
# 뭔소리냐? 
# 쉽게 말하면 해당하는 함수의 모든 라인을 한줄 한줄 마다 리스트로 바꾼다는 이야기다. 
# ["1번째 줄입니다.", "2번째 줄입니다.", "3번째 ..."]

# 3. read() 이용하기. 
f = open("C:/Python/새파일.txt", 'r')
data = f.read()
print(data)
f.close() 

# f.read()는 파일의 내용 전체를 문자열로 반환하다. 

# 파일에 새로운 내용 추가하기. 
# 쓰기 모드로 파일을 열때 이미 존재하는 파일을 열 경우 그 파일의 내용이 모두 사라지게 된다. 
# 이미 있는 내용에 추가를 하고 싶다면? 'a'로 열면 된다. 

# adddata.py
f = open("C:/Python/새파일.txt", 'a')
for i in range(11,20):
    data = "%d번째 줄입니다. \n" % i
    f.write(data)
f.close()

# 원래 있던 부분은 1~10번째줄, 이번에 추가한것은 11~19번째 줄이다. 

# with문과 함께 사용하기. 

f = open("foo.txt", 'w')
f.write("Life is too short")
f.close()

# 파일을 열면 위와 같이 항상 close 해주는 것이 좋지만 자동으로 할 수는 없을까:? 
# 이럴때 with를 사용하면 된다. 

with open("foo.txt", "w") as f:
    f.write("삶은 너무 짧아")



