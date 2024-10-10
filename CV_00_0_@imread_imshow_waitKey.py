"""

** 파이참 최신 버전을 사용할 경우 발생할 수 있는 오류에 대한 대처 방안
    1) Unresolved reference 오류:
        적법한 변수에 빨간 줄이 그어져 있어 경고 오류를 암시한다.
        실제로는 실행에 지장이 없다.
        => PyCharm을 수행할 때 관리자 모드로 수행한다. 한 번만 하면 다음부터는 나타나지 않는다.
    2) Cannot Run Git: Git is not installed
        Git를 사용하지 않는 사용자는 이 경고오류가 매번 출력되어 불편하다.
        => 파이참 우측 상단의 설정(톱니바퀴 아이콘)에서
        PyCharm 2022.2:
        Directory Mappings -> VCS(Vesrion Control System)에서 Git로 설정된 것을 <none>으로 설정한다.
        PyCharm 2023.2
        Settings => Version Control => Directory Mappings => VCS에서 Git로 설정된 것을 <none>으로 설정한다.
        설정이 바뀐 것을 확인하려면 PyCharm를 종료한 후 다시 수행하면 된다.

1. 개요
    아래 3개 목표을 달성하기 위해 OpencCV 함수 기반으로 영상 파일을 읽어들여 화면에 출력하는 방법을 소개한다.
    목표1: imread(), imshow(), waitKey()- 3개 함수의 기본적인 용법을 익힌다.
    목표2: 영상 데이터형의 기본 내용을 익힌다. 여기서는 변수 a
        -> type(a)=<class 'numpy.ndarray'>, a.shape=(512, 768, 3), a.dtype=uint8
    목표3: imshow()는 waitKey()가 있어야 화면 출력이 된다는 사실을 검증하는 루틴(맨 마지막 부분의 주석문 처리된 코드)을 이해한다.

2. 동작
      단계1: imshow() - 영상을 읽어온다.
            현재의 위치에서 상위 폴더의 data 폴더에는 이번 시간 다룰 샘플 영상과 비디오 동영상을 저장하였다.
      단계2: waitKey() - 영상을 출력한다. 그리고, 영상 어레이의 중요 속성을 출력해 본다.
            type(a)=<class 'numpy.ndarray'>, a.shape=(512, 768, 3), a.dtype=uint8
      단계3: waitKey() - 키 입력 기다리기. 실제로는 cv.waitKey() 함수가 수행되어야 화면에 영상이 출력된다.
      단계4: 다른 영상 파일을 읽어들여(imread()) 출력(imshow(), waitKey())한다.

3. 중요 함수
    더 자세한 내용이 알고 싶다면?
    각 함수의 자세한 용법은 https://docs.opencv.org/에 가서 버전 번호를 선택하 후
    새로 열리는 창의 우측 검색 창에서 함수명을 입력하여 검색한다.

    1) imread(): 파일에서 영상 데이터를 읽어 어레이로 반환하기.
        img=cv.imread("abc.jpg") - 영상 파일("abc.jpg") 읽어 영상 어레이(img)에 반환한다.
    2) imshow(): 어레이를 화면에 출력하기.
        imshow("win", img) - 영상 어레이(img)를 지정된 타이틀 ("win")의 창에 출력한다.
    3) waitKey(): 키 입력 기다리기. 이 명령에 의해 imshow()의 수행 내용이 실제 화면에 출력된다.
        waitKey()=waitKey(0) or waitKey(500) - 키입력을 무한 혹은 500[ms]동안 기다린다:

4. 미션
    미션1: 현재의 프로그램을 monarch와 smooth영상 모두 출력한 후 키 입력을 받을 때까지 무한정 기다리도록 수정하시오.

    미션2: 아래 주어진 조건의 영상을 화면에 출력한다.
        1) 0번의 수행 프로그램의 수행화면(영상 출력 결과-monarch와 smooth영상 및 PyCharm 화면)을
           윈도 보조프로그램의 캡처도구를 이용하여 적당한 이름(자신의 영문 이니셜)의 JPG파일로 저장한다.
        2) 캡처도구에서 저장한 파일을 현재의 폴더로 복사해 넣는다.
        3) 저장한 파일을 읽어 출력 후 무한정 대기하다가 아무 키나 입력하면 프로그램을 종료한다.
        요령: 본 예제 프로그램을 다른 이름으로 저장한 후 그 프로그램을 기반으로 수정하여 작성하는 것이 쉽습니다.

    미션3: 위 프로그램이 완성되면 다음의 수정 내용을 반영하여 다시 작성한다.
        1) 캡처한 파일을 data 폴더에 저장한다. 파이썬에서는 "c:\\data" 혹은 "c:/data"로 표기합니다.
        2) 화면(윈도) 타이틀에는 영상파일의 이름이 path까지 출력될 수 있도록 수정한다. 예: "c:/data/jhk.jpg"
        주의: OpenCV는 한글 처리가 되지 않을 수 있습니다. 가능한 한글폴더나 한글파일 이름을 지양해 주세요.
"""

