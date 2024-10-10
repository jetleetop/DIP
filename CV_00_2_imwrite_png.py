"""

1. 개요
    3채널로 읽어들인 영상을 png 파일로 저장하여 이를 다시 읽어 보아 원본 영상의 어레이와 같은지 확인해 본다.
    본 예제에서는 png 형식의 파일로 저장한다.
    PNG 형식은 png 무손실 압축(lossless compression) 기법을 사용한다.

2. 동작
    단계 1: 영상 파일을 3채널(imgC) 형식으로 읽어들인다.
    단계 2: 읽어낸 영상 데이터(imgC)를 png 형식으로 저장한다.
    단계 3: 저장된 파일을 어레이 tmp로 다시 읽어낸다.
    단계 4: 원본 데이터(imgC)와 png 파일로 저장했다가 다시 읽어낸 영상 데이터(tmp)가 같은지 확인한다.
        1) np.array_equal(imgC, tmp): 원본 어레이와 이를 저장한 파일을 읽어들인 어레이의 모든 원소 값이 같다? ->True
        2) np.all(imgC == tmp): 원본 어레이와 이를 저장한 파일을 읽어들인 어레이의 모든 원소 값이 같다? ->True
        3) 참고 (imgC == tmp): 원본 어레이와 이를 저장한 파일을 읽어들인 어레이의 모든 원소 값이 같다? ->[[[ True  True  True]
          [ True  True  True]
          [ True  True  True]
          ...
          [ True  True  True]

        * 주의!!!: 3)번의 비교 결과는 영상의 각 요소들을 개별로 비교한 결과를 반환한다...

3. 중요 함수
    1) imwrite(파일이름, 어레이)
        어레이의 영상을 지정된 파일이름으로 저장한다. png외에도 여러가지 확장자를 지원한다....
    2) np.array_equal(imgC, tmp)
        두 어레이 각 요소가 개별적으로 모두 같은지 비교하여 모두 같으면 True를 반환한다. 한 개라도 다르면 false
        두 어레이의 sahpe가 같아야 비교 가능하다.
    3) np.all(imgC == tmp)
        위와 같음.

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
#Name = 'monarch.bmp'
FullName = Path + Name


# ----------------------------------------------------------------------------------------------------------------------
print("\n단계 1: 영상 파일을 3채널(imgC) 형식으로 읽어들인다.")
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

cv.imshow(Name, imgC)
cv.waitKey()

# ----------------------------------------------------------------------------------------------------------------------
print("\n단계 2: 읽어낸 영상 데이터(imgC)를 png 형식으로 저장한다. ")
# ----------------------------------------------------------------------------------------------------------------------
tmp_file = "tmp_002.bmp"     # 저장할 파일 이름
cv.imwrite(tmp_file, imgC)

# ----------------------------------------------------------------------------------------------------------------------
print("\n단계 3: 저장된 파일을 어레이 tmp로 다시 읽어낸다.")
# ----------------------------------------------------------------------------------------------------------------------
tmp = cv.imread(tmp_file)
cv.imshow(tmp_file, tmp)
cv.waitKey()

# ----------------------------------------------------------------------------------------------------------------------
print("\n단계 4: 원본 데이터(imgC)와 png 파일로 저장했다가 다시 읽어낸 영상 데이터(tmp)가 같은지 확인한다.")
# ----------------------------------------------------------------------------------------------------------------------
is_equal = np.array_equal(imgC, tmp)
print(f"1) np.array_equal(imgC, tmp): 원본 어레이와 이를 저장한 파일을 읽어들인 어레이의 모든 원소 값이 같다? ->{is_equal}")

is_equal = np.all(imgC == tmp)      # 모든 요소가 같은지 확인한다.
print(f"2) np.all(imgC == tmp): 원본 어레이와 이를 저장한 파일을 읽어들인 어레이의 모든 원소 값이 같다? ->{is_equal}")

is_equal = imgC == tmp      # 모든 요소가 같은지 확인한다.
print(f"3) 참고 (imgC == tmp): 원본 어레이와 이를 저장한 파일을 읽어들인 어레이의 모든 원소 값이 같다? ->{is_equal}")
exit()


# ----------------------------------------------------------------------------------------------------------------------
print("\n심층 단계: 압축 품질을 지정하여 png로 저장한다. default=1.")
# 이곳은 CV_00_4를 연습한 후 다시 도전해 주세요....
#  lossless compression을 사용하므로 화질의 차이는 없다(?). --> 진짜 화질 차이가 없는지 사례를 통해 확인해 보세요.
#  JPG 파일보다 용량이 매우 크며, 품질을 달리 지정해도 파일의 크기의 차이도 별로 없다.
#  압축을 많이 하면 파일 크기만 약간 줄어들고 압축하는데 시간이 훨씬 더 많이 소요된다.
#  단지 압축 시간의 차이가 조금 있을 뿐...
# ----------------------------------------------------------------------------------------------------------------------
fname = 'tmp_png'
quality = 1              # png 파일의 품질. 0~9로 지정. 높은 값(9)이 압축이 심하다고 하나 약간 줄어들며 대신 압축시간이 더 걸림.
file_png = f'{fname}(q={quality:#02d}).png'
cv.imwrite(file_png, imgC, (cv.IMWRITE_PNG_COMPRESSION, quality) )
print(f"\n4.3) 'imgC' was saved in '{file_png}' with quality={quality} PNG format.")
img = cv.imread(file_png)
cv.imshow(f"4.3 '{file_png}'", img)
cv.waitKey(0)       # 이곳에서 키보드 입력을 기다린다.
exit()
