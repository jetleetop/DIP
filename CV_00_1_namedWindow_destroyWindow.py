"""

** 파이참 최신 버전을 사용할 경우 발생할 수 있는 오류에 대한 대처 방안
    1. Unresolved reference 오류:
        적법한 변수에 빨간 줄이 그어져 있어 경고 오류를 암시한다.
        실제로는 실행에 지장이 없다.
        => PyCharm을 수행할 때 관리자 모드로 수행한다. 한 번만 하면 다음부터는 나타나지 않는다.
    2. Cannot Run Git: Git is not installed
        Git를 사용하지 않는 사용자는 이 경고오류가 매번 출력되어 불편하다.
        => 파이참 우측 상단의 설정(톱니바퀴 아이콘)에서
        PyCharm 2022.2:
        Directory Mappings -> VCS(Vesrion Control System)에서 Git로 설정된 것을 <none>으로 설정한다.
        PyCharm 2023.2
        Settings => Version Control => Directory Mappings => VCS에서 Git로 설정된 것을 <none>으로 설정한다.
        설정이 바뀐 것을 확인하려면 PyCharm를 종료한 후 다시 수행하면 된다.


1. 개요
    목표 1: 아래 함수의 용법에 대해 살펴 본다.
    1) imread() 함수에 파일이름 외에 추가로 읽기 모드가 지원된다. --> imread(파일이름, 읽기모드)
    - 읽기모드 = 무조건 컬러로(3채널, default), 무조건 모노로..(1채널), 파일에 따라(컬러=3채널 혹은 모노=1채널)
    2) ch = waitKey()로 키 입력을 반환 받을 수도 있다. 아직 쓸 데는 없지만...
    3) namedWindow()함수의 사용법을 살펴 본다. namedWindow(창의_이름)
    - 영상 데이터 없이 일단 창을 먼저 연다. 창의 크기는 랜덤하다. 창의 이름만 지정한다.
    4) destroyWindow() 함수의 사용법을 살펴 본다. destroyWindow(창의_이름)
    - 프로그램을 종료하지 않고도 창의 이름을 지정하여 지정한 창을 닫는다.
    - destroyAllWindows() 인자는 없다. 열려진 모든 창들을 닫는다.

    목표 2: 영상을 담는 데이터형에 대해 고찰한다.
    - 영상을 담은 데이터는 numpy모듈에서 지원하는 ndarray type을 사용한다.

2. 동작
    단계 1: 영상 파일의 영상을 읽어 그 영상의 속성(크기, 채널 수..)을 출력한다.
         Color Image: imgC
         type : <class 'numpy.ndarray'>
         shape =  (512, 768, 3)     # 컬러 모드로 읽기
         img type =  uint8
         row =  512
         column =  768
         channel =  3
         itemsize =  1

    단계 2: namedWindow()로 빈 화면을 3초간 출력한 후 imshow()를 수행한다.
    그러나, imshow()만으로는 화면에는 출력이 되지 않는다. waitKey()도 수행해야 화면에 출력된다.
    3초동안 그림이 보이지 않습니다. 3초 후에 그림이 나타날 것입니다.
    imshow() 수행 완료. 그림이 출력되었고 이제 키를 기다립니다.
    키를 받았습니다. 창을 닫았습니다.

    단계 3: 이번에는 같은 파일을 mono로 읽어내어 출력하고,
    키를 입력하면 destroyWindow() 함수를 사용해 모노 창만 지정하여 닫는다.
    이때 키의 ASCII 값을 화면에 출력해 본다.

         Mono Image: imgM
         type : <class 'numpy.ndarray'>
         shape =  (512, 768)
         img type =  uint8
         row =  512
         column =  768
         itemsize =  1
        Pressed key: ASCII=20, chr=' '      # space bar를 눌렀다...

    단계 4: 키를 입력하면 destroyAllWindows() 함수로 나머지 창(사실상 1개)들을 모두 닫는다.
    Pressed key: ASCII=41, chr='A'      # 'A'문자를 눌럈다.

3. 중요 함수 설명
    * 주의: 함수 파라미터 해석
        아래 함수 설명에서 []은 optional arguement를 지정할 때 쓰이는 표현이다.
        지정하지 않으면 default 설정이 사용된다.

    1) imread(): 영상 파일 읽기
    retval = cv.imread(filename[, flags])
        본 함수를 통해 지정된 영상을 읽어내어 영상 데이터를 numpy.ndarray 객체로 반환한다.
        영상 파일("abc.jpg") 읽어 영상 어레이(img)에 반환하기: => img=cv.imread("abc.jpg", 열기_모드)

        filename = 영상 파일의 이름. 거의 모든 파일 양식(bmp. tif, jpg, png 등)을 지원. path도 함께 지정가능.
        flags = 읽어 내는 모드. 다음 3가지 중 하나. 지정하지 않으면 default 값(1)이 쓰인다.
            cv.IMREAD_COLOR = 1     default. 컬러영상을 row x column x channel의 3차원 ndarrary로 읽어 반환한다.
                                    컬러 채널 배열 순서는 B, G, R 순이다.
                                    모노 영상도 3채널(BGR) 영상으로 확장하여 읽는다. 이 경우 각 채널에는 같은 값이 들어 있다.
            cv.IMREAD_UNCHANGED = -1 있는 그대로 열기. 모노 영상은 모노, 컬러영상은 컬러 있는 그대로 읽어들인다.
            cv.IMREAD_GRAYSCALE = 0 컬러 영상, 모노 영상 모두 모노영상(1채널)으로 변환하여 읽어들인다.
        retval = numpy.ndarray 타입의 영상 데이터 객체.

    요약!!
        imread() 함수를 옵션없이 사용하면 모노 영상이라도 3채널 영상으로 읽어들인다.
        모노 그레이모드(flags=0) 옵션을 사용하면 컬러 영상이라도 1채널 영상 파일로 읽어 들인다.


    2) namedWindow(): 창을 생성해 보인다. 내용물은 없다. 빈 화면만 나온다. 크기가 때에 따라 달라진다.
        None = cv.namedWindow(winname[, flags])
            수행하면 winname(Name of window) 창을 생성하여 화면에 보인다. waitKey()없어도 창은 보인다.
            크기 정보가 없어서 열린 창의 크기는 유동적이다. 아직 내용물(영상)은 안보임.
            이 함수를 생략하고 바로 imshow()를 통해 영상을 출력해도 된다.

    3) imshow(): 어레이 영상을 화면에 보인다.
    None = cv.imshow(winname, array)              # array 영상을 winname 창에 출력한다.
        영상 어레이(img)를 지정된 이름("win")의 타이틀에 출력하기: imshow("win", img)
        아래 함수들은 cv.waitKey() 함수가 있어야 화면에 내용물을 출력한다.
            열려져 있는 winname 창이 없으면 생성한 후 영상을 출력한다.
            winname = Name of window
            array = Image to be shown

    4) waitKey(): 키 보드입력을 기다린다. 이 함수를 수행해야 imshow() 결과가 화면에 나타난다.
        키 입력을 무한(0) 혹은 지정된 시간(5000[ms])동안 기다려서 입력한 키를 반환한다.
        waitKey()는 waitKey(0)와 같이 무한대로 키 입력을 기다린다.
       지정된 시간이 경과하기 전에 키가 들어오면 더 이상 기다리지 않고 바로 반환한다.
    * 주의!!!: waitKey()를 수행해야 imshow()한 결과가 화면에 나타난다....

    3) 화면 창을 닫기
        destroyWindow("abc")
            타이틀 이름("abc")으로 지정된 창을 닫는다.
        destroyAllWindows()
            열려진 모든 창을 닫는다. 실행하지 않아도 종료시에는 모든 창이 자동으로 닫힌다.

4. 질문
    지정된 영상 파일이 존재하지 않으면 imread() 함수의 수행 결과는 어떻습니까? 오류 때문에 중지하나요?
    이 프로그램에서 영상 파일이 존재하지 않는다면 어떤 일이 일어나나요?
    영상 파일이 부재 상황시 발생하는 일과 이를 대비한 조치를 설명하여 보세요.


5. 미션
    아래 사례처럼 임의의 파일을 읽어 이것의 가로x세로 해상도와 영상 데이터의 크기(bytes)를 출력하시오.
    사례1: 파일이름: monarch.bmp
          가로x세로 = 768 x 512
          영상 데이터의 크기(bytes) = 1,138,928

    사례2: 파일이름: smooth.jpg
          가로x세로 = 512 x 240
          영상 데이터의 크기(bytes) = 122,880

    * 요령 및 조건:
    본 소스 파일을 다른 이름으로 저장하여 해당 소스 파일을 수정하여 작성하시오.
    다른 파일도 가능하도록 파일 이름은 본 예제 프로그램처럼 변수를 사용하시오.
    f-string 기법으로 print()문을 작성하세요.
    --> chatGPT 요청문: 십진수를 셋째 자리마다 comma(,)를 넣어 출력하는 파이썬 f-string print문을 작성 해 줘.
    컬러 영상 파일과 모노 영상 파일을 가리지 않고 적용할 수 있으면 만점입니다...


"""

