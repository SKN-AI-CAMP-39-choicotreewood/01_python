""" list

- 컨테이너(묶다)형 자료형이자 시퀀스(순서, index) 자료형

- 여러 값(literal)을 묶어서 관리

- list에 값이 저장된 순서(index)를 기억한다.

- 같은 시퀀스 자료형으로 str, tuple이 있다.

"""

print("--- list ---")
lst = [10, 20, 30]    # int 3개를 저장한 list

print(f"lst: {lst} - {type(lst)}")

print(f"lst[0]: {lst[0]} - {type(lst[0])}")


print("--- list 요소 추가/삭제 ---")

"""
- list는 값을 추가하거나 삭제할 수 있는 
  mutable 자료형이다.
- mutable 자료형 : 

- mutable 자료형: list, set, dict
- immutable 자료형: int, float, bool, str, tuple

"""

a = 10
a = a + 2

print("--- list mutable 확인 ---")

lst2 = [1, 2, 3, 4]

# id() 함수: 변수에 저장된 값(객체)의 식별 코드
print(id(lst2))    # 2764224028736

before_id = id(lst2)

# list.append(값)
# - 지정된 list 제일 끝에 값 추가
lst2.append(5)
after_id = id(lst2)

print(lst2, id(lst2))

print(before_id == after_id) # 이전, 현재 id 비교



print("--- list insert ---")
# 리스트 내부 원하는 위치(index)에 요소 삽입(추가)
lst2.insert(0, 0.5)
print("insert 후 lst2", lst2)

lst2.insert(3, 100)
print("insert 후 lst2", lst2)

lst2.insert(7, 777)  # 제일 끝
print("insert 후 lst2", lst2)

lst2.insert(10, 1010)  # 중간에 인덱스 건너 뛰고 삽입 -> 제일 끝으로
print("insert 후 lst2", lst2)

# list 값 변경
print("--- list update ---")
lst3 = [100, 200, 300]

# 1번 인덱스의 값을 2로 변경
lst3[1] = 2
print("변경후 lst3", lst3)



# 특정 인덱스 값 제거
print("--- list remove ---")
lst4 = ["aaa", "bbb", "ccc", "ddd"]

lst4.remove("bbb")
print("remove 후 lst4", lst4)
# list.remove(값): 지정한 값과 일치하는 첫 번째 요소 제거



print("--- list pop ---")
# list.pop(index)
# - 지정된 위치의 요소를 제거하고 반환
# - index를 생략하면 마지막 요소를 제거하고 반환
lst5 = [10, 20, 30, 40]
removed = lst5.pop(1)
print("pop 수행 후 lst5:", lst5)
print("removed:", removed)


# 값 정렬
print("--- list sort ---")
lst6 = [20, 13, 40, 33, 21, 42]
lst6.sort()   # 원본 리스트 자체를 정렬

print(lst6)


lst6.reverse()  # 역순으로 정렬
print(lst6)





# ----------------------------------------------------------------------

""" 다차원 list
- list의 요소로 list가 존재하는 형태

* 2차원 list
- 1차원 list를 요소로 갖는 list

"""
lst7 = [1, 2, 3]   # 1차원
lst8 = [4, 5, 6]   # 1차원

lst_2d_1 = [lst7, lst8]

print("--- 2차원 list ---")
print(lst_2d_1)

# 2차원 list에서 원하는 요소 얻어오기
print("lst_2d_1[0][2]:", lst_2d_1[0][2])

# 2차원 리스트에 1차원 리스트 추가하기
lst_2d_1.append([7, 8, 9])
print(lst_2d_1)

# 2차원 리스트 내부 1차원 리스트에 값 추가하기
lst_2d_1[1].append(99)
print(lst_2d_1)

# 2차원 리스트에서 특정 값 제거
lst_2d_1[2].pop(0)
print(lst_2d_1)




students = [
    ['홍길동', 20],
    ['신사임당', 22, '여'],
    ['이순신', 48, '전남', '여수시']
]

print("--- students에 저장된 모든 학생 이름만 꺼내기 ---")

print(students[0][0])
print(students[1][0])
print(students[2][0])



# csv(Comma Separated Value): 콤마로 구분된 값 (문자열 형식)



# str.split(구분자)
# - 문자열 내에서 지정된 구분자를 기준으로 나누어 list 반환
print("--- str.split(구분자) ---")
data = "이순신,48,전남,여수시"
split_data = data.split(",")
print("split 결과:", split_data, type(split_data))


# -------------------------------------------------------------------

print("--- list 연산 (+, *) ---")

foods = ["🍗", "🍕", "🍔"]
drinks = ["☕", "💧"]

foods_drinks = foods + drinks
print("foods + drinks: ", foods_drinks)
print("foods * 2: ", foods * 2)


# list slicing (문자열과 같은 방법)

print("--- list slicing ---")
texts = ["안녕하세요", "hello", "곤니찌와", "bye", "잘가"]
print("texts[0:2]: ", texts[0:2])
print("texts[2:]: ", texts[2:])
print("texts[::2]: ", texts[::2])



""" list 반복 순회 (iterable)

- iterable(순회) 가능한 타입: str, list, tuple, set, dict
- iterable 이란?
  -> 내부에 저장된 요소를 0번 인덱스부터 끝까지
    하나씩 꺼낼 수 있게 하는 기술

"""

lst = [10, 20, 30, 40, 50]

# for 변수 in 순회객체:
# -> 순회객체에서 요소를 하나씩 꺼내 변수에 저장하여 사용
for e in lst:
    print("요소:", e)

print(list(enumerate(lst)))

# 인덱스 순회
for index, e in enumerate(lst):
    print(f"{index}번째 요소: {e}")


