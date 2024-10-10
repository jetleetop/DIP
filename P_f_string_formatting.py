"""

print() 함수를 통한 데이터 출력 방법
    1) .format()을 이용하여 출력하기- string 자료형(사실상 object)의 메소드를 사용하기
    2) %-formatting를 이용하여 출력하기- Python 2의 방식
==> 3) f-string을 이용하여 출력하기 -  Literal String Interpolation.
        Python 3.6 이후 버전 가능. 고속 처리. 간편 사용.
        tuple, list 형의 데이터에 대해서도 적용 가능하다(취소. 그렇지 않은 것으로 판단됨).
"""


# -------------------------------------------------------------------------------------
# 실습 3: f-string 사용. Literal String Interpolation.
# f"~" 형식으로 따옴표 내부를 지정한 형식의 스트링 자료로 만든다.
# f-Strings: A New and Improved Way to Format Strings in Python - 3.6 이후에서 활용가능...
#   https://bluese05.tistory.com/70
#   https://www.python.org/dev/peps/pep-0498/
# 장점:
# F-strings provide a concise, readable way to include the value of Python expressions inside strings.
# int, float, str외에도 list, tuple 형 데이터에 대해서도 적용 가능하다.
# 실험에 의하면 출력 형식 지정 방법에 있어 c, s는 오류가 발생하였다. - 문자 혹은 스트링 변환 출력이 f-string에 대해서는 이루어지지 않았다.
# -------------------------------------------------------------------------------------
a = 'Kim?'
print(1, f'Hi, {a}')       # 출력 대상이 스트링형이면 그대로 출력.
# 출력 결과 =>1 Hi, Kim?

a = 13
print(2, f'I have {a} apples.')
# 출력 결과 =>2 I have 13 apples.

b = f'I have {a:#5.2f} apples.'     # I have 13.00 apples.
print(3, b)
# 출력 결과 =>3 I have 13.00 apples.

value = 12
print(4, f'input={value:#04x}')        # input=0X000c
# 출력 결과 =>4 input=0X000c

print(5, f'value={2.2838:#7.2f}')      # value=___2.28
# 출력 결과 =>5 value=   2.28

str1 = 'study'; num1 = 10; num2 = 90.123456780
print(f'6 |str1={str1}|num1={num1}|num1_in_3d={num1:#3d}|num2={num2:#f}|num2_in_5.3e={num2:#5.3e}')
# 출력 결과 =>6 |str1=study|num1=10|num1_in_3d= 10|num2=90.123457|num2_in_5.3e=9.012e+01
# 부동소수이하의 자리수 출력을 제어하지 않으면 보통 소수 6자리까지만 출력한다; num2={num2:#f} => num2=90.123457

# 문자열 출력 여백 제어 formatting
# :k> 10 총 10칸 공백, 공백문자 k, 오른쪽 정렬,
# :k< 10 총 10칸 공백, 공백문자 k, 왼쪽 정렬,
# :k^ 10 총 10칸 공백, 공백문자 k, 가운데 정렬,
print(f"7 |{str1:*>10}|{str1:*<10}|{str1:*^10}|{str1:^10}|")


# 3가지 프린트 형식 지정 방식 비교....
x = 10; y = 3
print(8.1, f'x + y = {x+y} | x * y = {x*y}')             # f-string 방식. 간결하고 읽기 편하다.
# 출력 결과 =>7 x + y = 13 | x * y = 30

print(8.2, 'x + y = %d | x * y = %d' % (x+y, x*y))        # %-formatting 방식
# 출력 결과 =>8 x + y = 13 | x * y = 30

print(8.3, 'x + y = {} | x * y = {}'.format(x+y, x*y))   # format 메서드 방식
# 출력 결과 =>9 x + y = 13 | x * y = 30

# 아쉽지만 아래와 같이 여러 요소를 갖고 있는 변수에 대해서 공통적인 양식으로 출력할 수는 없다.
# tuple, list 형의 데이터에 대해서는 적용이 불가능한 것으로 보인다.
#a = [2.2838, 123.234, 3.56]; print(9, f'{a:#7.2f}')   # 오류 발생

c_age = 17; n_age = 18
msg = (f"I am {c_age} " f"going on {n_age}.")
msg2 = ["hello""world"]
msg3 = ("hello""world")     # string으로 묶는다.
msg4 = "hello""world"
print(9, type(msg), type(msg2), type(msg3), type(msg4))
print(10, msg, msg2, msg3, msg4)



exit()
#"""



# ========================================================================================================================
# 조금 더 복잡한 사례: 기록용....
# 입문자에게는 비추천!!!!
# ========================================================================================================================

"""
# -----------------------------------------------------------------------------------------------------------------
# 암시적인 줄 연결이 가능한 경우
# 다음과 같이 (), [], {}로 묶여진 자료 데이터는 Implicit line joining이 가능합니다.
# -----------------------------------------------------------------------------------------------------------------
month_names = ['Januari', 'Februari', 'Maart',      # These are the
               'April',   'Mei',      'Juni',       # Dutch names
               'Juli',    'Augustus', 'September',  # for the months
               'Oktober', 'November', 'December']   # of the year

print(month_names)
"""


"""
# -----------------------------------------------------------------------------------------------------------------
# .format()과 %를 섞어서 사용한 경우..
# Literal %: %문자를 표현할 때는 %%을 사용한다.
# "^^수자"를 이용하여 빈칸 채우기 
# -----------------------------------------------------------------------------------------------------------------
print('text1={1}|text0={0}|1st %%=%f|3th format parameter={3}|2nd %%=%s|3rd %%=%s'           # 이때는 주석문 가능
      .format('TEXT0', 'TEXT1', num2, num1) % (num2, str1, num2))

# 밑줄(_)로 11칸을 채우고 가운데 정렬(^)하기 (___hello___)
print('{0:_^11}'.format('hello'))
print('{0:*^11}'.format('hello'))
exit(0)
"""


"""
# -----------------------------------------------------------------------------------------------------------------
# numpy를 학습후에는 numpy array의 데이터를 출력을 제어하는 방안에 대해 검토해 보자.
# -----------------------------------------------------------------------------------------------------------------
import numpy as np
y=np.array([1.5e-10, 1.5, 1500])
print(y)          # [  1.500e-10   1.500e+00   1.500e+03]
np.set_printoptions(suppress=True)
print(y)          # [    0.      1.5  1500. ]

y = np.array([1.5383948475e-10, 14568.34574090, 1500.990002, 19.29288e-6])
print('\n', y)

np.set_printoptions(precision=2)
print(y)

def ndprint(a, format_string='{0:.2f}'):
    print([format_string.format(v, i) for i, v in enumerate(a)])
ndprint(y, '{:10.4e}')
exit(0)
"""

