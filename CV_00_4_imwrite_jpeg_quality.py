"""

1. 개요
    영상 파일을 읽어들여 압축 품질(quality)을 지정하여 파일로 저장하는 방법에 대해 소개한다.

2. 동작
    단계 1: 영상 파일을 영상 파일을 컬러 모드(1, default)로 읽어 들인다.
    단계 2: 압축 품질(quality)을 지정하여 영상을 JPG 형식으로 저장한다.
        quality: 1 to 100. The higher is the better. quality is 95 default.
        확장자 없는 화일명: fname= monarch
        2.1) 압축 품질을 5로 지정하여 jpeg으로 저장한다.
            'imgC' was saved in 'tmp_monarch(q=05).jpg' with 'quality=5'.
            저장한 파일을 다시 읽어서 화면에 출력하여 영상의 품질을 확인한다.
        2.2) 압축 품질을 80으로 지정하여 jpeg으로 저장한다.
            'imgC' was saved in 'monarch(q=80).jpg' with 'quality=80'.
            저장한 파일을 다시 읽어서 화면에 출력하여 영상의 품질을 확인한다.

3. 중요 함수 설명
    1) 컬러 영상을 모노로 변환하기
        imgM = cv.cvtColor(imgC, cv.COLOR_BGR2GRAY)
    2) 영상을 주어진 품질(quality)로 JPEG 파일로 저장한다.
        cv.imwrite(파일이름, 어레이, (cv.IMWRITE_JPEG_QUALITY, quality))

4. 질문
    1. JPEG 파일로 저장할 때 quality를 지정하지 않으면 deafult로 사용되는 값은?
    2. quality=30, quality=50 중에서 화질이 더 우수한 파일은?
    3. quality=30, quality=50 중에서 파일의 크기가 더 작은 파일은?

5. 미션
    1. 본 프로그램에서 저장된 2개 파일의 크기를 출력하도록 프로그램을 수정하시오.
    2. PSNR은 높을 수록 원본 영상과 우수한 값을 반환하는 openCV 함수이다.
        높을 수록 원본과 가깝다고 할 수 있다. 대략 40dB 정도면 차이점을 육안으로 구별하기 어렵다.
       이 함수의 사용법을 조사하여 2개의 qulity를 지정한 영상들의 원본과의 PSNR을 구해
       어떤 quality 값으로 저장된 영상이 원본과 더 가까운지 판단하는 프로그램을 작성하시오.
"""

import cv2 as cv

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
FullName = Path + Name2


# ----------------------------------------------------------------------------------------------------------------------
print("단계 1: 영상 파일을 영상 파일을 컬러 모드(1, default)로 읽어 들인다.")
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

# ----------------------------------------------------------------------------------------------------------------------
print("단계 2: 압축 품질(quality)을 지정하여 영상을 JPG 형식으로 저장한다.")
print("quality: 1 to 100. The higher is the better. quality is 95 default.")
# 압축을 사용하는 파일 형식은 압축률을 통제할 수 있다.
# jpg와 png 형식의 파일로 저장한다. => 파일 이름의 확장자로 지정 가능하다.
# ----------------------------------------------------------------------------------------------------------------------
# 파일 이름에서 3글자 확장자(.bmp, .jpg, .png 등 점 포함)를 제거한다.
fname = Name2[0:-4]
print("확장자 없는 화일명: fname=", fname)

print("2.1) 압축 품질을 5로 지정하여 jpeg으로 저장한다.")

quality = 5              # quality : 1 to 100. The higher is the better. quality is 95 default.
file_qual = 'tmp_' + fname + f'(q={quality:#02d})'+'.jpg'              # 저장할 파일의 이름 = 원래이름+(q=05)
#여러 개의 파라미터를 제어할 때는 아래와 같이 파라미터 이름과 값을 나열하면 된다.
# 이들 파라미터는 리스트 혹은  튜플로서 한 개의 파라미터로 입력된다.
cv.imwrite(file_qual, imgC, (cv.IMWRITE_JPEG_QUALITY, quality))       # 영상을 주어진 품질(quality)로 저장한다.
print(f"'imgC' was saved in '{file_qual}' with 'quality={quality}'.")