import cv2 as cv


# ----------------------------------------------------------------------------------------------------------------------
# 섹션 1, 영상 파일 이름 정의 부분: 영상이 존재하는 폴더와 파일 이름을 지정한다.
# ----------------------------------------------------------------------------------------------------------------------
#Path = 'd:\\Work\\StudyImages\\Images\\'   # \\ 오류 발생 방지. \ 1개만 쓰면 오류.
# 백 슬래시를 1개만 사용해서 사용하고 싶다면 모든 파일 이름(Name) 앞에 백 슬래시 \를 붙여야 하는 번거로움을 감수해야 한다.
#Path = 'd:/Work/StudyImages/Images/'
Path = '../data/'       # . 현재 폴더, .. 바로 윗 폴더, ../data/ => 현재 폴더 바로 위 폴더 아래에 있는 data 폴더 아래
Name = 'lenna_mono.jpg'     # mono gray 영상. 1채널 영상
Name = 'RGBColors.JPG'
Name = 'colorbar_chart.jpg'
Name = 'lenna.tiff'
Name = 'smooth.jpg'         # mono gray 영상. 1채널 영상
#Name = 'monarch.bmp'
FullName = Path + Name
print("프로그램 시작.. 주의!! 한글 파일과 한글 폴더는 오류를 유발할 수도 있습니다.")
print("파일의 경로가 포함된 파일이름:", FullName)

