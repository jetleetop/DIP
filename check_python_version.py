"""

개요
    현재 수행 중인 파이썬과 여러 모듈들의 버전을 출력한다.

동작
    sys 모듈을 import한 후 이것의 멤버 변수인 sys.version을 출력하여 확인한다.

#참고
#    이것 말고 명령 프롬프트에서 파이썬을 버전 옵션을 주어 출력하는 방법도 있다.
#    주의할 것은 파이썬의 path 설정에 따라 원하지 않는 파이썬이 설치될 수 있으므로 다음 사례와 같이 수행하여 확인할 수 있다.
        C:/>python --version     # 간단히 "python -V"도 됨
"""

# 파이썬 버전을 출력해 본다...
import sys          # 파이썬이 설치될 때 함께 설치된 내장 모듈 -> 사용할 때는 import만 하면 된다.
print("설치된 파이썬 버전=", sys.version)
print(f"설치된 파이썬 버전={sys.version}")
# 터미널 창에서 "python --version" 혹은 "python -V" 명령어을 출력하여 확인해 보는 방안도 있다.

# 모듈 OpenCV 버전을 출력해 본다; 영상처리 함수를 모아 놓은 모듈
import cv2 as cv    # opncv-contrib-python 모듈을 추가 설치한 모듈. 모듈의 이름은 cv2이다.
print(f"설치된 OpenCV 버전={cv.__version__}")    # cv2를 cv로 바꾸어 로드하였다.

# 모듈 numpy 버전을 출력해 본다; 수학적 처리 함수를 모아 놓은 모듈. cv설치 시 자동 설치(?)
import numpy as np
print(f"설치된 numpy 버전={np.__version__}")    # numpy를 np로 바꾸어 로드하였다.

# 모듈 matplotlib 버전을 출력해 본다; 그랙픽 처리를 모아 놓은 모듈
import matplotlib
print(f"설치된 matplotlib 버전={matplotlib.__version__}")

# 모듈 pip 버전을 출력해 본다; 파이썬 모듈(패키지) 관리를 위한 수행 script. 파이썬과 함께 자동 설치
import pip
print(f"설치된 pip 버전={pip.__version__}")

# 모듈 setuptools 버전을 출력해 본다; 파이참 모듈 설치를 위한 기본 모듈. 파이참과 함께 자동 설치
import setuptools
print(f"설치된 setuptools 버전={setuptools.__version__}")

import PIL  # 모듈 pillow; 영상처리 함수들... matplotlib 설치시 함께 자동 설치(?)
print(f"설치된 PIL(pillow) 버전={PIL.__version__}")
