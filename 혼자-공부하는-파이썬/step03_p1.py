# [튜터의 따뜻한 응원 한마디 🌱]
# 처음이어도 괜찮아요! 차근차근 코드를 채워 멋진 결과물을 확인해 봐요.
# 1) 입력된 이름을 읽어 보관해요.
name = input()
# 2) 수량과 가격도 각각 읽어 보관해요.
quantity_text = input()
price_text = input()
# TODO: 입력값을 숫자로 바꾸고 주문 정보를 정리해 보세요.

quantity_int = int(quantity_text)
price_int = int(price_text)
price_total = quantity_int * price_int
price_out = ""
for i in range(len(str(price_total))):
    if (i+1) % 3 != 0:
        price_out += (str(price_total))[-i-1]
    else:
        price_out += (str(price_total))[-i-1] + ","

price_out = price_out[::-1]

str_1 = f"이름: {name}"
str_2 = f"수량: {quantity_int}개"
str_3 = f"금액: {price_out}원"

result = f"{str_1}\n{str_2}\n{str_3}"
# 3) 완성한 결과를 출력해요.
print(result)