import cv2 as cv

# 만약, No module named 'cv2' 오류(cv2에 설치가 안되었음을 의미하는 붉은 밑줄이 그어져있다)가 보인다면?
# opencv(opencv-python)를 설치했는데도 붉은 밑줄이 그어져 있다면 파이참을 종료하고 다시 수행하면 바로 잡힙니다.
# 파이참이 현재 설정을 아직 update하고 있지 못해 생긴 잠정적인 오류입니다.

print("\n단계1: imshow() - 영상을 읽어온다.  "
      "\n현재의 위치에서 상위 폴더의 data 폴더에는 이번 시간 다룰 샘플 영상과 비디오 동영상을 저장하였다.")
a = cv.imread("../data/monarch.bmp", 0)
# 영상 파일이 해당 폴더에 있어야 한다.

print("\n단계2: waitKey() - 영상을 출력한다. 그리고, 영상 어레이의 중요 속성을 출력해 본다.")
# print('type(a)={}, a.shape={}, a.dtype={}'.format(type(a), a.shape, a.dtype))
print(f"type(a)={type(a)}, a.shape={a.shape}, a.dtype={a.dtype}")
cv.imshow("test1", a)  # 영상 보이기. 창의 이름(test1)에 어레이 영상(a)를 출력한다.

print("\n단계3: waitKey() - 키 입력 기다리기. 실제로는 cv.waitKey() 함수가 수행되어야 화면에 영상이 출력된다.")
cv.waitKey()  # ()안에 기다리는 시간을 [ms] 단위로 입력한다. 인자가 없으면 무한정 키를 기다린다.

print("\n단계4: 다른 영상 파일을 읽어들여(imread()) 출력(imshow(), waitKey())한다.")
print("주의!!: 화면 출력은 imshow()와 waitKey()함수에 의해 이루어진다.")
b = cv.imread("../data/smooth.jpg", -1)     # 가장 권장하는 방법
#b = cv.imread("..\\data\\smooth.jpg")  # 차선책
#b = cv.imread("..\data\smooth.jpg")     # SyntaxWarning: \\(2개)가 필요하다.
cv.imshow("test2", b)  # 영상 보이기. 창의 이름(test2)에 어레이 영상(a)를 출력한다.
print(f"b.shape{b.shape}")
cv.waitKey(10000)  # 10000[ms]=10초 기다리기. 중간에 키입력 들어오면 빠져나간다.
# 프로그램이 종료되면 열려져 있는 창들은 자동으로 모두 닫힌다.


'''
# waitKey()를 수행하지 않으면 화면에 출력이 되지 않는다.
# 이것을 확인하고 싶으면 상단의 cv.waitKey(10000)을 주석처리하고 이 주석문을 해제하여 수행하여 보세요...
anykey = input("마지막으로 수행되는 waitKey()를 지우고 이곳에서 아무 키나 입력해 보세요....>")
print(f"키보드 입력={anykey}")
print("9초의 지연시간후 종료합니다. test2 화면에 아무 것도 보이지 않은 상태에서 종료하는 것을 관찰할 수 있습니다. ")
import time
time.sleep(9)
'''