# ----------------------------------------------------------------------------------------------------------------------
# 섹션 2: numpy.ndarray 데이터의 상세 내용(속성)을 출력하는 함수를 정의한다.
# 어레이 변수의 이름을 문자열로 입력받아 이 변수의 중요 정보를 출력한다.
# numpy.ndarray
#   https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html
# ----------------------------------------------------------------------------------------------------------------------

def printImgAtt(string, img):
    print("\n", string)
    print(' type :', type(img))           # imge type =  <class 'numpy.ndarray'>
    print(' shape = ', img.shape)      # 영상 어레이의 크기 알아내기. image shape =  (512, 768, 3). (행, 열, 채널)
    print(' img type = ', img.dtype) # 어레이 요소의 데이터 타입 알아내기. uint8 = unsigned 8비트.
    if len(img.shape) >= 2:
        print(' row = ', img.shape[0])  # shape는 tuple이다. 원소는 []로 지정. 리스트도 []로 지정한다.
        print(' column = ', img.shape[1])  # 열의 수.
        #if img.shape[2] == 3: # 이것은 모노 영상에 대해 오류 발생.
        if len(img.shape) == 3:
            print(' channel = ', img.shape[2])  # 채널의 수. 컬러 영상이면 3. 모도 영상이면 1.
    print(' itemsize = ', img.itemsize)    # 한 개의 원소를 이루는데 필요한 바이트의 수

"""
# 위 함수를 좀더 쉽게 사용하기 위해 개선하였습니다. 본 예제 프로그램에서는 활용하고 있지 않습니다.
# 파이썬 학습: eval() 함수의 용법을 잘 익혀야 이해할 수 있습니다.
def printImgAtt2(string):
    print("\n" + string)
    img = eval(string)             # 전달받은 스트링 문자열을 프로그램 소스의 변수에 반영한다.
    print(' type :', type(img))           # imge type =  <class 'numpy.ndarray'>
    print(' shape = ', img.shape)      # 영상 어레이의 크기 알아내기. image shape =  (512, 768, 3). (행, 열, 채널)
    print(' img type = ', img.dtype)    # 어레이 요소의 데이터 타입 알아내기. uint8 = unsigned 8비트.
    if len(img.shape) >= 2:
        print(' row = ', img.shape[0])  # shape는 tuple이다. 원소는 []로 지정. 리스트도 []로 지정한다.
        print(' column = ', img.shape[1])  # 열의 수.
        #if img.shape[2] == 3: # 이것은 모노 영상에 대해 오류 발생.
        if len(img.shape) == 3:
            print(' channel = ', img.shape[2])  # 채널의 수. 컬러 영상이면 3. 모도 영상이면 1.
    print(' itemsize = ', img.itemsize)    # 한 개의 원소를 이루는데 필요한 바이트의 수
"""
# ----------------------------------------------------------------------------------------------------------------------
print("\n단계 1: 영상 파일의 영상을 읽어 그 영상의 속성(크기, 채널 수..)을 출력한다.")
# cv.imread(파일, flags)에서; -1=있는 그대로 읽기(IMREAD_UNCHANGED). 0=모노(1채널)로 읽기, 1=컬러(3채널)로 읽기(default)
# ----------------------------------------------------------------------------------------------------------------------
read_mode = cv.IMREAD_COLOR         # 파일 읽어내는 모드 = 컬러 = 1. default
imgC = cv.imread(FullName, flags=read_mode)         # 주어진 모드로 읽어낸다.
# imread()는 입력 영상을 제대로 읽어오지 못하면 None를 반환한다. 중지하지 않는다.

