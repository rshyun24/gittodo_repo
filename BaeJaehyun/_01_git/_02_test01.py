import math
# 01.
# 어떤 실수가 주어졌을 때, 이 수를
#
# 첫째 자리에서 반올림한 정수
# 올림한 정수
# 버림한 정수
# 를 출력하는 프로그램을 작성하시오.
# # 예시 값: 3.14
# # 예시 출력: 3 (반올림), 4 (올림), 3 (버림)

def test1():
    """1번 실습문제 풀이"""
    x = 3.14
    print(round(x), math.ceil(x), math.floor(x))
test1()


# # 02.
# # 사용자로부터 두 개의 숫자를 입력받아, 두 숫자가 같은지 비교하고 결과를 출력하시오.
# # # 예시 입력: 5, 5
# # # 예시 출력: True

def test2():
    """2번 실습문제 풀이"""
    x, y = input(int()).split()
    print(f'{x} = {y}')
    if x == y:
        print('true')
    else:
        print('false')
test2()

# 03.
# 정수 x가 10 이상이고 100 이하인지 판단하여 True 또는 False를 출력하시오.
# 힌트: and 연산자 사용

def test3():
    """3번 실습문제 풀이"""
    a = int(input())
    if (100 > a) and (a > 10) :
        print('True')
    else :
        print('False')
test3()

# 04.
# 0 에서 1 사이의 실수 하나를 입력받아, 소수점 이하가 0.5 이상이면 True를,
# 그렇지 않으면 False를 출력하시오.
# 힌트: round(), 비교연산자 사용

def test4():
    """4번 실습문제 풀이"""
    b = float(input())
    if round(b) == 1:
        print('True')
    else :
        print('False')
test4()

# 05.
# 사용자로부터 실수 하나를 입력받아 다음 조건을 모두 만족하는지 확인하라:
# 소수점 첫째자리에서 올림한 값이 10보다 작다.
# 소수점 이하를 버린 값이 5 이상이다.
# # 위 두 조건을 and 연산자로 판단

def test5():
    """5번 실습문제 풀이"""
    a = float(input())
    print(math.ceil(x) < 10 and math.floor(x) >= 5)
test5()

# 06.
# 숫자 a와 b를 입력받아 다음 조건 중 하나라도 만족하면 True, 아니면 False를 출력하시오:
# a가 b보다 크다
# a를 반올림한 값이 b의 버림값보다 크다
# 힌트: or, round(), math.floor()

def test6():
    """6번 실습문제 풀이"""
    a = float(input())
    b = float(input())
    if round(a) > math.floor(b) or a > b:
        print('True')
    else :
        print('False')
test6()

# 07.
# 임의의 실수 x가 주어졌을 때,
# x의 올림값이 짝수이고
# x의 반올림값이 10보다 작을 경우
# True를 출력하시오. 아니면 False.
# 힌트: math.ceil(x) % 2 == 0, round(x) < 10

def test7():
    """7번 실습문제 풀이"""
    x = float(input())
    if math.ceil(x) % 2 == 0 and round(x) < 10 :
        print('True')
    else :
        print('False')
test7()

# 08.
# 실수 x가 주어졌을 때, 버림값, 반올림값, 올림값을 각각 구한 후 이 중
# 가장 큰 값을 출력하시오.

def test8():
    """8번 실습문제 풀이"""
    x = float(input())
    print(max(round(x), math.ceil(x), math.floor(x)))
test8()

# 09.
# 사용자로부터 실수 하나를 입력받고, 다음 조건 중 하나라도 만족하면 "조건 만족",
# 아니면 "조건 불만족"을 출력하시오:
# 반올림한 값이 5의 배수이다.
# 올림한 값이 짝수이다.

def test9():
    """9번 실습문제 풀이"""
    v = float(input())
    if round(v) % 5 == 0 or math.ceil(v) % 2 == 0 :
        print('조건 만족')
    else :
        print('조건 불만족')
test9()

# 10.
# 실수 두 개 a, b를 입력받고 다음 조건을 만족하는지 판별하시오:
#
# a를 반올림한 값이 b를 반올림한 값보다 작거나 같으면서
# a를 올림한 값이 b를 버림한 값보다 크다

def test10():
    """10번 실습문제 풀이"""
    a = float(input())
    b = float(input())
    if round(a) <= round(b) and math.ceil(a) >= math.floor(b) :
        print('True')
    else:
        print('False')
test10()