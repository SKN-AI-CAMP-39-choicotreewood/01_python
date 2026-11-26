# [튜터의 따뜻한 응원 한마디 🌱]
# 처음이어도 괜찮아요! 차근차근 코드를 채워 멋진 결과물을 확인해 봐요.
# 1) 표지 한 줄을 입력받습니다.
raw = input()
# 2) 공백 정리와 대소문자 변환, 판정 결과를 준비해 보세요.
# TODO: 정리한 표지와 판정 결과를 만들어요.

txt = raw.strip()

str_1 = f"대문자: {txt.upper()}"
str_2 = f"소문자: {txt.lower()}"
str_3 = f"표지 판정: {"사용 가능" if txt.isalnum() == True else "다시 입력"}"

result = f"{str_1}\n{str_2}\n{str_3}"
# 3) 안내된 형식으로 결과를 출력해 보세요.
print(result)
