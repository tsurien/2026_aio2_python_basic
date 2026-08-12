# clac 모듈 add() 함수 정의

def add(a, b) :
    result = a + b
    return result # 익숙해지면 변수 패스

def mul(a, b):
    return a * b

def sub(a, b):
    return a - b

def div(a, b):
    if b == 0:
        raise ValueError
    return a / b

def quo(a, b):
    return a // b

def rem(a, b):
    return a % b

# 터미널

if __name__ == '__main__' :
    # 실행 내용을 넣어준다. 
    print('hi')