# 영상 파일 읽기를 실패하면(예를 들어 파일이 없을 때) 오류 메시지를 출력하고 프로그램을 중지한다.
# assert condition, message  : condition이 false이면 message를 출력하면서 AssertError 발생.
assert imgC is not None, f'No image file [{Name}] ....!'
# imgC가 None이 아니라는 것이 false이면 f-string 메시지를 출력하면서 중지한다.

printImgAtt('Color Image: imgC', imgC)
# 미션 1: printImgAtt() 함수를 사용하여 imgC의 속성 정보를 출력하시오.



# ----------------------------------------------------------------------------------------------------------------------
print("\n단계 2: namedWindow()로 빈 화면을 3초간 출력한 후 imshow()를 수행한다. "
      "\n그러나, imshow()만으로는 화면에는 출력이 되지 않는다. waitKey()도 수행해야 화면에 출력된다.")
# ----------------------------------------------------------------------------------------------------------------------

winname_img ="imgC: ImReadMode=" + str(cv.IMREAD_COLOR)     # cv.IMREAD_COLOR=1. default. BGR color. 3 channel.
cv.namedWindow(winname_img)     # 수행 즉시 바로 창이 열린다.
print("3초동안 그림이 보이지 않습니다. 3초 후에 그림이 나타날 것입니다.")
# 미션 3(파이썬 연습): 위 메시지의 시간(초)를 변수로 지정하여(예: t=5) 출력하도록 바꾸어 보시오.

# imshow()를 수행하지 않아 빈 창이 열리는 것을 볼 수 있다.
# 그림의 크기를 모르므로 창의 크기는 때에 따라 달라질 수 있다.
cv.waitKey(3000)    # 괄호()안의 인수(ms)만큼 기다린다. 인수가 없으면 무한대로 기다린다.


cv.imshow(winname_img, imgC)  # 수행해도 그림은 출력되지 않는다. cv.waitKey()를 수행해야 영상을 출력한다.
print("imshow() 수행 완료. 그림이 출력되었고 이제 키를 기다립니다.")

cv.waitKey()        # 이제야 영상이 화면에 보인다.
print("키를 받았습니다. 창을 닫았습니다.")

# ----------------------------------------------------------------------------------------------------------------------
print("\n단계 3: 이번에는 같은 파일을 mono로 읽어내어 출력하고, "
      "\n키를 입력하면 destroyWindow() 함수를 사용해 모노 창만 지정하여 닫는다."
      "\n이때 키의 ASCII 값을 화면에 출력해 본다.")
# ----------------------------------------------------------------------------------------------------------------------

imgM = cv.imread(FullName, 0)      # IMREAD_GRAYSCALE = 0. Read in mono.
#imgM = cv.imread(FullName, IMREAD_GRAYSCALE)      # IMREAD_GRAYSCALE = 0. Read in mono.
#imgM = cv.imread(FullName, flags=0)
printImgAtt('Mono Image: imgM', imgM)
# 미션 2: printImgAtt2() 함수를 사용하여 imgM의 속성 정보를 출력하시오.

winname_imgM = "'imgM': ImReadMode=" + str(cv.IMREAD_GRAYSCALE)  # =0. mono gray. 1 channel.
cv.imshow(winname_imgM, imgM)
key = cv.waitKey(0)       # 키보드 입력을 무한정 기다린다.
print(f"Pressed key: ASCII={key:x}, chr='{chr(key)}'")
cv.destroyWindow(winname_imgM)     # 지정한 이름의 창을 닫는다. 모노 영상 창은 닫는다.


# ----------------------------------------------------------------------------------------------------------------------
print("\n단계 4: 키를 입력하면 destroyAllWindows() 함수로 나머지 창들을 모두 닫는다.")
# ----------------------------------------------------------------------------------------------------------------------
key = cv.waitKey()       # 0을 지정하지 않아도 키보드 입력을 무한정 기다린다.
print(f"Pressed key: ASCII={key:x}, chr='{chr(key)}'")
cv.destroyAllWindows()      # 모든 창을 닫는다. 이 루틴이 없어도 종료시에는 모두 닫는다.


