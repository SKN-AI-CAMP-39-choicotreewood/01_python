""" bool과 조건 조합

- boolean은 참/거짓을 나타냄.
- 파이썬에서는 'bool'이라고 표현
- 참(True), 거짓(False)
- 주로 조건에 따른 코드 분기에 많이 사용


"""

is_true = True
is_false = False

print("is_true: ", is_true, type(is_true))
print("is_false: ", is_false, type(is_false))



# 비교 연산자
# >, <, ==, !=, >=, <=

print("1 > 0.5:", 1 > 0.5)     # True
print("1 < 0.5:", 1 < 0.5)     # False
print("1 >= 0.5:", 1 >= 0.5)   # True 
print("1 <= 0.5:", 1 <= 0.5)   # False
print("1 == 1:", 1 == 1)       # True
print("1 != 1:", 1 != 1)       # False



# 논리 부정 연산자 (! => not)
print(True)
print(not True)


# 논리 연산자 (and, or)

# and 연산자
# - 좌항과 우항이 모두 참(True)일 때만 True
print("True and True:", True and True)     # True
print("True and False:", True and False)   # False
print("True or False:", True or False)     # False
print("False or False:", False or False)   # False

print("--- and ---")
print("100 > 0 and 1 == 1:", 100 > 0 and 1 == 1)  # True
print("30 > 20 and 123 != 123:", 30 > 20 and 123 != 123) # False
print("3 <= -3 and 12 == 12:", 3 <= -3 and 12 == 12) # False
print("9 >= 9 / 9 * 9 and 12 != 11 + 1:", 9 >= 9 / 9 * 9 and 12 != 11 + 1) # False


# or 연산자
# - 좌항과 우항이 모두 거짓(False)일 때만 False
print("True or True:", True or True)     # True
print("True or False:", True or False)   # True
print("False or True:", False or True)   # True
print("False or False:", False or False)   # False

print("100 > 0 or 1 == 1:", 100 > 0 or 1 == 1)         # True
print("10 * 10 == 100 or 1 != 1:", 10 * 10 == 100 or 1 != 1)    # True
print("100 == 0 or 10 == 10:", 100 == 0 or 10 == 10)       # True
print("100 - 1000 > 0 or 23 != 20 + 3:", 100 - 1000 > 0 or 23 != 20 + 3)   # False



print("--- 합격 또는 불합격 여부 판별하기 ---")
# 조건: 각 과목 점수가 40점 이상이고 평균 60점 이상만 True, 나머지는 False

score_kor = 70
score_eng = 50

result = score_kor >= 40 and score_eng >= 40 and ((score_kor + score_eng)/2) >= 60


print("합격여부: ", result)


# 논리 연산자(not, and, or), 비교 연산자(>, <, ==, !=, >=, <=)의 결과는
# 항상 자료형이 bool 이다.



