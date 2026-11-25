# 변수 (variable)
# - 값을 저장하는 메모리 공간
# - 변수 선언과 동시에 값(Literal)을 할당할 수 있다.

# 변수 선언과 동시에 대입
a = 10  # a 변수에 10을 저장(대입)
b = "홍길동"  # b 변수에 "홍길동"을 저장(대입)

num = a  # num 변수에 a (10) 대입

print("a: ", a)
print("b: ", b)
print("num: ", num)


"""
변수명 작성요령
1. 대소문자를 구분한다.
2. 변수명은 snake_casing을 사용한다. (단어와 단어사이를 _로 연결)
3. 한글 변수명을 지정할 수 있다. (Python에서 유효하며 협업의 표기 일관성을 위해 영문을 주로 사용한다.)
4. 언더바(_)를 제외한 특수문자를 사용할 수 없고, 숫자로 시작할 수 없다.
5. 파이썬 예약어(if, elif, else, for, while, …)를 사용할 수 없다.
6. **직관적인 변수명**을 사용한다. 짧고 간편하다고, a, b, c와 같은 변수명을 사용하지 않는다.
"""

# 대소문자 구분 확인
name = "이순신"
NAME = "홍길동"
print(name, NAME)

# 변수명은 snake_casing을 사용한다.
show_me_the_money = 10000
print("show_me_the_money:", show_me_the_money)

# 한글 변수명을 지정할 수 있다. (하지만 사용하지 않는다.)
우리반 = "SKN_AI_39"
print(우리반)

# 언더바(_)를 제외한 특수문자를 사용할 수 없고, 숫자로 시작할 수 없다.
# 1st_user = "김씨"  => 안 됨
_1st_user = "김씨"
print(_1st_user)

# second! = "박씨"  => 안 됨

# 파이썬 예약어(if, elif, else, for, while, …)를 사용할 수 없다.
import keyword
print(keyword.kwlist)
# 'False', 'None', 'True', 'and', 'as', 'assert',
# 'async', 'await', 'break', 'class', 'continue',
# 'def', 'del', 'elif', 'else', 'except', 'finally',
# 'for', 'from', 'global', 'if', 'import',
# 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass',
# 'raise', 'return', 'try', 'while', 'with', 'yield'

# 직관적인 변수명을 사용한다.
# 짧고 간편하다고, a, b, c와 같은 변수명을 사용하지 않는다.
# 의미 없는 변수명 금지








