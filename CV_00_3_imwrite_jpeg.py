"""

1. 개요
    영상 파일을 3채널(imgC)과 1채널(imgM)로 2회 읽어 들여
    이를 JPG 형식으로 저장한 파일들의 크기를 원본 파일과 비교한다.
    * 원본 파일의 압축이 덜 되어 있다면
      '원본 파일>3채널 JPEG 파일> 1채널 JPG 파일' 순으로 파일 크기가 정해진다.

2. 동작
      단계 1: 영상 파일을 3채널(imgC)과 1채널(imgM)로 2회 읽어 들인다.
            imgC.shape=(512, 768, 3), imgM.shape=(512, 768)
      단계 2: 두 영상 어레이를 JPG 형식으로 저장한다.
            jpg는 손실압축(lossy compression) 기법을 사용한다.
            확장자를 제거한 파일명: fname= monarch
      단계 3: 두 파일의 영상을 읽어들이고 화면에 출력한다.
            두 영상 어레이의 shape 중 채널 수가 다르다.
            imgCC.shape=(512, 768, 3), imgMM.shape=(512, 768)
      단계 4: 파일 크기를 비교한다.
            원본=monarch.bmp: 파일의 크기=1,179,702
            컬러=tmp_color_monarch.jpg: 파일의 크기=143,723
            모노=tmp_mono_monarch.jpg: 파일의 크기=121,336

3. 중요 함수 설명
      새로운 함수 없음.
4. 질문
    1. 영상 파일을 읽을 때 컬러 파일을 1채널의 모노 파일로 읽어 들이는 방법은?
    2. 1채널의 모노 영상을 3채널의 컬러 데이터로 읽어 들이는 방법은?


"""

import cv2 as cv
import numpy as np

# ----------------------------------------------------------------------------------------------------------------------
# 단계 0 :  영상이 존재하는 폴더와 파일 이름을 지정하기.
# ----------------------------------------------------------------------------------------------------------------------
#Path = 'd:\Work\StudyImages\Images\\'       # \\ 오류 발생 방지. \만 쓰면 오류.
#Path = 'd:/Work/StudyImages/Images/'
#Path = '../../Images/'               # 현재 상위 폴더의 상위 폴더 아래에 있는 Images 폴더.
Path = '../data/'       # . 현재 폴더, .. 바로 윗 폴더, ../data/ => 현재 폴더 바로 위 폴더 아래에 있는 data 폴더 아래
Name = 'RGBColors.JPG'
Name2= 'colorbar_chart.jpg'
Name = 'lenna.tif'
#Name = 'monarch.bmp'                # 압축이 되어 있지 않는 파일
FullName = Path + Name


# ----------------------------------------------------------------------------------------------------------------------
print("\n단계 1: 영상 파일을 3채널(imgC)과 1채널(imgM)로 2회 읽어 들인다.")
# cv.imread(파일, flags)에서; -1=있는 그대로 읽기. 0=모노(1채널)로 읽기, 1=컬러(3채널)로 읽기(default)
# ----------------------------------------------------------------------------------------------------------------------
#flags = cv.IMREAD_COLOR                    # 3채널로 읽는다. default. =1
imgC = cv.imread(FullName, 1)         # ==> 같음. flags = cv.IMREAD_COLOR
#imgC = cv.imread(FullName)         # 위와 같은 동작을 한다. flag를 밝히지 않으면 그 값은 1이다.
# imread()는 입력 영상을 제대로 읽어오지 못하면 None를 반환한다.

# 영상 파일 읽기를 실패하면(예를 들어 파일이 없을 때) 오류 메시지를 출력하고 프로그램을 중지한다.
# assert condition, message  : condition이 false이면 message를 출력하면서 AssertError 발생.
assert imgC is not None, f'No image file [{Name}] ....!'
# imgC가 None이 아니라는 것이 false이면 f-string 메시지를 출력하면서 중지한다.

imgM = cv.imread(FullName, 0)      # IMREAD_GRAYSCALE = 0. Read in mono.
print(f"imgC.shape={imgC.shape}, imgM.shape={imgM.shape}")

cv.imshow("Color 3 channel", imgC)
cv.imshow("Mono 1 channel", imgM)
cv.waitKey()


# ----------------------------------------------------------------------------------------------------------------------
print("\n단계 2: 두 영상 어레이를 JPG 형식으로 저장한다."
      "\njpg는 손실압축(lossy compression) 기법을 사용한다.")
# ----------------------------------------------------------------------------------------------------------------------
# 파일 이름에서 3글자 확장자(.bmp, .jpg, .png 등 점 포함)를 제거한다.
fname = Name[0:-4]
print("확장자를 제거한 파일명: fname=", fname)
fname_color = f"tmp_color_{fname}.jpg"
fname_mono = f"tmp_mono_{fname}.jpg"

cv.imwrite(fname_color, imgC)
cv.imwrite(fname_mono, imgM)

# ----------------------------------------------------------------------------------------------------------------------
print("\n단계 3: 두 파일의 영상을 읽어들이고 화면에 출력한다."
      "\n두 영상 어레이의 shape 중 채널 수가 다르다.")
# ----------------------------------------------------------------------------------------------------------------------
imgCC = cv.imread(fname_color, cv.IMREAD_UNCHANGED)     # -1로 써도 됨. 채널수를 바꾸지 말고 있는 그대로 읽어들인다.
imgMM = cv.imread(fname_mono, cv.IMREAD_UNCHANGED)     # -1로 써도 됨. 채널수를 바꾸지 말고 있는 그대로 읽어들인다.

cv.imshow(fname_color, imgCC)
cv.imshow(fname_mono, imgMM)
print(f"imgCC.shape={imgCC.shape}, imgMM.shape={imgM.shape}")
cv.waitKey()

# ----------------------------------------------------------------------------------------------------------------------
print("\n단계 4: 파일 크기를 비교한다.")
import os
original_size = os.path.getsize(FullName)
color_size = os.path.getsize(fname_color)
mono_size = os.path.getsize(fname_mono)
print(f"원본={Name}: 파일의 크기={original_size:,}")
print(f"컬러={fname_color}: 파일의 크기={color_size:,}")
print(f"모노={fname_mono}: 파일의 크기={mono_size:,}")
