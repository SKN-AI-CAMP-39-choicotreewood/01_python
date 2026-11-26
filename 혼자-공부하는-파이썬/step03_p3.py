# [튜터의 따뜻한 응원 한마디 🌱]
# 처음이어도 괜찮아요! 차근차근 코드를 채워 멋진 결과물을 확인해 봐요.
# 1) 문장과 찾을 낱말을 차례로 읽어요.
sentence = input()
keyword = input()
# TODO: 단어 수와 낱말의 위치, 포함 여부를 구해 보세요.

lst_sentence = sentence.split(" ")

if "" in lst_sentence:
    for i in range(lst_sentence.count("")):
        n = lst_sentence.index("")
        lst_sentence.pop(n)

count = len(lst_sentence)
check = ""
first_position = 0
last_position = 0

if keyword not in sentence:
    check = "아니오"
    first_position = -1
    last_position = -1
else:
    check = "예"
    first_position = sentence.index(keyword)
    last_position = len(sentence) - sentence[::-1].index(keyword[::-1]) - len(keyword)

str_1 = f"단어 수: {count}"
str_2 = f"첫 위치: {first_position}"
str_3 = f"마지막 위치: {last_position}"
str_4 = f"포함 여부: {check}"


result = f"{str_1}\n{str_2}\n{str_3}\n{str_4}"
# 2) 완성한 결과를 출력해요.
print(result)
