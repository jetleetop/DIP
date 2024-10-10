import cv2 as cv
import numpy as np

Path = '../data/'
Name = 'the_return_of_the_king.avi'
#Name = 'CV_Bullet Time and The Matrix.mp4'
Name = 'car_race1.mp4'
Name = 'car_race2.mp4'
Name = 'frozen.avi'
#Name = 'matrix.mp4'

FullName = Path + Name
#FullName = 'test.avi'           # 테스트용
#FullName = 'CamVid.avi'

capture = cv.VideoCapture(FullName)

frame_index = 0
scale = 1.0
# 기본적으로 모든 채널을 활성화
active_channels = [1, 1, 1]  # B, G, R
font_color = (255, 0, 255) # M
font_Scale = 1.0
while True:
    key = cv.waitKeyEx(1)
    current_frame = int(capture.get(cv.CAP_PROP_POS_FRAMES))
    capture.set(cv.CAP_PROP_POS_FRAMES, frame_index)  # 지정한 프레임 번호로 이동한다.
    _, frame = capture.read()
    cv.putText(frame, str(current_frame), (0, frame.shape[0]), cv.FONT_HERSHEY_SIMPLEX, font_Scale, font_color, 1, 1)
    # 각 픽셀에 scale 곱하기
    adjusted_frame = frame * scale

    # 0~255 범위로 클리핑 및 uint8으로 변환
    adjusted_frame = np.clip(adjusted_frame, 0, 255).astype(np.uint8)

    # 초기화
    displayed_frame = np.zeros_like(adjusted_frame)

    # 채널 활성화 상태에 따라 색상 채우기
    displayed_frame[..., 0] = adjusted_frame[..., 0] * active_channels[0]  # B 채널
    displayed_frame[..., 1] = adjusted_frame[..., 1] * active_channels[1]  # G 채널
    displayed_frame[..., 2] = adjusted_frame[..., 2] * active_channels[2]  # R 채널

    cv.imshow('Display', displayed_frame)
    match key:
        case 0x240000: #home 0번 프레임으로
            frame_index = 0
        case 0x230000: #end 마지막 프레임으로
            frame_index = 324
        case 0x210000: #pg up 프레임 10 증가
            frame_index = frame_index + 10
        case 0x220000: #pg down 프레임 10 감소
            frame_index = frame_index - 10
        case 0x260000: #arrow up 프레임 1 증가
            frame_index = frame_index + 1
        case 0x280000: #arrow down 프레임 1 감소
            frame_index = frame_index - 1
        case 2555904: #arrow right 밝기 증가
            scale = scale * 1.15
        case 2424832: #arrow left  밝기 감소
            scale = scale / 1.15
        case 0x31:  # 1번 키: 기존화면
            active_channels = [1, 1, 1]
            font_color = (255, 0, 255)
        case 0x32:  # 2번 키: R 화면
            active_channels = [0, 0, 1]  # R 채널만 활성화
            font_color = (0, 0, 255)
        case 0x33:  # 3번 키: G 화면
            active_channels = [0, 1, 0]  # G 채널만 활성화
            font_color = (0, 255, 0)
        case 0x34:  # 4번 키: B 화면
            active_channels = [1, 0, 0]  # B 채널만 활성화
            font_color = (255, 0, 0)
        case 0x73:  # s를 누르면 저장
            match active_channels:
                case [1, 0, 0]:
                    cv.imwrite(f"team1_{frame_index + 1}_blue.jpg", displayed_frame)  # 현재 프레임 저장
                    print(f"Frame saved as 'team1_{frame_index + 1}_blue.jpg'")
                case [0, 1, 0]:
                    cv.imwrite(f"team1_{frame_index + 1}_green.jpg", displayed_frame)  # 현재 프레임 저장
                    print(f"Frame saved as 'team1_{frame_index + 1}_green.jpg'")
                case [0, 0, 1]:
                    cv.imwrite(f"team1_{frame_index + 1}_red.jpg", displayed_frame)  # 현재 프레임 저장
                    print(f"Frame saved as 'team1_{frame_index + 1}_red.jpg'")
                case [1, 1, 1]:
                    cv.imwrite(f"team1_{frame_index + 1}.jpg", displayed_frame)  # 현재 프레임 저장
                    print(f"Frame saved as 'team1_{frame_index + 1}.jpg'")
        case 0x71: # q를 누르면 폰트크기 증가
            font_Scale = font_Scale * 1.15
        case 0x65: # e를 누르면 폰트크기 감소
            font_Scale = font_Scale / 1.15
        case 27:  # escape 누르면 종료
            break
capture.release()
cv.destroyAllWindows()