print("저장한 파일을 다시 읽어서 화면에 출력하여 영상의 품질을 확인한다.")
img = cv.imread(file_qual)
cv.imshow(f"2.1 '{file_qual}'", img)
cv.waitKey(0)       # 이곳에서 키보드 입력을 기다린다.

print("2.2) 압축 품질을 80으로 지정하여 jpeg으로 저장한다.")
quality = 80              # quality : 1 to 100. The higher is the better. quality is 95 default.
file_qual = fname + f'(q={quality:#02d})'+'.jpg'              # 저장할 파일의 이름
cv.imwrite(file_qual, imgC, (cv.IMWRITE_JPEG_QUALITY, quality))       # 영상을 주어진 품질(quality)로 저장한다.
print(f"'imgC' was saved in '{file_qual}' with 'quality={quality}'.")

print("저장한 파일을 다시 읽어서 화면에 출력하여 영상의 품질을 확인한다.")
img = cv.imread(file_qual)
cv.imshow(f"2.2 '{file_qual}'", img)
cv.waitKey(0)       # 이곳에서 키보드 입력을 기다린다.


"""
#====================================================================================================================
# 참고용 -- 미션 과제(1): 다음 주어진 지시사항에 따라 동작하는 프로그램을 작성하시오.
# 변수 fname로 주어진 영상 파일에 대해 주어진 미션을 완수히시오.
# fname = "../data/colorbas_chart.jpg"      # 영상 파일. 단, 파일의 실제 이름은 바뀔 수도 있음.
# 1. 영상의 가로(column, 열) 및 세로(row, 행) 정보를 변수 a, b에 넣으시오.
#     힌트: a.shape, 이를 이용하여 영상의 가로, 세로 정보를 출력하면 된다. => print(f'가로={a}, 세로={b}')
# 2. 영상의 면적을 출력하시오. 사례 => 면적 = 23674834
# 3. 파일이 컬러인지 모노 영상인지를 검사하여 그 결과를 출력하시오. 사례 => 영상은 '컬러 혹은 모노'입니다.
# 4. 해당 영상을 화면에 출력하시오. 이때 파일 이름이 타이틀 바에 출력되어야 합니다.
#    경로(path)를 제외할 수 있으면 추가 점수 있음.
#
# 5. 읽은 영상을 quality를 지정하여 현재의 폴더에 JPG 영상으로 저장하시오. 파일 이름은 tmp.jpg
#    quality는 사용자의 입력을 받아 지정하게 하면 가점(아래 힌트 참조). 못하겠으면 5로 고정.
# 6. 저장된 영상을 읽어 화면에 출력하시오 이때 타이틀 바의 이름은 "quality=?"
#     ? 값은 5로 고정하거나, 사용자 입력으로 정한 값으로 정한다. 사용자 입력 가점.
#====================================================================================================================



#====================================================================================================================
# 힌트: 키보드 입력받아 정수로 변환하는 예제
#====================================================================================================================

# input() 함수로 받은 데이터는 string 형이다.
# 따라서 정수가 필요한 자리에 사용할 때는 이를 int() 함수를 사용하여 정수로 바꾸어야 한다.
abc = input("Type integer number = ")
print(f"You typed {abc}, type(abc)={type(abc)}")

q = int(abc)
print(q + 10)       # abc+10은 불가능. 스트링과 정수를 더할 수 없음.
"""








#====================================================================================================================
# 기록 보관용... 먼저 컬러 좌표계의 학습이 필요함.. => 나중에 다룸.
# 영상을 색차(chroma) 성분과 휘도(luminance) 성분으로 나누어 압축하는데 각각에 대한 압축품질을 개별로 설정할 수도 있다.
#q_chroma = 1; q_luma = 80
#file_qual2 = fname + f'_Chro={q_chroma:#02d}_Luma={q_luma:#02d}.jpg'  # 저장할 파일의 이름
#cv.imwrite(file_qual2, imgC, (cv.IMWRITE_JPEG_CHROMA_QUALITY, q_chroma, cv.IMWRITE_JPEG_LUMA_QUALITY, q_luma))
#print(f"3.2c) 'imgC' was saved in '{file_qual2}' with luminance quality={q_luma}, chroma quality={q_chroma}.")
#====================================================================================================================
